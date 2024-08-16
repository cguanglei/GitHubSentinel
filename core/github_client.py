import requests

class GitHubClient:
    def __init__(self, token):
        self.token = token
    
    def get_latest_updates(self, repo_name):
        # 通过 GitHub API 获取仓库最新动态
        headers = {'Authorization': f'token {self.token}'}
        response = requests.get(f'https://api.github.com/repos/{repo_name}/events', headers=headers)
        return response.json()
