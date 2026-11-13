import json, subprocess, sys, os, glob
from concurrent.futures import ThreadPoolExecutor
D = sys.argv[1]
os.makedirs(os.path.join(D,"stats"), exist_ok=True)
ids=[]
for f in glob.glob(os.path.join(D,"*.json")):
    for b in json.load(open(f)):
        if b.get("state")=="finished": ids.append(b["id"])
cache=os.path.join(D,"stats")
todo=[i for i in ids if not os.path.exists(os.path.join(cache,f"{i}.json"))]
print("total",len(ids),"todo",len(todo), flush=True)
def get(i):
    r=subprocess.run(["teamcity","api",f"/app/rest/builds/id:{i}/statistics"],capture_output=True,text=True)
    if r.returncode==0:
        try:
            d={p["name"]:p["value"] for p in json.loads(r.stdout).get("property",[])}
            json.dump(d,open(os.path.join(cache,f"{i}.json"),"w"))
            return 1
        except Exception: return 0
    return 0
with ThreadPoolExecutor(12) as ex:
    ok=sum(ex.map(get,todo))
print("fetched",ok)
