#! /usr/bin/env python3

from github import Github
from github.GithubException import BadCredentialsException
from sys import exit
import argparse
import os


def write_topics(repo, topiclist, dry_run):
    if not dry_run:
        repo.replace_topics(topiclist)


parser = argparse.ArgumentParser(
    description="Quickly add/remove the 'hacktoberfest' topic to all of your public Github projects"
)
parser.add_argument("action", type=str, help="'add' or 'remove' the topic", choices=["add", "remove"])
parser.add_argument("--organization", "-o", help="Modify topics for an organization, not your personal projects")
parser.add_argument("--dry-run", action="store_true", help="Don't actually modify the topics")
args = parser.parse_args()

try:
    token = os.environ["GITHUB_TOKEN"]
except KeyError:
    print("You need to provide an GitHub Token via the env variable 'GITHUB_TOKEN'")
    exit(1)

g = Github(token)

try:
    print("Getting list of repositories")
    if args.organization:
        repositories = [r for r in g.get_user().get_repos(affiliation = "organization_member", visibility = "public") if r.organization.login == args.organization]
    else:
        repositories = list(g.get_user().get_repos(affiliation = "owner", visibility = "public"))
    user_id = g.get_user().id
except BadCredentialsException:
    print("Token is invalid or has the wrong permissions")
    exit(1)

for repo in repositories:
    print(f"> Checking {repo.full_name}:")

    if repo.private or repo.fork or repo.archived:
        print("Repo is private, a fork or archived. Skipping...")
        continue

    if not args.organization and repo.organization is not None:
        print("Repo belongs to a organization. Skipping...")
        continue

    if not args.organization and repo.owner.id != user_id:
        print("Repo does not belong to you. Skipping...")
        continue

    topic_list = repo.get_topics()

    if "hacktoberfest" in topic_list and args.action == "remove":
        print("Removing topic from repo")
        topic_list.remove("hacktoberfest")
        write_topics(repo, topic_list, args.dry_run)
    elif "hacktoberfest" not in topic_list and args.action == "add":
        print("Adding topic to repo")
        new_topics = topic_list + ["hacktoberfest"]
        write_topics(repo, new_topics, args.dry_run)
    else:
        print("Repo in correct state")
