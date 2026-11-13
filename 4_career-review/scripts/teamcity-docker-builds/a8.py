import sys,os,json,collections; sys.path.insert(0,os.path.dirname(__file__))
from lib import *
L={x["number"]:x for x in load("deploy_legacy")}
K={x["number"]:x for x in load("deploy_docker")}
print("docker statuses:", collections.Counter((x["status"],(x.get("statusText") or "")[:60]) for x in K.values()))
def st(x,k): return float(x["stats"].get(k,0))/1000
pairs=[(L[n],K[n]) for n in K if n in L and K[n]["status"]=="SUCCESS" and L[n]["status"]=="SUCCESS"]
print("paired:",len(pairs))
lw=[a["dur"] for a,b in pairs]; dk=[b["dur"] for a,b in pairs]
print("legacy total",summ(lw)); print("docker total",summ(dk))
r=[b/a for a,b in zip(lw,dk)]; print(f"paired ratio med {pct(r,50):.2f} -> {100*(1-pct(r,50)):.0f}% faster; docker faster in {sum(1 for x in r if x<1)}/{len(r)}")
# legacy stages
stages_l={"checkout":"buildStageDuration:sourcesUpdate","npm install":"buildStageDuration:buildStepRUNNER_965","JS build (yarn run build)":"buildStageDuration:buildStepRUNNER_670","nuget pack":"buildStageDuration:buildStepRUNNER_674","nuget push":"buildStageDuration:buildStepRUNNER_677","cleanup":"buildStageDuration:buildStepRUNNER_672","artifact publish":"buildStageDuration:artifactsPublishing","prep":"buildStageDuration:firstStepPreparation"}
stages_k={"checkout":"buildStageDuration:sourcesUpdate","compare check":"buildStageDuration:buildStepRUNNER_1","tasks.sh build (install+build in container)":"buildStageDuration:buildStepRUNNER_2","remove image":"buildStageDuration:buildStepRUNNER_3","artifact publish":"buildStageDuration:artifactsPublishing","finishing":"buildStageDuration:buildFinishing"}
print("\nlegacy stages (paired):")
for n,k in stages_l.items(): print(f"  {n:45s} med {pct([st(a,k) for a,b in pairs],50):6.1f}s")
print("docker stages (paired):")
for n,k in stages_k.items(): print(f"  {n:45s} med {pct([st(b,k) for a,b in pairs],50):6.1f}s")
lw_like=[st(a,stages_l['checkout'])+st(a,stages_l['npm install'])+st(a,stages_l['JS build (yarn run build)']) for a,b in pairs]
dk_like=[st(b,stages_k['checkout'])+st(b,stages_k['tasks.sh build (install+build in container)']) for a,b in pairs]
print("like-for-like checkout+install+build: legacy",summ(lw_like)," docker",summ(dk_like))
print("artifacts size: legacy med",pct([st(a,'ArtifactsSize')*1000/1e6 for a,b in pairs],50),"MB docker",pct([st(b,'ArtifactsSize')*1000/1e6 for a,b in pairs],50),"MB")
print("queue: legacy",summ([a["queue"] for a,b in pairs])," docker",summ([b["queue"] for a,b in pairs]))
print("tests: legacy", collections.Counter(a["stats"].get("PassedTestCount") for a,b in pairs), "docker", collections.Counter(b["stats"].get("PassedTestCount") for a,b in pairs))
# legacy full-history (30 days) for stability
lall=[x for x in L.values() if x["status"]=="SUCCESS"]
print("\nlegacy 30-day:",summ([x["dur"] for x in lall]), "runs/day", len(lall)/((max(x['s'] for x in lall)-min(x['s'] for x in lall)).total_seconds()/86400))
print("legacy npm install 30d", summ([st(x,stages_l['npm install']) for x in lall]))
print("legacy checkout 30d", summ([st(x,stages_l['checkout']) for x in lall]))
print("legacy build 30d", summ([st(x,stages_l['JS build (yarn run build)']) for x in lall]))
# control backend
C=[x for x in load("deploy_backend_control") if x["status"]=="SUCCESS"]
cut=ts("20261106T000000+0000")
print("\ncontrol (Web Package Backend) before 6 Nov",summ([x["dur"] for x in C if x["s"]<cut])," after",summ([x["dur"] for x in C if x["s"]>=cut]))
print("legacy FE package before 6 Nov",summ([x["dur"] for x in lall if x["s"]<cut])," after",summ([x["dur"] for x in lall if x["s"]>=cut]))
