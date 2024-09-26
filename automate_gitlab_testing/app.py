import requests
import json
import yaml
from modules.config import Config
from modules.group import Group
from modules.project import Project





# def create_project(project_name, namespace_id, with_readme=True):
#     """ Create a new project in GitLab """
#     data = {"name": project_name, "namespace_id": namespace_id}
#     response = requests.post(f"{API_URL}/projects", headers=headers, json=data)
#     if with_readme and response.status_code == 201:
#         project_id = response.json()["id"]
#         init_project_with_readme(project_id, project_name)
#     return response.json()

# def init_project_with_readme(project_id, project_name):
#     """ Initialize a project with a README file """
#     import git
#     import tempfile
#     import os
#     repo_url = f"git@gitlab.com:{project_name}.git"
#     with tempfile.TemporaryDirectory() as tmpdirname:
#         repo = git.Repo.init(os.path.join(tmpdirname, project_name))
#         origin = repo.create_remote('origin', repo_url)
#         with open(os.path.join(tmpdirname, project_name, 'README.md'), 'w') as f:
#             f.write(f"# {project_name}\nInitial README file")
#         repo.index.add(['README.md'])
#         repo.index.commit("Initial commit with README")
#         origin.push(refspec='master:master')




def main():
    # Initialize configuration
    config = Config()
    group = Group(config)
    project = Project(config)
    to_delete_dict = {}
    to_delete_dict['groups'] = {'ids': []}
    to_delete_dict['projects'] = {'ids': []}

    # response_json = project.list()
    # print(json.dumps(response_json, indent=4))
    # response_json = group.list()
    # print(json.dumps(response_json, indent=4))
    print("-------------------- Creation of groups ----------------------------")

    # Create root group : Not possible in gitlab.com
    root_group = group.create("MyRootGroup")
    print(json.dumps(root_group, indent=4))
    # Example usage
    # Create a subgroup
    root_id = 75764245 #in gitlab.com
    # root_id=root_group["id"]
    # to_delete_dict['groups']['ids'].append(root_id)
    subgroup = group.create("SubGroup", parent_id=root_id)
    print(json.dumps(subgroup, indent=4))
    subgroup_id = subgroup["id"]
    to_delete_dict['groups']['ids'].append(subgroup_id)
    print(f"Subgroup ID to delete : {subgroup_id}")


    print("-------------------- Creation of project ----------------------------")


    project_data = project.create_under_group("first project",subgroup_id)
    project_data_id = project_data["id"]
    print(json.dumps(project_data, indent=4))
    to_delete_dict['projects']['ids'].append(project_data_id)

    print(f"project ID to delete : {project_data_id}")

    # project_with_readme = create_project("ProjectWithREADME", subgroup["id"], with_readme=True)
    # project_without_readme = create_project("ProjectWithoutREADME", subgroup["id"], with_readme=False)

    with open('to_delete.yaml', 'w') as file:
        yaml.dump(to_delete_dict, file)

    # print(project.delete(project_data_id))
    # print(group.delete(subgroup_id))
    # print(group.delete(root_id))

if __name__ == "__main__":
    main()
