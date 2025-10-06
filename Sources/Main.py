from asyncio import run
from datetime import datetime
from typing import Dict
from urllib.parse import quote

from humanize import intword, naturalsize, intcomma

from ManagerDebug import InitDebugManager, DebugManager as DBM
from ManagerGithub import InitGithubManager, GitHubManager as GHM
from ManagerDownload import InitDownloadManager, DownloadManager as DM
from ManagerEnvironment import EnvironmentManager as EM

from GraphicsChartDrawer import CreateLocGraph, GRAPH_PATH
from YearlyCommitCalculater import CalculateCommitData
from GraphicsListFormatter import MakeList, MakeCommitDayTimeList, MakeLanguagePerRepoList


async def GetWakaTimeStats(repositories: Dict, commit_dates: Dict) -> str:
    DBM.i("Adding Short WakaTime Stats...")
    stats = ""

    data = await DM.GetRemoteJson("waka_latest")
    if not data:
        DBM.p("WakaTime Data Unavailable!")
        return stats

    if EM.SHOW_COMMIT or EM.SHOW_DAYS_OF_WEEK:
        DBM.i("Adding User Commit Day/Time Info...")
        stats += f"{await MakeCommitDayTimeList(data['data']['timezone'], repositories, commit_dates)}\n\n"

    if EM.SHOW_TIMEZONE or EM.SHOW_LANGUAGE or EM.SHOW_EDITORS or EM.SHOW_PROJECTS or EM.SHOW_OS:
        no_activity = "No Activity Tracked This Week"
        stats += "📊 **This Week I Spent Time On** \n\n```text\n"

        if EM.SHOW_TIMEZONE:
            stats += f"🕑︎ Timezone: {data['data']['timezone']}\n\n"
        if EM.SHOW_LANGUAGE:
            stats += f"💬 Languages:\n{MakeList(data['data']['languages']) or no_activity}\n\n"
        if EM.SHOW_EDITORS:
            stats += f"🔥 Editors:\n{MakeList(data['data']['editors']) or no_activity}\n\n"
        if EM.SHOW_PROJECTS:
            stats += f"🐱‍💻 Projects:\n{MakeList(data['data']['projects']) or no_activity}\n\n"
        if EM.SHOW_OS:
            stats += f"💻 Operating System:\n{MakeList(data['data']['operating_systems']) or no_activity}\n\n"

        stats = stats.rstrip() + "\n```\n\n"

    DBM.g("WakaTime Stats Added!")
    return stats


async def GetShortGithubInfo() -> str:
    DBM.i("Adding Short GitHub Info...")
    stats = f"**🐱 {GHM.USER.login} GitHub Data** \n\n"

    if GHM.USER.disk_usage is None:
        stats += "> 📦 Used In GitHub's Storage: ? \n > \n"
        DBM.p("Missing GitHub PAT With User Scope.")
    else:
        stats += f"> 📦 Used In GitHub's Storage: {naturalsize(GHM.USER.disk_usage)} \n > \n"

    data = await DM.GetRemoteJson("github_stats")
    if data and data["years"]:
        year_info = data["years"][0]
        stats += f"> 🏆 Contributions Made In The Year: {intcomma(year_info['total'])} in {year_info['year']} \n > \n"

    hire_status = "i8o8i Solutions Is Open to Hire" if GHM.USER.hireable else "i8o8i Solutions Is Not Open to Hire"
    stats += f"> {'💼' if GHM.USER.hireable else '🚫'} {hire_status} \n > \n"
    stats += f"> 📜 Public Repositories: {GHM.USER.public_repos} \n > \n"
    private = GHM.USER.owned_private_repos or 0
    stats += f"> 🔑 Private Repositories: {private} \n > \n"

    DBM.g("Short GitHub Info Added!")
    return stats


async def CollectUserRepositories() -> Dict:
    DBM.i("Getting User Repositories List...")
    repos = await DM.GetRemoteGraphql("user_repository_list", username=GHM.USER.login, id=GHM.USER.node_id)
    repo_names = [repo["name"] for repo in repos]
    contributed = await DM.GetRemoteGraphql("repos_contributed_to", username=GHM.USER.login)
    contributed_clean = [repo for repo in contributed if repo and repo["name"] not in repo_names and not repo["isFork"]]
    DBM.g("Collected All User And Contributed Repositories.")
    return repos + contributed_clean


async def GetStats() -> str:
    DBM.i("Collecting Stats For README...")
    stats = ""
    repositories = await CollectUserRepositories()

    if EM.SHOW_LINES_OF_CODE or EM.SHOW_LOC_CHART or EM.SHOW_COMMIT or EM.SHOW_DAYS_OF_WEEK:
        yearly_data, commit_data = await CalculateCommitData(repositories)
    else:
        yearly_data, commit_data = {}, {}
        DBM.w("Skipped Yearly Data Calculation.")

    if EM.SHOW_TOTAL_CODE_TIME:
        data = await DM.GetRemoteJson("waka_all")
        if data:
            stats += f"![Code Time](http://img.shields.io/badge/{quote('Code Time (Team)')}-{quote(data['data']['text'])}-blue)\n\n"

    if EM.SHOW_PROFILE_VIEWS:
        views = GHM.REMOTE.get_views_traffic(per="week").count
        stats += f"![Profile Views](http://img.shields.io/badge/Profile%20Views%20(Team)-{views}-blue)\n\n"

    if EM.SHOW_LINES_OF_CODE:
        total_loc = sum(yearly_data[y][q][d]["add"] for y in yearly_data for q in yearly_data[y] for d in yearly_data[y][q])
        data_str = f"{intword(total_loc)} Lines of code"
        stats += f"![Lines of code](https://img.shields.io/badge/From%20Hello%20World%20I%20Have%20Written-{quote(data_str)}-blue)\n\n"

    if EM.SHOW_SHORT_INFO:
        stats += await GetShortGithubInfo()

    stats += await GetWakaTimeStats(repositories, commit_data)

    if EM.SHOW_LANGUAGE_PER_REPO:
        stats += f"{MakeLanguagePerRepoList(repositories)}\n\n"

    if EM.SHOW_LOC_CHART:
        await CreateLocGraph(yearly_data, GRAPH_PATH)
        stats += f"**Timeline**\n\n{GHM.UpdateChart('Lines of Code', GRAPH_PATH)}"

    if EM.SHOW_UPDATED_DATE:
        stats += f"\n Last Updated On {datetime.now().strftime(EM.UPDATED_DATE_FORMAT)} UTC"

    DBM.g("Stats Collected.")
    return stats


async def Main():
    InitGithubManager()
    await InitDownloadManager(GHM.USER.login)
    DBM.i("Managers Initialized.")
    stats = await GetStats()

    if not EM.DEBUG_RUN:
        GHM.UpdateReadme(stats)
        GHM.CommitUpdate()
    else:
        GHM.SetGithubOutput(stats)

    await DM.CloseRemoteResources()


if __name__ == "__main__":
    InitDebugManager()
    start_time = datetime.now()
    DBM.g("Program Execution Started At $date.", date=start_time)
    run(Main())
    end_time = datetime.now()
    DBM.g("Program Execution Finished At $date.", date=end_time)
    DBM.p("Program Finished In $time.", time=end_time - start_time)
