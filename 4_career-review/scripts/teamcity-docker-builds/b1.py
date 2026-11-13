import sys,os,collections,datetime as dt; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from trace import *
B=load_all()
N={"win":26,"dok":11}
print("pool day       util24  util9-18 | FE-PR  FE-pkg other (% of 9-18 capacity) | agents seen")
days=sorted({x["s"].astimezone(SYD).date() for x in B})
for pool in ["win","dok"]:
    for d in days:
        lo=dt.datetime(d.year,d.month,d.day,tzinfo=SYD); hi=lo+dt.timedelta(days=1)
        blo=lo+dt.timedelta(hours=9); bhi=lo+dt.timedelta(hours=18)
        tot=0; bus=collections.Counter(); ags=set()
        for x in B:
            if x["pool"]!=pool: continue
            s=max(x["s"],lo); f=min(x["f"],hi)
            if f>s: tot+=(f-s).total_seconds(); ags.add(x["agent"])
            s=max(x["s"],blo); f=min(x["f"],bhi)
            if f>s: bus[x["cat"].split(" (")[0] if x["cat"]!="other" else "other"]+=(f-s).total_seconds()
        cap24=N[pool]*86400; capb=N[pool]*9*3600
        b=sum(bus.values())
        print(f"{pool} {d} {d.strftime('%a')} {100*tot/cap24:5.1f}% {100*b/capb:6.1f}% | {100*bus['FE PR']/capb:5.1f} {100*bus['FE package']/capb:5.1f} {100*bus['other']/capb:5.1f} | {len(ags)}")
