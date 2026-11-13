import sys,os,json,collections; sys.path.insert(0,os.path.dirname(__file__))
from lib import *
checks=["validate_app","validate_shared","css","closure","webpack"]
allb=[]
for c in checks:
    b=[x for x in load(f"pr_{c}_dock") if x["status"]=="SUCCESS"]
    med=pct([x["dur"] for x in b],50)
    cold=[x for x in b if x["dur"]>med+40]
    print(f"{c:16s} med={med:.0f}s cold(>{med+40:.0f}s)={len(cold)}/{len(b)} ({100*len(cold)/len(b):.0f}%) cold med={pct([x['dur'] for x in cold],50):.0f}s warm med={pct([x['dur'] for x in b if x not in cold],50):.0f}s")
    for x in b: x["cold"]=x in cold; x["chk"]=c
    allb+=b
# are cold runs clustered by commit (deps change) -> same rev cold in all checks?
byrev=collections.defaultdict(list)
for x in allb: byrev[(x["branchName"],x["rev"])].append(x["cold"])
allcold=sum(1 for v in byrev.values() if len(v)==5 and all(v)); anycold=sum(1 for v in byrev.values() if any(v))
print("commits with all 5 cold:",allcold,"any cold:",anycold,"of",len(byrev))
# per agent first build of day?
byag=collections.defaultdict(list)
for x in allb: byag[x["agentname"]].append(x)
first=0; firstcold=0
for a,xs in byag.items():
    xs.sort(key=lambda x:x["s"])
    prev=None
    for x in xs:
        gap=(x["s"]-prev).total_seconds()/3600 if prev else 999
        if gap>6: 
            first+=1; firstcold+=x["cold"]
        prev=x["f"]
print("first FE build on an agent after >6h idle:",first,"of which cold",firstcold)
# Failures
print("\n=== failures")
for v in ["win","dock"]:
    for c in checks:
        for x in load(f"pr_{c}_{v}"):
            if x["status"]!="SUCCESS": print(v,c,x["s"].strftime("%m-%d %H:%M"),x["branchName"],(x.get("statusText") or "")[:110])
