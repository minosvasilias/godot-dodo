import requests
from git import Repo
import os
import re
import json
import logging

search_url = "https://api.github.com/search/repositories?q=language:gdscript license:mit+pushed:<{before_date}&per_page=100&page={page}&sort=updated"

total_count_3x = 0
total_count_4x = 0
data_3x = []
data_4x = []
repos_3x = []
repos_4x = []


# Load existing data to allow continuing from where we left off
def load_data():
    global data_3x
    global data_4x
    global repos_3x
    global repos_4x
    global total_count_3x
    global total_count_4x
    try:
        with open("dodo_data_3x.json", "r") as f:
            data_3x = json.loads(f.read())
            total_count_3x = len(data_3x)
        with open("dodo_data_4x.json", "r") as f:
            data_4x = json.loads(f.read())
            total_count_4x = len(data_4x)
        with open("dodo_repos_3x.json", "r") as f:
            repos_3x = json.loads(f.read())
        with open("dodo_repos_4x.json", "r") as f:
            repos_4x = json.loads(f.read())
    except FileNotFoundError:
        logging.info("No existing data found, generating new...")


# Retrieve GitHub search results and scrape them
def search(page, before_date, github_token):
    url = search_url.format(page=page, before_date=before_date)
    headers = {"Authorization": "Bearer " + github_token}

    print("Getting search results: " + url)
    response = requests.get(url, headers=headers)
    json = response.json()

    for item in json["items"]:
        try:
            check_repo(item)
        except Exception as e:
            logging.debug(e)


# Check if repo is valid and scrape it
def check_repo(repo):
    # If repo already exists in repo list, skip it
    if repo["full_name"] in repos_3x or repo["full_name"] in repos_4x:
        print("Repo already scraped, skipping: %s" % repo["full_name"])
        return
    # Else, if repo directory does not exist, clone it
    if not os.path.exists("repos/" + repo["full_name"]):
        print("Cloning repo: %s" % repo["full_name"])
        Repo.clone_from(repo["clone_url"], "repos/" + repo["full_name"])
    # For each file in the repo, check if it's called project.godot
    # If it is, open it and check engine version used for project
    version = None
    project_root = None
    for root, dirs, files in os.walk("repos/" + repo["full_name"]):
        for file in files:
            if not project_root and file == "project.godot":
                version = get_version(os.path.join(root, file))
                project_root = root
                break

    # If version is 3 or 4, scrape the project
    print("Godot Version: ", version)
    if version == "3" or version == "4":
        scripts_found = scrape_folder(project_root, version)
        # If any scripts were found, add repo to list of repos
        if scripts_found:
            repos = repos_3x if version == "3" else repos_4x
            repo_file = "dodo_repos_3x.json" if version == "3" else "dodo_repos_4x.json"
            repos.append(repo["full_name"])
            # Save repo list
            with open(repo_file, "w") as f:
                f.write(json.dumps(repos))

    # Remove cloned repo again
    os.system("rm -rf repos/" + repo["full_name"])


# Get Godot version from project.godot file
def get_version(file_path):
    version_string = 'config/features=PackedStringArray("'
    with open(file_path, "r") as f:
        for line in f:
            if version_string in line:
                version = line.replace(
                    version_string, "").strip()[:1]
                return version
    # If no version is found, assume 3.x
    return "3"


# Scrape all scripts in a folder
def scrape_folder(dir, version):
    print("Scraping folder: %s" % dir)
    scripts_found = False
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".gd"):
                scripts_found = True
                scrape_script(os.path.join(root, file), version)

    # After scraping all scripts in folder, save data
    data = data_3x if version == "3" else data_4x
    data_file = "dodo_data_3x.json" if version == "3" else "dodo_data_4x.json"
    with open(data_file, "w") as f:
        f.write(json.dumps(data))

    # Print total counts
    print("3.x count: %s" % total_count_3x)
    print("4.x count: %s" % total_count_4x)
    return scripts_found


# Scrape a single script
def scrape_script(script_path, version):
    with open(script_path, "r") as f:
        functions = f.read().split("func ")
        # Exclude first item, we only care about functions
        for function in functions[1:]:
            # Re-add func stem
            raw_func_string = "func " + function
            func_string = ""
            # Add lines until we reach a line that doesn't start with whitespace
            for line in raw_func_string.splitlines():
                if re.match(r'\s', line) or line.startswith("func "):
                    func_string += line + "\n"
                else:
                    break
            # Add function to data
            add_function(func_string, version)


# Add function to data
def add_function(func_string, version):
    # Increment total count
    global total_count_3x
    global total_count_4x
    if version == "3":
        total_count_3x += 1
    else:
        total_count_4x += 1

    # Add instruction-output pair to data
    # Output remains empty for now, will be populated using label_dataset.py
    function_data = {
        "instruction": "",
        "output": func_string
    }
    data = data_3x if version == "3" else data_4x
    data.append(function_data)


# Load data, and ask user for GitHub API token as well as search date
if __name__ == "__main__":
    load_data()
    github_token = input("Enter your GitHub API token: ")
    before_date = input(
        "Search results before date (YYYY-MM-DD):") + "T00:00:00Z"
    print("Scraping first 1000 repositories found before %s..." % before_date)
    # Max results for GitHub search is 1000, so we need to loop through 10 pages
    for i in range(10):
        search(i, before_date, github_token)
