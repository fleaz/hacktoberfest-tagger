# hacktoberfest-tagger
Quickly add/remove the 'hacktoberfest' topic to all your public repositories
![Screenshot of the programm output](screenshot.png)

## Motivation
Due to too much SPAM, participation in the Hacktoberfest is now opt-in. That means that you (as a maintainer) have to
add the "hacktoberfest" topic to your repositories before the PRs will count for contributors.  Because most private
accounts will probably not be affected this much by spam, I created this tool to quickly add/remove the topic to all
your public repositories on GitHub.

## Prerequisites
First you need to go to the [Github developer settings](https://github.com/settings/tokens) and create a personal
access token with the `public_repo` permission. The benefit of this in contrast to using your username&password is that
the script only has the permissions it needs, and it also works when you have 2FA enabled (which you definitely should! ;)
)

Provide this token to the script, for example by 

    export GITHUB_TOKEN="copy-your-token-here"
    
Then you need to install the "PyGithub" library. With pipenv installed you can run `pipenv install` in the repository
folder to create a new virtual environment with all dependencies. If you want to use **pip** you can run `pip install -r requirements.txt`.

## Usage
```
run.py [-h] [--organization ORGANIZATION] [--dry-run] {add,remove}

Quickly add/remove the 'hacktoberfest' topic to all of your public Github
projects

positional arguments:
  {add,remove}          'add' or 'remove' the topic

optional arguments:
  -h, --help            show this help message and exit
  --organization ORGANIZATION, -o ORGANIZATION
                        Modify topics for an organization, not your personal
                        projects
  --dry-run             Don't actually modify the topics
```
