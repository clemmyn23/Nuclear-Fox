import sys,os,json,re,collections; sys.path.insert(0,os.path.dirname(__file__))
from lib import *
names={}
cur=None
for line in open(os.path.join(os.path.dirname(__file__),"steps.txt")):
    pass
checks=["validate_app","validate_shared","css","closure","webpack"]
for c in checks:
    for v in ["win","dock"]:
        b=[x for x in load(f"pr_{c}_{v}") if x["status"]=="SUCCESS"]
        keys=collections.defaultdict(list)
        for x in b:
            for k,val in x["stats"].items():
                if k.startswith("buildStageDuration:"): keys[k[19:]].append(float(val)/1000)
        parts=", ".join(f"{k}={pct(vs,50):.0f}" for k,vs in sorted(keys.items()) if pct(vs,50)>=1)
        print(f"{c:16s} {v:4s} {parts}")
