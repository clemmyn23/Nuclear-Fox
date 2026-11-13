import json, subprocess, sys, os, glob
from concurrent.futures import ThreadPoolExecutor
D=sys.argv[1]; pre=sys.argv[2]; cache=os.path.join(D,"stats")
ids=[x["id"] for f in glob.glob(os.path.join(D,"days","*.json")) if "2026-11-02"<=os.path.basename(f)[:10]<="2026-11-10" for x in json.load(open(f)) if ((x.get("agent") or {}).get("name") or "").startswith(pre)]
todo=[i for i in reversed(ids) if not os.path.exists(os.path.join(cache,f"{i}.json"))]
print(pre,"todo",len(todo),flush=True)
def get(i):
    if os.path.exists(os.path.join(cache,f"{i}.json")): return 1
    r=subprocess.run(["teamcity","api",f"/app/rest/builds/id:{i}/statistics"],capture_output=True,text=True)
    if r.returncode==0:
        try:
            d={p["name"]:p["value"] for p in json.loads(r.stdout).get("property",[])}
            json.dump(d,open(os.path.join(cache,f"{i}.json"),"w")); return 1
        except Exception: return 0
    return 0
with ThreadPoolExecutor(12) as ex: ok=sum(ex.map(get,todo))
print("done",ok,flush=True)
