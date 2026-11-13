import sys,os; sys.path.insert(0,os.path.dirname(__file__))
from lib import *
import collections
checks=["validate_app","validate_shared","css","closure","webpack"]
OV0=ts("20261031T012200+0000"); OV1=ts("20261106T025000+0000")
print("=== Per check, all finished SUCCESS builds")
for c in checks:
    for v in ["win","dock"]:
        b=[x for x in load(f"pr_{c}_{v}") if x["status"]=="SUCCESS"]
        days=(max(x["s"] for x in b)-min(x["s"] for x in b)).total_seconds()/86400
        hrs=sum(x["dur"] for x in b)/3600
        print(f"{c:16s} {v:4s} dur {summ([x['dur'] for x in b])} | queue med={pct([x['queue'] for x in b if x['queue'] is not None],50):.0f}s p90={pct([x['queue'] for x in b if x['queue'] is not None],90):.0f} | {len(b)/days:.1f}/day agent-h={hrs:.1f} over {days:.1f}d")
print()
print("=== Overlap window only (both running), SUCCESS")
for c in checks:
    for v in ["win","dock"]:
        b=[x for x in load(f"pr_{c}_{v}") if x["status"]=="SUCCESS" and OV0<=x["s"]<=OV1]
        print(f"{c:16s} {v:4s} {summ([x['dur'] for x in b])}")
