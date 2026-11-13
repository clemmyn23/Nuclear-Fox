import sys,os,datetime as dt; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from sim import *
d0,d1=dt.date(2026,11,2),dt.date(2026,11,10)
dok,_=prep("dok",d0,d1)
def biz(t):
    l=t.astimezone(SYD); return l.weekday()<5 and 8<=l.hour<19
other=[x for x in dok if x["cat"]=="other"]
act=[x["wait"] for x in other if biz(x["ready"])]
print(f"actual wait of NON-FE Docker builds (biz): p50={pct(act,50):.0f} p90={pct(act,90):.0f} p99={pct(act,99):.0f} n={len(act)}")
for N in [11,12,13,14,15]:
    for lab,bl in [("without FE",other),("with FE (now)",dok)]:
        r=simulate(bl,lambda t,N=N:N)
        w=[(r[x["id"]][0]-x["ready"]).total_seconds() for x in other if biz(x["ready"])]
        print(f"N={N:2d} {lab:14s} non-FE builds wait p50={pct(w,50):4.0f} p90={pct(w,90):5.0f} p99={pct(w,99):5.0f}")
