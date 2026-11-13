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
periods={"Oct 28-30 (before)": weekdays(dt.date(2026,10,28),dt.date(2026,10,30)),
 "Nov 2-5 (both ran)": weekdays(dt.date(2026,11,2),dt.date(2026,11,5)),
 "Nov 9-10 (after)": weekdays(dt.date(2026,11,9),dt.date(2026,11,10))}
# exact: sweep events, sample busy count at every 10 s instant
for name,days in periods.items():
    for pool in ["win","dok"]:
        out={}
        for sel in ["all","FE"]:
            samples=[]
            for d in days:
                lo=dt.datetime(d.year,d.month,d.day,9,tzinfo=SYD); hi=lo+dt.timedelta(hours=9)
                ev=[]
                for x in B:
                    if x["pool"]!=pool or x["f"]<=lo or x["s"]>=hi: continue
                    if sel=="FE" and not x["cat"].startswith("FE"): continue
                    ev.append((x["s"],x["f"]))
                step=10; n=int(9*3600/step)
                diff=[0]*(n+1)
                for s,f in ev:
                    a=max(0,int((s-lo).total_seconds()//step)+1); b=min(n,int((f-lo).total_seconds()//step))
                    if b>=a: diff[a]+=1; diff[b+1 if b+1<=n else n]-=1
                c=0
                for i in range(n):
                    c+=diff[i]; samples.append(c)
            out[sel]=(sum(samples)/len(samples),pct(samples,90),pct(samples,99),max(samples))
        a=out["all"]; f=out["FE"]
        print(f"{name:20s} {pool}: busy mean={a[0]:5.1f} p90={a[1]:3.0f} p99={a[2]:3.0f} max={a[3]:3d} | FE mean={f[0]:.2f} p90={f[1]:.0f} p99={f[2]:.0f} max={f[3]}")
