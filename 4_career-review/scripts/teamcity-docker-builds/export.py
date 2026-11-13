import sys,os,csv,json; sys.path.insert(0,os.path.dirname(__file__))
from lib import *
OUT=sys.argv[1]
keys=["pr_validate_app_win","pr_validate_shared_win","pr_css_win","pr_closure_win","pr_webpack_win",
      "pr_validate_app_dock","pr_validate_shared_dock","pr_css_dock","pr_closure_dock","pr_webpack_dock",
      "deploy_legacy","deploy_docker","deploy_backend_control"]
cols=["series","runtime","build_id","build_number","branch","revision","status","status_text","queued_utc","started_utc","finished_utc","duration_s","queue_s","agent","checkout_s","artifact_publish_s","tests_passed","step_durations_s"]
n=0
with open(os.path.join(OUT,"builds.csv"),"w",newline="") as fh:
    w=csv.writer(fh); w.writerow(cols)
    for k in keys:
        rt="docker" if ("dock" in k) else ("windows" if k!="deploy_backend_control" else "windows-control")
        for x in load(k):
            s=x["stats"]
            steps={kk[len("buildStageDuration:buildStep"):]:round(float(v)/1000,1) for kk,v in s.items() if kk.startswith("buildStageDuration:buildStep")}
            w.writerow([k,rt,x["id"],x.get("number"),x.get("branchName"),x["rev"],x.get("status"),(x.get("statusText") or "").replace("\n"," ")[:200],
                x.get("queuedDate"),x.get("startDate"),x.get("finishDate"),round(x["dur"]) if x["dur"] is not None else "",round(x["queue"]) if x["queue"] is not None else "",
                x["agentname"],round(float(s.get("buildStageDuration:sourcesUpdate",0))/1000,1),round(float(s.get("buildStageDuration:artifactsPublishing",0))/1000,1),s.get("PassedTestCount",""),json.dumps(steps)])
            n+=1
print("rows",n)
