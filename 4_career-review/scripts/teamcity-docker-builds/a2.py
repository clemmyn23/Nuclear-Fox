import sys,os; sys.path.insert(0,os.path.dirname(__file__))
from lib import *
import collections
checks=["validate_app","validate_shared","css","closure","webpack"]
OV0=ts("20261031T012200+0000"); OV1=ts("20261106T025000+0000")
def bycommit(v, lo=None, hi=None):
    m=collections.defaultdict(dict)
    for c in checks:
        for x in load(f"pr_{c}_{v}"):
            if lo and x["s"]<lo: continue
            if hi and x["s"]>hi: continue
            key=(x["branchName"],x["rev"])
            # keep first run per check per commit
            if c not in m[key] or x["q"]<m[key][c]["q"]: m[key][c]=x
    return m
W=bycommit("win",OV0,OV1); K=bycommit("dock",OV0,OV1)
def metrics(d):
    q0=min(x["q"] for x in d.values()); f1=max(x["f"] for x in d.values())
    return (f1-q0).total_seconds(), sum(x["dur"] for x in d.values()), max(x["dur"] for x in d.values()), max(x["queue"] or 0 for x in d.values())
# commits where both ran all 5 checks, all success
common=[k for k in W if k in K and len(W[k])==5 and len(K[k])==5 and all(x["status"]=="SUCCESS" for x in list(W[k].values())+list(K[k].values()))]
print("commits in overlap: win",len(W),"dock",len(K),"both, all-5 success:",len(common))
wm=[metrics(W[k]) for k in common]; km=[metrics(K[k]) for k in common]
for i,name in enumerate(["push->all green (wall)","summed agent time","slowest check run","max queue"]):
    a=[x[i] for x in wm]; b=[x[i] for x in km]
    print(f"{name:24s} WIN {summ(a)}\n{'':24s} DCK {summ(b)}")
    deltas=[aa-bb for aa,bb in zip(a,b)]
    wins=sum(1 for d in deltas if d>0)
    print(f"{'':24s} paired delta med={pct(deltas,50):.0f}s, docker faster in {wins}/{len(deltas)} ({100*wins/len(deltas):.0f}%)")
# paired per check same commit
print("\n=== paired per check (same commit, both SUCCESS)")
for c in checks:
    pairs=[(W[k][c]["dur"],K[k][c]["dur"],W[k][c]["queue"] or 0,K[k][c]["queue"] or 0) for k in W if k in K and c in W[k] and c in K[k] and W[k][c]["status"]=="SUCCESS" and K[k][c]["status"]=="SUCCESS"]
    a=[p[0] for p in pairs]; b=[p[1] for p in pairs]
    r=[bb/aa for aa,bb in pairs and [(p[0],p[1]) for p in pairs]]
    print(f"{c:16s} n={len(pairs)} win med={pct(a,50):.0f}s dock med={pct(b,50):.0f}s  med ratio={pct(r,50):.2f} ({(1-pct(r,50))*100:.0f}% faster) speedup x{pct(a,50)/pct(b,50):.1f} | queue win med={pct([p[2] for p in pairs],50):.0f} dock med={pct([p[3] for p in pairs],50):.0f}")
# after switch, docker only
print("\n=== Docker-only after Windows paused (>= 6 Nov 03:00 UTC)")
A=bycommit("dock",ts("20261106T030000+0000"),None)
full=[k for k in A if len(A[k])==5 and all(x["status"]=="SUCCESS" for x in A[k].values())]
am=[metrics(A[k]) for k in full]
for i,name in enumerate(["push->all green (wall)","summed agent time","slowest check run","max queue"]):
    print(f"{name:24s} {summ([x[i] for x in am])}")
print("\n=== Windows full period, all-5 commits")
Wf=bycommit("win")
full=[k for k in Wf if len(Wf[k])==5 and all(x["status"]=="SUCCESS" for x in Wf[k].values())]
wm2=[metrics(Wf[k]) for k in full]
for i,name in enumerate(["push->all green (wall)","summed agent time","slowest check run","max queue"]):
    print(f"{name:24s} {summ([x[i] for x in wm2])}")
