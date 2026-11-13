#!/usr/bin/env bash
# Pulls every build run on each Docker-pool agent since 20 Oct 2026 into <dir>/pool_<agent>.json.
# a4.py (pool utilisation) and a5.py (which workloads grew) read these files.
set -euo pipefail
dir="${1:?usage: pull_pool.sh <dir>}"
for agent in $(teamcity pool view 10 | awk '/-dok-/{print $2}'); do
  teamcity api "/app/rest/builds?locator=agent:(name:${agent}),defaultFilter:false,branch:default:any,personal:any,sinceDate:20261020T000000%2B0000,count:20000&fields=build(id,buildTypeId,startDate,finishDate,agent(name))" \
    > "${dir}/pool_${agent}.json"
done
