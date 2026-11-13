import json, subprocess, sys, os
OUT = sys.argv[1]
configs = {
 "pr_validate_app_win": "CreatesendCom_StaticAssetValidation",
 "pr_validate_shared_win": "CreatesendCom_MonolithMergeChecks_ValidateJavascriptShared",
 "pr_closure_win": "CreatesendCom_BuildJavascriptClosure",
 "pr_webpack_win": "CreatesendCom_BuildJavascriptWebpack",
 "pr_css_win": "CreatesendCom_BuildValidateCss",
 "pr_validate_app_dock": "CreatesendCom_MonolithMergeChecks_FrontendMergeChecks_ValidateJavascriptApp",
 "pr_validate_shared_dock": "CreatesendCom_MonolithMergeChecks_FrontendMergeChecks_ValidateJavascriptShared",
 "pr_closure_dock": "CreatesendCom_MonolithMergeChecks_FrontendMergeChecks_BuildJavascriptClosure",
 "pr_webpack_dock": "CreatesendCom_MonolithMergeChecks_FrontendMergeChecks_BuildJavascriptWebpack",
 "pr_css_dock": "CreatesendCom_MonolithMergeChecks_FrontendMergeChecks_BuildValidateCss",
}
fields = "build(id,number,status,state,branchName,startDate,finishDate,queuedDate,agent(name,pool(name)),triggered(type,user(username)),statusText,personal,revisions(revision(version)))"
for k, bt in configs.items():
    loc = f"buildType:{bt},defaultFilter:false,branch:default:any,personal:any,count:5000"
    url = f"/app/rest/builds?locator={loc}&fields={fields}"
    r = subprocess.run(["teamcity","api",url], capture_output=True, text=True)
    if r.returncode != 0:
        print(k, "ERR", r.stderr[:300]); continue
    builds = json.loads(r.stdout).get("build", [])
    json.dump(builds, open(os.path.join(OUT, k + ".json"), "w"), indent=1)
    ds=sorted(x.get("startDate","") for x in builds if x.get("startDate"))
    print(k, len(builds), ds[0][:13] if ds else None, ds[-1][:13] if ds else None)
