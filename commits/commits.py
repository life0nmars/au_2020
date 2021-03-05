TOKEN = str(input())

import requests

headers = {'Authorization': 'token ' + TOKEN}

login = requests.get('https://api.github.com/user', headers=headers)
print(login.json())
def get_headers():
    return {'Authorization': 'token ' + TOKEN}
def get_user_pr(userName = 'life0nmars', repos = 'python_au', state = 'open'):
  r = requests.get("https://api.github.com/repos/{}/{}/pulls?state={}".format(userName, repos, state), headers = get_headers())
  for elem in r.json():
    commits = requests.get(elem["commits_url"], headers = get_headers()).json()
    if len(commits) > 1:
      return (len(commits))