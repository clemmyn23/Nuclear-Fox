import sys,os,json,collections,datetime as dt,copy,math; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from sim import *
D=os.environ["TCD"]
d0,d1=dt.date(2026,11,2),dt.date(2026,11,10)
PRICE={"dok":0.432,"win":0.9644}   # USD/h on-demand Sydney, AWS price list 2026-11-07
HOURS_MONTH=730; PEAK_FRAC=75.83/168  # weekdays 05:20-20:30 full size
dok,miss=prep("dok",d0,d1); win,missw=prep("win",d0,d1)
print(f"docker builds {len(dok)} missing stats {miss}; windows builds {len(win)} missing stats {missw}")
cm={}; q={}
for c in ["validate_app","validate_shared","css","closure","webpack"]:
    for x in json.load(open(os.path.join(D,f"pr_{c}_dock.json"))):
        revs=(x.get("revisions") or {}).get("revision") or []
        cm[x["id"]]=(x.get("branchName"),revs[0]["version"] if revs else None,c); q[x["id"]]=ts(x["queuedDate"])
def is_peak(t):
    l=t.astimezone(SYD); m=l.hour*60+l.minute
    return l.weekday()<5 and 5*60+50<=m<20*60+30
def biz(t):
    l=t.astimezone(SYD); return l.weekday()<5 and 8<=l.hour<19
def p2g(builds,res):
    by=collections.defaultdict(dict)
    for x in builds:
        if x["id"] in cm:
            b,r,c=cm[x["id"]]
            if c not in by[(b,r)] or q[x["id"]]<q[by[(b,r)][c]["id"]]: by[(b,r)][c]=x
    out=[]
    for v in by.values():
        if len(v)<5: continue
        t0=min(q[x["id"]] for x in v.values())
        if biz(t0): out.append((max(res[x["id"]][1] for x in v.values())-t0).total_seconds())
    return out
def wt(builds,res,sel): return [(res[x["id"]][0]-x["ready"]).total_seconds() for x in builds if sel(x)]
def cost(pool,Npeak,offpeak):
    if not offpeak: return Npeak*PRICE[pool]*HOURS_MONTH
    Noff=Npeak-math.floor(Npeak*0.70) if pool=="dok" else offpeak
    return (Npeak*PEAK_FRAC+Noff*(1-PEAK_FRAC))*PRICE[pool]*HOURS_MONTH
def sched(Npeak,Noff):
    return (lambda t: Npeak if is_peak(t) else Noff)
def report(label,builds,res,c):
    p=p2g(builds,res)
    wb=wt(builds,res,lambda x:biz(x["ready"])); wo=wt(builds,res,lambda x:not is_peak(x["ready"]))
    return f"{label:34s} push->green p50={pct(p,50):5.0f} p90={pct(p,90):5.0f} | wait biz p50={pct(wb,50):4.0f} p90={pct(wb,90):5.0f} p99={pct(wb,99):5.0f} | off-peak wait p90={pct(wo,90):4.0f} p99={pct(wo,99):5.0f} | ${c:,.0f}/mo"
actual={x["id"]:(x["s"],x["f"]) for x in dok}
print("TARGET (Windows era 27 Oct-6 Nov): push->green p50=327 p90=827")
print(report("ACTUAL Docker (11 agents)",dok,actual,cost("dok",11,False)))
print(report("SIM 11 always-on (calibration)",dok,simulate(dok,lambda t:11),cost("dok",11,False)))
# after JC-414: add package builds
win_pkg=[x for x in win if x["cat"]=="FE package (Windows)"]
shadow_days={x["s"].astimezone(SYD).date() for x in dok if x["cat"]=="FE package (Docker shadow)"}
dok414=[]
for x in dok:
    y=dict(x)
    if x["cat"]=="FE package (Docker shadow)": y["dur"]=x["dur"]+15
    dok414.append(y)
for x in win_pkg:
    if x["s"].astimezone(SYD).date() in shadow_days: continue
    y=dict(x); y["id"]=-x["id"]; y["pool"]="dok"; y["cat"]="FE package (Docker)"; y["dur"]=305.0
    dok414.append(y)
print(f"JC-414 scenario adds {len(dok414)-len(dok)} Docker package builds")
for scen,bl in [("NOW",dok),("AFTER JC-414",dok414)]:
    print(f"\n== {scen}")
    for N in range(11,21):
        print(report(f"{N} always-on",bl,simulate(bl,lambda t,N=N:N),cost("dok",N,False)))
    for N in range(12,21):
        Noff=N-math.floor(N*0.70)
        print(report(f"{N} peak / {Noff} off-peak (module 70%)",bl,simulate(bl,sched(N,Noff)),cost("dok",N,True)))
    for N in range(12,19):
        for Noff in (6,8):
            c=(N*PEAK_FRAC+Noff*(1-PEAK_FRAC))*PRICE["dok"]*HOURS_MONTH
            print(report(f"{N} peak / {Noff} off-peak",bl,simulate(bl,sched(N,Noff)),c))
