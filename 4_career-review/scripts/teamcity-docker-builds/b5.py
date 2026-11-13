import sys,os,collections,datetime as dt; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from trace import *
from lib import pct
B=load_all()
lo=dt.datetime(2026,10,13,tzinfo=SYD); hi=dt.datetime(2026,11,11,tzinfo=SYD)
step=30; n=int((hi-lo).total_seconds()//step)
def peak(t):
    l=t.astimezone(SYD)
    if l.weekday()>=5: return False
    m=l.hour*60+l.minute
    return 5*60+50 <= m < 20*60+30
for pool,N in [("dok",11),("win",26)]:
    diff=[0]*(n+2)
    for x in B:
        if x["pool"]!=pool: continue
        a=max(0,int((x["s"]-lo).total_seconds()//step)+1); b=min(n,int((x["f"]-lo).total_seconds()//step))
        if b>=a: diff[a]+=1; diff[b+1]-=1
    c=0; on=[]; off=[]; offn=collections.Counter()
    for i in range(n):
        c+=diff[i]; t=lo+dt.timedelta(seconds=i*step)
        (on if peak(t) else off).append(c)
    print(f"{pool}: PEAK window busy mean={sum(on)/len(on):.1f} p90={pct(on,90):.0f} p99={pct(on,99):.0f} max={max(on)} | OFF-PEAK busy mean={sum(off)/len(off):.2f} p90={pct(off,90):.0f} p99={pct(off,99):.0f} p99.9={pct(off,99.9):.0f} max={max(off)}; share of agent-time off-peak={sum(off)/(sum(on)+sum(off))*100:.1f}%")
    # which off-peak hours are busiest
    hrs=collections.defaultdict(list)
    c=0
    for i in range(n):
        c+=diff[i]; t=(lo+dt.timedelta(seconds=i*step)).astimezone(SYD)
        if not peak(t): hrs[("we" if t.weekday()>=5 else "wd",t.hour)].append(c)
    top=sorted(hrs.items(),key=lambda kv:-pct(kv[1],99))[:6]
    print("   busiest off-peak hours (p99 busy):", ", ".join(f"{k[0]} {k[1]:02d}h={pct(v,99):.0f}" for k,v in top))
