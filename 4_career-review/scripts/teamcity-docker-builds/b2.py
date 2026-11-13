import sys,os,collections,datetime as dt; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from trace import *
from lib import pct
B=load_all()
def weekdays(a,b):
    d=a; out=[]
    while d<=b:
        if d.weekday()<5: out.append(d)
        d+=dt.timedelta(days=1)
    return out
periods={
 "Oct 28-30 (before)": weekdays(dt.date(2026,10,28),dt.date(2026,10,30)),
 "Nov 2-5 (both ran)": weekdays(dt.date(2026,11,2),dt.date(2026,11,5)),
 "Nov 9-10 (after)": weekdays(dt.date(2026,11,9),dt.date(2026,11,10)),
}
# agent-hours per weekday by pool x category
print("== agent-hours per weekday (24h)")
for name,days in periods.items():
    T=collections.Counter()
    ds=set(days)
    for x in B:
        if x["s"].astimezone(SYD).date() in ds: T[(x["pool"],x["cat"])]+=(x["f"]-x["s"]).total_seconds()/3600
    print(name, {f"{p}/{c}":round(v/len(days),1) for (p,c),v in sorted(T.items())})
# minute-resolution busy agents, weekday 08-19 local; report mean + p95 by category per pool
print("\n== busy agents (weekday 09-18 AEDT): mean / p95 / max, sampled per minute")
for name,days in periods.items():
    for pool in ["win","dok"]:
        res={}
        for catsel in ["all","FE"]:
            samples=[]
            for d in days:
                lo=dt.datetime(d.year,d.month,d.day,9,tzinfo=SYD)
                cnt=[0]*(9*60)
                for x in B:
                    if x["pool"]!=pool: continue
                    if catsel=="FE" and not x["cat"].startswith("FE"): continue
                    s=int((x["s"]-lo).total_seconds()//60); f=int((x["f"]-lo).total_seconds()//60)
                    for m in range(max(s,0),min(f+1,9*60)): cnt[m]+=1
                samples+=cnt
            res[catsel]=(sum(samples)/len(samples),pct(samples,95),max(samples))
        print(f"  {name:20s} {pool}: all mean={res['all'][0]:.1f} p95={res['all'][1]:.0f} max={res['all'][2]} | FE mean={res['FE'][0]:.2f} p95={res['FE'][1]:.0f} max={res['FE'][2]}")
