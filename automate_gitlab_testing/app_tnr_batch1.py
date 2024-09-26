import requests

import os
import tempfile
from git import Repo


api_url = "https://gitlab.com/api/v4"
bearer_token = "glpat-eiWMakeeYvoDvSxs_yWK"
headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json"
}
username='Nekogeekaku'
dns='gitlab.com'
result = {}



print(f"-------------------- Create sub group ----------------------------")
post_data= {"name": "SubGroup", "path": "SubGroup","parent_id": 87926667 }
response = requests.post(f"{api_url}/groups", headers=headers, json=post_data)
print(response)
print(response.json())
group = response.json()
group_id = group.get("id",-1)
print(f"Group Id  : {group_id}")

print(f"-------------------- Create sub sub group ----------------------------")
post_data= {"name": "SubGroup2", "path": "SubGroup2","parent_id": group_id }
response = requests.post(f"{api_url}/groups", headers=headers, json=post_data)
print(response)
group2 = response.json()
group_id2 = group2.get("id",-1)
print(f"Group Id  : {group_id2}")


print(f"-------------------- Create project ----------------------------")
post_data= {"name": "Project", "namespace_id": group_id }
response = requests.post(f"{api_url}/projects", headers=headers, json=post_data)
print(response)
project = response.json()
project_id = project.get("id",-1)
print(f"Project Id  : {project_id}")


print(f"-------------------- Commit a file in project ----------------------------")
file_name= "newfile.txt"
file_content= "Hello, GitLab!"
commit_message= "Some commit message"
project_info = requests.get(f"{api_url}/projects/{project_id}", headers=headers).json()
print(project_info)
path_with_namespace= project_info['path_with_namespace']

with tempfile.TemporaryDirectory() as repo_dir:
    print(f"-------------------- clone ----------------------------")
    remote = f"https://{username}:{bearer_token}@{dns}/{path_with_namespace}.git"
    repo = Repo.clone_from(remote, repo_dir, env={"GIT_SSL_NO_VERIFY": "1"})

    print(f"-------------------- add file ----------------------------")

    repo = Repo(repo_dir)
    file_path = os.path.join(repo.working_dir, file_name)
    with open(file_path, 'w') as file:
        file.write(file_content)
    
    print(f"-------------------- commit ----------------------------")

    repo = Repo(repo_dir)

    repo.index.add([file_path])
    repo.index.commit(commit_message)
    print(f"-------------------- push ----------------------------")

    repo = Repo(repo_dir)
    origin = repo.remote(name='origin')
    origin.push()

    print(f"-------------------- pull ----------------------------")
    repo = Repo(repo_dir)
    origin = repo.remote(name='origin')
    origin.pull()
 

