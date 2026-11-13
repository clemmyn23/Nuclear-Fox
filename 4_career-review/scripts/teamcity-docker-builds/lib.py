import json, glob, os, statistics as st
from datetime import datetime, timezone
D = os.environ["TCD"]
def ts(s): return datetime.strptime(s, "%Y%m%dT%H%M%S%z") if s else None
def load(k):
    out=[]
    for b in json.load(open(os.path.join(D,k+".json"))):
        if b.get("state")!="finished": continue
        p=os.path.join(D,"stats",f"{b['id']}.json")
        s=json.load(open(p)) if os.path.exists(p) else {}
        b["stats"]=s
        b["q"]=ts(b.get("queuedDate")); b["s"]=ts(b.get("startDate")); b["f"]=ts(b.get("finishDate"))
        b["dur"]=(b["f"]-b["s"]).total_seconds() if b["s"] and b["f"] else None
        b["queue"]=float(s.get("TimeSpentInQueue",0))/1000 if s.get("TimeSpentInQueue") else ((b["s"]-b["q"]).total_seconds() if b["q"] and b["s"] else None)
        revs=(b.get("revisions") or {}).get("revision") or []
        b["rev"]=revs[0]["version"] if revs else None
        b["agentname"]=(b.get("agent") or {}).get("name")
        out.append(b)
    return out
def pct(xs,p):
    xs=sorted(xs); 
    if not xs: return None
    k=(len(xs)-1)*p/100; f=int(k); c=min(f+1,len(xs)-1)
    return xs[f]+(xs[c]-xs[f])*(k-f)
def summ(xs):
    xs=[x for x in xs if x is not None]
    if not xs: return "n=0"
    return f"n={len(xs)} med={pct(xs,50):.0f}s p25={pct(xs,25):.0f} p75={pct(xs,75):.0f} p90={pct(xs,90):.0f} mean={st.mean(xs):.0f} min={min(xs):.0f} max={max(xs):.0f}"
