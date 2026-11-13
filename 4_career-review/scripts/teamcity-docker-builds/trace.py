import json,glob,os,collections,datetime as dt,zoneinfo
from lib import ts
SYD=zoneinfo.ZoneInfo("Australia/Sydney")
D=os.path.join(os.environ["TCD"],"days")
FE_PR="CreatesendCom_MonolithMergeChecks_FrontendMergeChecks_"
FE_PR_WIN={"CreatesendCom_StaticAssetValidation","CreatesendCom_MonolithMergeChecks_ValidateJavascriptShared","CreatesendCom_BuildValidateCss","CreatesendCom_BuildJavascriptClosure","CreatesendCom_BuildJavascriptWebpack"}
FE_PKG_WIN={"CreatesendCom_MonolithDeploy_WebPackageJavascript","CreatesendCom_MonolithCanaryDeploy_WebPackageJavascript","CreatesendCom_MonolithHotfix_WebPackageJavascript","CreatesendCom_MonolithHotfix_WebPackageJavascript_Prod"}
def cat(bt):
    if bt.startswith(FE_PR): return "FE PR (Docker)"
    if "FrontendPackage" in bt: return "FE package (Docker shadow)"
    if bt in FE_PR_WIN: return "FE PR (Windows)"
    if bt in FE_PKG_WIN: return "FE package (Windows)"
    return "other"
def load_all():
    B=[]; seen=set()
    for f in sorted(glob.glob(os.path.join(D,"*.json"))):
        for x in json.load(open(f)):
            if x["id"] in seen or not x.get("startDate") or not x.get("finishDate"): continue
            seen.add(x["id"])
            a=(x.get("agent") or {}).get("name") or ""
            if a.startswith("apse2c-bld"): pool="win"
            elif a.startswith("apse2c-dok"): pool="dok"
            else: continue
            B.append(dict(id=x["id"],bt=x["buildTypeId"],pool=pool,agent=a,q=ts(x.get("queuedDate")),s=ts(x["startDate"]),f=ts(x["finishDate"]),cat=cat(x["buildTypeId"])))
    return B
