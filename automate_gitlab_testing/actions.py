# actions.py
import requests
import json
import yaml

from modules.singleton import Singleton
from modules.group import Group
from modules.project import Project
from modules.gitutilities import Gitutilities

import os
import tempfile

def echo(text_to_echo):
    print(text_to_echo)

def extract_id_from_group_or_project_or_user(data):
    data_id = data.get("id",-1)
    return id


def init_config():
     s = Singleton()
     s.init_config()

def print_config(setting_name):
    s = Singleton()
    print(s.config.get_setting(setting_name))



def init_delete_dictionary():
    s = Singleton()
    s.to_delete_dict = {}
    s.to_delete_dict['groups'] = {'ids': []}
    s.to_delete_dict['projects'] = {'ids': []}
def init_group():
    s = Singleton()
    s.group = Group(s.config)
def init_project():
    s = Singleton()
    s.project = Project(s.config)
def init_gitutilities():
    s = Singleton()
    s.gitutilities = Gitutilities(s.config)
def create_group(group_name, parent_id=None):
    s = Singleton()
    group = s.group.create(group_name, parent_id)
    print(json.dumps(group, indent=4))
    group_id = group.get("id",-1)
    s.to_delete_dict['groups']['ids'].append(group_id)
    return group

def create_project_under_group(project_name, group_data):
    s = Singleton()
    group_id = group_data.get("id",-1)
    project = s.project.create_under_group(project_name, group_id)
    print(json.dumps(project, indent=4))
    project_id = project.get("id",-1)
    s.to_delete_dict['projects']['ids'].append(project_id)
    return project

def create_a_file_and_commit_in_project_repo(project_data, filename,file_content,commit_message):
    s = Singleton()
    project_id = project_data.get("id",-1)

    path_with_namespace= s.project.get_path_with_namespace(project_id)
    with tempfile.TemporaryDirectory() as tmpdirname:
        s.gitutilities.clone_project(path_with_namespace,tmpdirname)
        s.gitutilities.add_file_commit_push(tmpdirname, filename, file_content, commit_message)

    return project_data



def save_to_delete():
    s = Singleton()
    with open('to_delete.yaml', 'w') as file:
        yaml.dump(s.to_delete_dict, file)





def fetch_data(url):
    response = requests.get(url)
    return response.json()

def process_data(data, process_type):
    if process_type == "filter":
        return [item for item in data if len(item) > 10]
    return data

def save_results(data, destination):
    with open(destination, 'w') as f:
        json.dump(data, f)
