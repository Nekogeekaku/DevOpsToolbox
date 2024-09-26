from git import Repo
import os


from modules.config import Config
from modules.project import Project


class Gitutilities:
    def __init__(self, config):
        self.config = config
        self.api_url = config.get_setting('api_url')
        self.bearer_token = config.get_setting('bearer_token')
        self.username = config.get_setting('username')
        self.base_name = config.get_setting('base_name')
        self.headers = {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json"
        }


    def clone_project(self,path_with_namespace, local_dir):
        """ Clone a GitLab project to a local directory """

        remote = f"https://{self.username}:{self.bearer_token}@{self.base_name}/{path_with_namespace}.git"

        repo = Repo.clone_from(remote, local_dir, env={"GIT_SSL_NO_VERIFY": "1"})

        return repo

    def add_file_commit_push(self,repo_dir, file_name, content, commit_message):
        """ Add a new file, commit, and push to a GitLab project """
        repo = Repo(repo_dir)
        file_path = os.path.join(repo.working_dir, file_name)
        with open(file_path, 'w') as file:
            file.write(content)
        
        repo.index.add([file_path])
        repo.index.commit(commit_message)
        
        repo = Repo(repo_dir)
        origin = repo.remote(name='origin')
        origin.push()
        return repo





