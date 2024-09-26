import json
import requests
from modules.singleton import Singleton


class Action:
    #def __init(self):
        # print("Plugin create_group constructor")
        # This is called when the plugin is loaded
    def name(self):
        return "create_project_under_group"
    def definition(self):
        print("Give a definition of create_project_under_group")
    def run(self, data):
        s = Singleton()
        api_url = s.get_setting('API_URL')
        bearer_token = s.get_setting('BEARER_TOKEN')
        headers = {
            "Authorization": f"Bearer {bearer_token}",
            "Content-Type": "application/json"
        }
        post_data = {}
        for k, v in data.items():
            print(k,v)
            post_data[k] =  s.interpret_param(v)
        response = requests.post(f"{api_url}/projects", headers=headers, json=post_data)
        project = response.json()
        project_id = project.get("id",-1)
        s.debug_log(f"Project Id  : {project_id}")
        result = {}
        result["project"] = project
        return result

    def mockup(self, data):
        s = Singleton()
        # s.debug_log(data)
        # get all params
        post_data = {}
        for k, v in data.items():
            # print(k,v)
            post_data[k] =  s.interpret_param(v)
        s.debug_log(f"post_data: {post_data}")


        project = {'id': 1, 'name': 'Project'}
        project_id = project.get("id",-1)
        s.debug_log(f"Project Id  : {project_id}")
        result = {}
        result["project"] = project
        return result

