import sys,os,json,glob,collections; sys.path.insert(0,os.path.dirname(__file__))
from lib import *
D=os.environ["TCD"]
B=[]
for f in glob.glob(os.path.join(D,"pool_*.json")):
    for x in json.load(open(f)).get("build",[]):
        if x.get("startDate") and x.get("finishDate"):
            x["s"]=ts(x["startDate"]); x["f"]=ts(x["finishDate"]); x["a"]=x["agent"]["name"]; B.append(x)
FE="CreatesendCom_MonolithMergeChecks_FrontendMergeChecks_"
PKG="FrontendPackage"
def cat(bt):
    if bt.startswith(FE): return "FE PR checks (Docker)"
    if PKG in bt: return "FE package (Docker)"
    return "everything else"
# only Sydney agents, business hours Sydney (Mon-Fri 9-18 local)
import zoneinfo
syd=zoneinfo.ZoneInfo("Australia/Sydney")
def week(lo,hi,label):
    T=collections.Counter(); n=collections.Counter()
    for x in B:
        if not x["a"].startswith("apse2c"): continue
        if not (lo<=x["s"]<hi): continue
        T[cat(x["buildTypeId"])]+=(x["f"]-x["s"]).total_seconds(); n[cat(x["buildTypeId"])]+=1
    tot=sum(T.values())
    # capacity in business hours: 11 agents * hours
    print(f"== {label}: total busy agent-h on Sydney Docker agents={tot/3600:.0f}")
    for k,v in T.most_common(): print(f"   {k:24s} {v/3600:6.1f} h ({100*v/tot:4.1f}%) builds={n[k]}")
week(ts("20261020T000000+0000"),ts("20261031T000000+0000"),"20-30 Oct (before Docker PR checks)")
week(ts("20261031T000000+0000"),ts("20261106T030000+0000"),"31 Oct-6 Nov (overlap)")
week(ts("20261106T030000+0000"),ts("20261111T000000+0000"),"6-10 Nov (after switch)")
# business-hour utilisation per day: busy agent-seconds between 09:00-18:00 Sydney / (agents*9h)
print("\n== Sydney Docker agents, weekday 09-18 AEDT utilisation")
import datetime as dt
days=sorted({x["s"].astimezone(syd).date() for x in B})
for d in days:
    if d.weekday()>=5: continue
    lo=dt.datetime(d.year,d.month,d.day,9,tzinfo=syd); hi=lo+dt.timedelta(hours=9)
    busy=collections.Counter(); ags=set()
    for x in B:
        if not x["a"].startswith("apse2c"): continue
        s=max(x["s"],lo); f=min(x["f"],hi)
        if f>s: busy[cat(x["buildTypeId"])]+=(f-s).total_seconds(); ags.add(x["a"])
    cap=11*9*3600
    tot=sum(busy.values())
    print(f"  {d} util={100*tot/cap:5.1f}%  FE-PR={100*busy['FE PR checks (Docker)']/cap:4.1f}%  FE-pkg={100*busy['FE package (Docker)']/cap:4.1f}%  other={100*busy['everything else']/cap:4.1f}%")
