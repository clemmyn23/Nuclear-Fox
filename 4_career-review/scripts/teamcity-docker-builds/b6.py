import sys,os,collections,datetime as dt; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from trace import *
B=load_all()
def agg(pool,days):
    T=collections.Counter(); N=collections.Counter()
    for x in B:
        if x["pool"]==pool and x["s"].astimezone(SYD).date() in days and x["cat"]=="other":
            T[x["bt"]]+=(x["f"]-x["s"]).total_seconds()/3600; N[x["bt"]]+=1
    return {k:v/len(days) for k,v in T.items()},{k:v/len(days) for k,v in N.items()}
a=[dt.date(2026,10,28),dt.date(2026,10,29),dt.date(2026,10,30)]
b=[dt.date(2026,11,2),dt.date(2026,11,3),dt.date(2026,11,4),dt.date(2026,11,5),dt.date(2026,11,9),dt.date(2026,11,10)]
for pool in ["win","dok"]:
    A,An=agg(pool,a); Bb,Bn=agg(pool,b)
    rows=sorted(set(A)|set(Bb),key=lambda k:-(Bb.get(k,0)-A.get(k,0)))
    print(f"== {pool}: other total {sum(A.values()):.0f} -> {sum(Bb.values()):.0f} agent-h/weekday; top growers:")
    for k in rows[:8]: print(f"   {k[:85]:85s} {A.get(k,0):5.1f} -> {Bb.get(k,0):5.1f} h/wd  runs {An.get(k,0):5.1f} -> {Bn.get(k,0):5.1f}")
