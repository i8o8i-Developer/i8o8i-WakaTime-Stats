# I8o8i Waka Time Stats

<p align="center">
   Are You An Early 🐤 Or A Night 🦉?
   <br/>
   When Are You Most Productive During The Day?
   <br/>
   What Are The Languages That You Code In?
   <br/>
   Let's Check It Out In Your Profile's README!
</p>

<p align="center">
    <a href="https://github.com/i8o8i-Developer/i8o8i-WakaTime-Stats/issues">Report Bug</a>
     
    <a href="https://github.com/i8o8i-Developer/i8o8i-WakaTime-Stats/issues">Request Feature</a>
  </p>

## Prep Work

1. You Need To Update The Markdown File(`.md`) With 2 Comments. You Can Refer [Here](#update-your-readme) For Updating It.
2. You'll Need A WakaTime API Key. You Can Get That From Your WakaTime Account Settings
    - You Can Refer [Here](#new-to-wakatime), If You're New To WakaTime.
3. You'll Need A GitHub API Token With `repo` And `user` Scope From [Here](https://github.com/settings/tokens) If You're Running The Action To Get Commit Metrics.
   - You Can Use [This](#profile-repository) Example To Work It Out.
> [!NOTE]
> Enabling The `repo` Scope Seems **DANGEROUS**, \
> But This GitHub Action Only Accesses Your Commit Timestamps And The Number Of Lines Of Code Added Or Deleted In Repositories That You Contributed To.
4. You Need To Save The WakaTime API Key And The GitHub API Token In The Repository Secrets. You Can Find That In The Settings Of Your Repository. \
  Be Sure To Save Those As The Following:
    - WakaTime API Key As `WAKATIME_API_KEY=<Your WakaTime API Key>`
    - GitHub Personal Access Token (PAT) As `GH_TOKEN=<Your GitHub Access Token>`
5. You Can Enable And Disable Feature Flags Based On Your Requirements.

This GitHub Action Can Be Set To Run At Any Time You Want Using `cron`. See [Crontab.guru](https://crontab.guru/) And [This](https://crontab.cronhub.io/) Website To Generate `cron` Expressions.

## Update Your Readme

Add A Comment To Your `README.md` Like This:

```md
<!--START_SECTION:waka-->
<!--END_SECTION:waka-->
```

`waka` Can Be Replaced By Any String Specified In The `SECTION_NAME` Flag As Per [The Available Flags Section](#flags-available).

These Lines Will Be Our Entry-Points For The Dev Metrics.

## New To WakaTime

WakaTime Gives You An Idea Of The Time You Really Spent On Coding. This Helps You Boost Your Productivity And Competitive Edge.

- Head Over To <https://wakatime.com> And Create An Account.
- Get Your WakaTime API Key From Your [Account Settings In WakaTime](https://wakatime.com/settings/account).
- Install The [WakaTime Plugin](https://wakatime.com/plugins) In Your Favourite Editor / IDE.
- Paste In Your API Key To Start The Analysis.

### Profile Repository

You'll Need To Get A [GitHub Access Token](https://docs.github.com/en/actions/configuring-and-managing-workflows/authenticating-with-the-github_token) With A `repo` And `user` Scope And Save It In The Repo Secrets `GH_TOKEN = <Your GitHub Access Token>`

Here Is A Sample Workflow File For Running It:

```yml
name: Waka Readme

on:
  schedule:
    # Runs At 12am IST
    - cron: '30 18 * * *'
  workflow_dispatch:
jobs:
  update-readme:
    name: Update Readme With Metrics
    runs-on: ubuntu-latest
    steps:
      - uses: i8o8i-Developer/i8o8i-WakaTime-Stats@master
        with:
          WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
          GH_TOKEN: ${{ secrets.GH_TOKEN }}
```
- Now You Can Commit And Wait For It To Run Automatically, Or You Can Also Trigger To Run It To See The Result Now. Just Go To The `Actions` In Your Repo, Select Your `Profile Readme Development Stats` Workflow And Click `Run workflow`. Now Wait For A Minute Or Two And You Will See Your Changes.

## Extras

If You Want To Add The Other Info To Your Stats, You Can Add Multiple `FLAGS` In Your Workflow File. By Default All Flags Are Enabled (Except The Lines Of Code Flag Due To The Heavy Operation Performed)

```yml
- uses: i8o8i-Developer/i8o8i-WakaTime-Stats@master
  with:
      WAKATIME_API_KEY: ${{ secrets.WAKATIME_API_KEY }}
      GH_TOKEN: ${{ secrets.GH_TOKEN }}
      SHOW_OS: "False"
      SHOW_PROJECTS: "False"
```

### Flags Available

---

`LOCALE`  This Flag Can Be Used To Show Stats In Your Language. Default Is English. Locale [Short Hand](https://saimana.com/list-of-country-locale-code/) To Be Passed In The Flag Variable. Example Of The Final Result Can Be Found [Here](https://github.com/anmol098/anmol098/blob/master/Readme-fr.md)

The `SECTION_NAME` Flag Can Be Set To Any String, And Will Be The Name Of The Section To Replace In The README.

The `COMMIT_BY_ME` Flag Can Be Set To `True` To Commit The Code Using Your Name And Email.

The `COMMIT_MESSAGE` Flag Can Be Set For The Commit Message. The Default Is "Updated With Dev Metrics"

The `COMMIT_USERNAME` Flag Can Be Set As A Username To Commit The Code. The Default Is "readme-bot".

The `COMMIT_EMAIL` Flag Can Be Set To An Email To Commit The Code. The Default Is "41898282+github-actions[bot]@users.noreply.github.com".

The `SHOW_UPDATED_DATE` Flag Can Be Set To `True` To Show The Updated Date In End Of Paragraph.

The `UPDATED_DATE_FORMAT` Flag Can Be Set To Put The Updated Date Into A Format. The Default Is `"%d/%m/%Y %H:%M:%S"`.

The `SHOW_LINES_OF_CODE` Flag Can Be Set To `True` To Show The Number Of Lines Of Code Writen Till Date.

![Lines Of Code](https://img.shields.io/badge/From%20Hello%20World%20I've%20written-1.3%20million%20Lines%20of%20code-blue)

The `SHOW_TOTAL_CODE_TIME` Flag Can Be Set To `False` To Hide *Code Time*.

![Code Time](http://img.shields.io/badge/Code%20Time-1%2C438%20hrs%2054%20mins-blue)

The `SHOW_PROFILE_VIEWS` Flag Can Be Set To `False` To Hide **Profile Views**

![Profile Views](http://img.shields.io/badge/Profile%20Views-2189-blue)

The `SHOW_COMMIT` Flag Can Be Set To `False` To Hide The Commit Stats.

**I Am An Early Birds** 
```text
🌞 Morning    95 commits     ███████░░░░░░░░░░░░░░░░░░   30.55% 
🌆 Daytime    78 commits     ██████░░░░░░░░░░░░░░░░░░░   25.08% 
🌃 Evening    112 commits    █████████░░░░░░░░░░░░░░░░   36.01% 
🌙 Night      26 commits     ██░░░░░░░░░░░░░░░░░░░░░░░   8.36%

```

The `SHOW_DAYS_OF_WEEK` Flag Can Be Set To `False` To Hide The Commits Made On The Different Days Of The Week.

📅 **I Am Most Productive On Sundays** 

```text
Monday       50 commits     ███░░░░░░░░░░░░░░░░░░░░░░   13.19% 
Tuesday      85 commits     █████░░░░░░░░░░░░░░░░░░░░   22.43% 
Wednesday    56 commits     ███░░░░░░░░░░░░░░░░░░░░░░   14.78% 
Thursday     44 commits     ███░░░░░░░░░░░░░░░░░░░░░░   11.61% 
Friday       28 commits     █░░░░░░░░░░░░░░░░░░░░░░░░   7.39% 
Saturday     30 commits     ██░░░░░░░░░░░░░░░░░░░░░░░   7.92% 
Sunday       86 commits     █████░░░░░░░░░░░░░░░░░░░░   22.69%

```

The `SHOW_LANGUAGE` Flag Can Be Set To `False` To Hide The Programming Languages You Use.

```text
💬 Languages:
JavaScript               5 hrs 26 mins       ███████████████░░░░░░░░░░   61.97%
PHP                      1 hr 35 mins        ████░░░░░░░░░░░░░░░░░░░░░   18.07%
Markdown                 1 hr 9 mins         ███░░░░░░░░░░░░░░░░░░░░░░   13.3%
Python                   22 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   4.32%
XML                      8 mins              ░░░░░░░░░░░░░░░░░░░░░░░░░   1.62%
```


The `SHOW_OS` Flag Can Be Set To `False` To Hide Your OS Details.

```text
💻 Operating Systems:
Windows                  8 hrs 46 mins       █████████████████████████   100.0%
```

The `SHOW_PROJECTS` Flag Can Be Set To `False` To Hide The Projects Worked On.

```text
🐱‍💻 Projects:
ctx_connector            4 hrs 3 mins        ███████████░░░░░░░░░░░░░░   46.33%
NetSuite-Connector       1 hr 31 mins        ████░░░░░░░░░░░░░░░░░░░░░   17.29%
mango-web-master         1 hr 12 mins        ███░░░░░░░░░░░░░░░░░░░░░░   13.77%
cable                    54 mins             ██░░░░░░░░░░░░░░░░░░░░░░░   10.41%
denAPI                   40 mins             ██░░░░░░░░░░░░░░░░░░░░░░░   7.66%
```

The `SHOW_TIMEZONE` Flag Can Be Set To `False` To Hide The Time Zone You Are In.

```text
⌚︎ Timezone: Asia/Calcutta
```

The `SHOW_EDITORS` Flag Can Be Set To `False` To Hide The List Of Code Editors/IDEs Used.

```text
🔥 Editors:
WebStorm                 6 hrs 47 mins       ███████████████████░░░░░░   77.43%
PhpStorm                 1 hr 35 mins        ████░░░░░░░░░░░░░░░░░░░░░   18.07%
PyCharm                  23 mins             █░░░░░░░░░░░░░░░░░░░░░░░░   4.49%
```
```

The `SHOW_LANGUAGE_PER_REPO` Flag Can Be Set To `False` To Hide The Number Of Repositories In Different Programming Languages And Frameworks.

**I Mostly Code In Vue** 

```text
Vue          8 repos        ██████░░░░░░░░░░░░░░░░░░░   25.0% 
Java         6 repos        ████░░░░░░░░░░░░░░░░░░░░░   18.75% 
JavaScript   6 repos        ████░░░░░░░░░░░░░░░░░░░░░   18.75% 
PHP          3 repos        ██░░░░░░░░░░░░░░░░░░░░░░░   9.38% 
Python       2 repos        █░░░░░░░░░░░░░░░░░░░░░░░░   6.25% 
Dart         2 repos        █░░░░░░░░░░░░░░░░░░░░░░░░   6.25% 
CSS          2 repos        █░░░░░░░░░░░░░░░░░░░░░░░░   6.25%

```

The `SHOW_SHORT_INFO` Flag Can Be Set To `False` To Hide The Short Fun Fact Info Of A User.
> [!NOTE]
> This Section Requires A Personal Access Token (PAT) With The `user` Scope, Otherwise The Data Shown Here Will Be Incorrect.

**🐱 {Username} GitHub Data** 

> 🏆 Contributions Made In The Year: 433 In 2020
 > 
> 📦 Used In GitHub's Storage: 292.3 kB
 > 
> 💼 i8o8i Solutions Is Open To Hire
 > 
> 📜 Public Repositories: 25
 > 
> 🔑 Private Repositories: 15 

The `SHOW_LOC_CHART` Flag Can Be Set To `False` To Hide The Lines Of Code Written In Different Quarters Of Different Years.

The `IGNORED_REPOS` Flag Can Be Set To `"waka-readme-stats, my-first-repo"` (Just An Example) To Ignore Some Repos You Dont Want To Be Counted.

The `SYMBOL_VERSION` Flag Can Be Set For The Symbol For The Progress Bar (Default: `1`).
| Version | Done Block | Empty Block |
|-------- | ---------- | ----------- |
|    1    |      █     |       ░     |
|    2    |      ⣿     |       ⣀     |
|    3    |      ⬛    |       ⬜    |

The `DEBUG_LOGGING` Flag Can Be Set To Increase The GitHub Action's Output Verbosity, By Default Equals Internal Runner Debug Property



## ❤️ Support The Project

This Project Is Maintained By I8o8i Solutions. We Open-Source Our Tools To Help Developers Boost Productivity And Showcase Their Work.

If You Find This Useful, Here Are Ways To Support Us:

- **Star The Repo**: Show Your Appreciation By Starring This Repository On GitHub.
- **Share It**: Spread The Word About I8o8iWakaTimeStats With Your Network.
- **Contribute**: Submit Issues, Pull Requests, Or Suggestions To Improve The Project.
- **Follow Us**: Keep Up With Our Latest Projects And Updates.

Your Support Helps Us Continue Building Awesome Tools For The Developer Community!

Thanks! 💕

---

# Contributing

Contributions Are Welcome! Please Share Any Features, And Add Unit Tests! Use The Pull Request And Issue Systems To Contribute.


Made With ❤️ And Python 🐍.

## License

This Project Is Licensed Under The MIT License. See The [LICENSE](LICENSE) File For Details.

# Inspired From

> [Awesome Pinned Gists](https://github.com/matchai/awesome-pinned-gists) <br/>
> [anmol098/waka-readme-stats](https://github.com/anmol098/waka-readme-stats)

### This Project Needs A **Star**  From You .


## Stargazers Over Time

[![Stargazers over time](https://starchart.cc/i8o8i-Developer/i8o8i-WakaTime-Stats.svg)](https://starchart.cc/i8o8i-Developer/i8o8i-WakaTime-Stats)

Powered By I8o8i Workstation !!