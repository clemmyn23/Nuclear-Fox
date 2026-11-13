import sys,os,json,collections,datetime as dt,math; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from sim import *
PRICE=0.9644; HM=730; PF=75.83/168
d0,d1=dt.date(2026,11,2),dt.date(2026,11,10)
win,miss=prep("win",d0,d1)
print("windows builds",len(win),"missing stats",miss)
def is_peak(t):
    l=t.astimezone(SYD); m=l.hour*60+l.minute
    return l.weekday()<5 and 5*60+50<=m<20*60+30
def biz(t):
    l=t.astimezone(SYD); return l.weekday()<5 and 8<=l.hour<19
def rep(label,bl,res,c):
    wb=[(res[x["id"]][0]-x["ready"]).total_seconds() for x in bl if biz(x["ready"])]
    wo=[(res[x["id"]][0]-x["ready"]).total_seconds() for x in bl if not is_peak(x["ready"])]
    return f"{label:40s} wait biz p50={pct(wb,50):4.0f} p90={pct(wb,90):5.0f} p99={pct(wb,99):5.0f} | off-peak p90={pct(wo,90):4.0f} p99={pct(wo,99):5.0f} | ${c:,.0f}/mo"
act={x["id"]:(x["s"],x["f"]) for x in win}
print(rep("ACTUAL 26 (incl FE PR until 6 Nov)",win,act,26*PRICE*HM))
print(rep("SIM 26 (calibration, same load)",win,simulate(win,lambda t:26),26*PRICE*HM))
nofe=[x for x in win if x["cat"]=="other"]
print(f"\n== Windows without any FE work (after JC-414): {len(nofe)} builds")
for N in [26,24,22,20,18]:
    print(rep(f"{N} always-on",nofe,simulate(nofe,lambda t,N=N:N),N*PRICE*HM))
for N,Noff in [(26,13),(24,12),(22,11),(24,8),(22,8)]:
    c=(N*PF+Noff*(1-PF))*PRICE*HM
    print(rep(f"{N} peak / {Noff} off-peak",nofe,simulate(nofe,lambda t,N=N,Noff=Noff: N if is_peak(t) else Noff),c))
