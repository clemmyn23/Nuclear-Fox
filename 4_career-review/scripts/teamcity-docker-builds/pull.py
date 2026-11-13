import json, subprocess, sys, os
OUT = sys.argv[1]
configs = {
 "deploy_legacy": "CreatesendCom_MonolithDeploy_WebPackageJavascript",
 "deploy_docker": "CreatesendCom_MonolithDeploy_FrontendPackageDocker_WebPackageJavascript",
 "canary_legacy": "CreatesendCom_MonolithCanaryDeploy_WebPackageJavascript",
 "canary_docker": "CreatesendCom_MonolithCanaryDeploy_FrontendPackage_WebPackageJavascript",
 "hotfix_legacy": "CreatesendCom_MonolithHotfix_WebPackageJavascript",
 "hotfix_docker": "CreatesendCom_MonolithHotfix_FrontendPackage_WebPackageJavascript",
 "hotfixprod_legacy": "CreatesendCom_MonolithHotfix_WebPackageJavascript_Prod",
 "deploy_backend_control": "CreatesendCom_MonolithDeploy_WebPackageBackend",
}
fields = "build(id,number,status,state,branchName,startDate,finishDate,queuedDate,agent(name,pool(name)),triggered(type,user(username)),statusText,personal,canceledInfo(text),revisions(revision(version)))"
for k, bt in configs.items():
    loc = f"buildType:{bt},defaultFilter:false,branch:default:any,sinceDate:20260601T000000%2B0000,count:2000"
    url = f"/app/rest/builds?locator={loc}&fields={fields}"
    r = subprocess.run(["teamcity","api",url], capture_output=True, text=True)
    if r.returncode != 0:
        print(k, "ERR", r.stderr[:300]); continue
    d = json.loads(r.stdout)
    builds = d.get("build", [])
    json.dump(builds, open(os.path.join(OUT, k + ".json"), "w"), indent=1)
    print(k, len(builds))
