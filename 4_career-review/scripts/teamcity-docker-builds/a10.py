import sys,os,json,collections; sys.path.insert(0,os.path.dirname(__file__))
from lib import *
checks=["validate_app","validate_shared","css","closure","webpack"]
OV0=ts("20261031T012200+0000"); OV1=ts("20261106T025000+0000")
days=(OV1-OV0).total_seconds()/86400
print(f"overlap window {days:.2f} days")
T={"win":[0,0,set()],"dock":[0,0,set()]}
for v in T:
    for c in checks:
        for x in load(f"pr_{c}_{v}"):
            if OV0<=x["s"]<=OV1:
                T[v][0]+=1; T[v][1]+=x["dur"]; T[v][2].add((x["branchName"],x["rev"]))
for v,(n,s,cm) in T.items():
    print(f"{v}: runs={n} ({n/days:.0f}/day) agent-h={s/3600:.1f} ({s/3600/days:.1f}/day) distinct PR commits={len(cm)} ({len(cm)/days:.0f}/day) distinct PRs={len({b for b,r in cm})}")
w=T["win"]; d=T["dock"]
print(f"agent-h reduction {(1-d[1]/w[1])*100:.0f}%  runs reduction {(1-d[0]/w[0])*100:.0f}%")
print(f"annualised agent-h saved ~{(w[1]-d[1])/3600/days*365:.0f}")
# Commits Windows ran but Docker skipped (trigger scoping)
onlyw=T["win"][2]-T["dock"][2]
print("commits Windows checked but Docker did not trigger on:",len(onlyw))
