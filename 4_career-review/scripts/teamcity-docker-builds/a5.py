import sys,os,json,glob,collections; sys.path.insert(0,os.path.dirname(__file__))
from lib import *
D=os.environ["TCD"]
B=[]
for f in glob.glob(os.path.join(D,"pool_*.json")):
    for x in json.load(open(f)).get("build",[]):
        if x.get("startDate") and x.get("finishDate") and x["agent"]["name"].startswith("apse2c"):
            x["s"]=ts(x["startDate"]); x["f"]=ts(x["finishDate"]); B.append(x)
def agg(lo,hi):
    T=collections.Counter(); N=collections.Counter()
    for x in B:
        if lo<=x["s"]<hi: T[x["buildTypeId"]]+=(x["f"]-x["s"]).total_seconds(); N[x["buildTypeId"]]+=1
    return T,N
a,an=agg(ts("20261020T000000+0000"),ts("20261028T000000+0000"))
b,bn=agg(ts("20261102T000000+0000"),ts("20261111T000000+0000"))
# per-day normalise: 8 days vs 9 days
rows=[(k,a[k]/8/3600,b[k]/9/3600,an[k],bn[k]) for k in set(a)|set(b)]
rows.sort(key=lambda r:-(r[2]-r[1]))
print(f"{'buildType':95s} before h/day  after h/day  runs before/after")
for k,x,y,n1,n2 in rows[:15]: print(f"{k:95s} {x:6.2f}  {y:6.2f}   {n1}/{n2}")
