import yaml
import requests
from modules.singleton import Singleton
import os
import tempfile
from git import Repo

class Action:
    #def __init(self):
        # print("Plugin create_group constructor")
        # This is called when the plugin is loaded
    def name(self):
        return "pull_project"
    def definition(self):
        print("Give a definition of pull_project")
    def run(self, data):
        s = Singleton()
        self.api_url = s.get_setting('API_URL')
        self.bearer_token = s.get_setting('BEARER_TOKEN')
        self.headers = {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json"
        }
        self.username=s.get_setting('USERNAME')
        self.dns=s.get_setting('DNS')

        post_data = {}
        for k, v in data.items():
            print(k,v)
            post_data[k] =  s.interpret_param(v)


        project_id = post_data.get("project_id",-1)
        project_info = requests.get(f"{self.api_url}/projects/{project_id}", headers=self.headers).json()
        path_with_namespace= project_info['path_with_namespace']

        with tempfile.TemporaryDirectory() as tmpdirname:

            self.clone_project(path_with_namespace,tmpdirname)
            self.pull(tmpdirname)

    def pull(self,repo_dir):
        repo = Repo(repo_dir)
        origin = repo.remote(name='origin')
        origin.pull()
 
    def clone_project(self,path_with_namespace, local_dir):
        """ Clone a GitLab project to a local directory """

        remote = f"https://{self.username}:{self.bearer_token}@{self.dns}/{path_with_namespace}.git"

        repo = Repo.clone_from(remote, local_dir, env={"GIT_SSL_NO_VERIFY": "1"})

        return repo


    def mockup(self, data):
        s = Singleton()
        self.api_url = s.get_setting('API_URL')
        self.bearer_token = s.get_setting('BEARER_TOKEN')
        self.headers = {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json"
        }
        self.username=s.get_setting('USERNAME')
        self.dns=s.get_setting('DNS')

        post_data = {}
        for k, v in data.items():
            print(k,v)
            post_data[k] =  s.interpret_param(v)


        project_id = post_data.get("id",-1)
        filename = post_data.get("filename",-1)
        file_content = post_data.get("file_content",-1)
        commit_message = post_data.get("commit_message",-1)
        project_info = requests.get(f"{self.api_url}/projects/{project_id}", headers=self.headers).json()
        path_with_namespace= project_info['path_with_namespace']

        with tempfile.TemporaryDirectory() as tmpdirname:
            self.clone_project(path_with_namespace,tmpdirname)
            self.pull(tmpdirname)

        
