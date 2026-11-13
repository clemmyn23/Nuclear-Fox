import sys,os,json,heapq,collections,datetime as dt; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from trace import *
from lib import pct
D=os.environ["TCD"]
AGENT_WAIT="queueWaitReason:There_are_no_idle_compatible_agents_which_can_run_this_build"
def stats(i):
    p=os.path.join(D,"stats",f"{i}.json")
    return json.load(open(p)) if os.path.exists(p) else None
def prep(pool, day_from, day_to):
    B=[x for x in load_all() if x["pool"]==pool and day_from<=x["s"].astimezone(SYD).date()<=day_to]
    out=[]; miss=0
    for x in B:
        s=stats(x["id"])
        if s is None: miss+=1; w=0.0
        else: w=float(s.get(AGENT_WAIT,0))/1000
        x["wait"]=w; x["ready"]=x["s"]-dt.timedelta(seconds=w); x["dur"]=(x["f"]-x["s"]).total_seconds()
        out.append(x)
    return out,miss
def simulate(builds, n_agents_fn):
    """FIFO, identical agents. n_agents_fn(t) -> number of agents available at time t (schedule)."""
    bs=sorted(builds,key=lambda x:x["ready"])
    free=[]  # heap of agent free times
    # model capacity schedule by checking count at each start; simple: fixed N per build's ready time
    res={}
    agents=[]
    for x in bs:
        N=n_agents_fn(x["ready"])
        while len(agents)<N: heapq.heappush(agents,x["ready"])
        # if capacity shrank, drop agents that are free (keep busy ones)
        while len(agents)>N and agents and agents[0]<=x["ready"]: heapq.heappop(agents)
        t=heapq.heappop(agents)
        start=max(t,x["ready"])
        fin=start+dt.timedelta(seconds=x["dur"])
        heapq.heappush(agents,fin)
        res[x["id"]]=(start,fin)
    return res
