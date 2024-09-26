from git import Repo
import os
import requests
import tempfile

from modules.config import Config
from modules.project import Project



class Gitutilities_work:
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
        # print(file_path)
        # print(repo.working_dir)
        # print(os.listdir(repo.working_dir))
        repo.index.commit(commit_message)
             
        origin = repo.remote(name='origin')
        origin.push()


    # Example usage within the script
    def modify_project(self,project_id):
        """ Example function to clone, modify, and push changes """
        project_info = requests.get(f"{self.api_url}/projects/{project_id}", headers=self.headers).json()
        project_url = project_info['http_url_to_repo']
        with tempfile.TemporaryDirectory() as tmpdirname:
            repo = self.clone_project(project_url, tmpdirname)
            self.add_file_commit_push(repo, "newfile.txt", "Hello, GitLab!", "Added newfile.txt")



def test_commit_push(path_with_namespace):
    with tempfile.TemporaryDirectory() as tmpdirname:
        os.listdir(tmpdirname)

        username = "Nekogeekaku"
        password = "glpat-eiWMakeeYvoDvSxs_yWK"

        remote = f"https://{username}:{password}@gitlab.com/{path_with_namespace}.git"

        repo = Repo.clone_from(remote, tmpdirname)
        os.listdir(tmpdirname)

        repo = Repo(tmpdirname)
        file_path = os.path.join(repo.working_dir, "newfile.txt")
        with open(file_path, 'w') as file:
            file.write("Hello, GitLab!")
        repo.index.add([file_path])

        # repo.git.add("rel/path/to/dir/with/changes/")
        repo.index.commit("Some commit message")

        repo = Repo(tmpdirname)
        origin = repo.remote(name="origin")
        origin.push()
        print("Git push")



if __name__ == "__main__":
    # Running unit tests
    config = Config()
    gitutilities = Gitutilities(config)
    project = Project(config)
    # git.modify_project(57978313)
    project_id = 58064526

    path_with_namespace= project.get_path_with_namespace(project_id)
    with tempfile.TemporaryDirectory() as tmpdirname:
        os.listdir(tmpdirname)
        repo= gitutilities.clone_project(path_with_namespace,tmpdirname)
        os.listdir(tmpdirname)
        gitutilities.add_file_commit_push(tmpdirname, "newfile.txt", "Hello, GitLab!", "Some commit message")
    
    print("---------------- Git push ---------------------")

    
    # test_commit_push(path_with_namespace)
    # exit
    # print(f"project_url: {project_url}")
    # with tempfile.TemporaryDirectory() as tmpdirname:
    #     os.listdir(tmpdirname)


    #     # full_local_path = "/path/to/repo/"
    #     # username = "your-username"
    #     # password = "your-password"
    #     # remote = f"https://{username}:{password}@github.com/some-account/some-repo.git"

    #     # Repo.clone_from(remote, full_local_path)

    #     # repo = Repo(full_local_path)
    #     # repo.git.add("rel/path/to/dir/with/changes/")
    #     # repo.index.commit("Some commit message")

    #     # repo = Repo(full_local_path)
    #     # origin = repo.remote(name="origin")
    #     # origin.push()
    #     repo = Repo.clone_from(project_url, tmpdirname, env={"GIT_SSL_NO_VERIFY": "1"})
    #     os.listdir(tmpdirname)
    #     file_path = os.path.join(repo.working_dir, "newfile.txt")
    #     with open(file_path, 'w') as file:
    #         file.write("Hello, GitLab!")
    #     repo.index.add([file_path])
    #     repo.index.commit("Added newfile.txt")
    #     origin = repo.remote(name='origin')
    #     origin.push()
    #     print(f"list dir : {os.listdir(tmpdirname)}")

    #     print(f"Repo is : {repo}")
