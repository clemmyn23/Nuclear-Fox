import sys,os; sys.path.insert(0,os.path.dirname(__file__))
from lib import *
import collections
checks=["validate_app","validate_shared","css","closure","webpack"]
for v in ["win","dock"]:
    R=collections.Counter(); tot=0; n=0
    for c in checks:
        for x in load(f"pr_{c}_{v}"):
            n+=1
            for k,val in x["stats"].items():
                if k.startswith("queueWaitReason:"): R[k[16:]]+=float(val)/1000
            tot+=x["queue"] or 0
    print(f"== {v}: builds={n} total queue h={tot/3600:.1f}")
    for k,s in R.most_common(8): print(f"   {s/3600:7.1f} h  {k}")
# docker queue by day
print("\n== Docker PR checks: per UTC day: builds, median queue, p90 queue, distinct agents")
for v in ["dock","win"]:
    byday=collections.defaultdict(list); ag=collections.defaultdict(set)
    for c in checks:
        for x in load(f"pr_{c}_{v}"):
            d=x["s"].astimezone().strftime("%m-%d %a")
            byday[d].append(x["queue"] or 0); ag[d].add(x["agentname"])
    print(v)
    for d in sorted(byday): print(f"  {d} n={len(byday[d]):4d} q med={pct(byday[d],50):5.0f}s p90={pct(byday[d],90):5.0f}s agents={len(ag[d])}")
