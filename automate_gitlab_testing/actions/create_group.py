import json
import requests
from modules.singleton import Singleton


class Action:
    #def __init(self):
        # print("Plugin create_group constructor")
        # This is called when the plugin is loaded
    def name(self):
        return "create_group"
    def definition(self):
        print("Give a definition of create group")
    def run(self, data):
        s = Singleton()
        api_url = s.get_setting('API_URL')
        bearer_token = s.get_setting('BEARER_TOKEN')
        headers = {
            "Authorization": f"Bearer {bearer_token}",
            "Content-Type": "application/json"
        }
        # post_data = {"name": data["group_name"], "path": data["group_name"].lower()}
        # if data["parent_id"]:
        #     post_data["parent_id"] = data["parent_id"]
        post_data = {}
        for k, v in data.items():
            print(k,v)
            post_data[k] =  s.interpret_param(v)
        # s.debug_log(f"post_data: {post_data}")

        # print(f" url : {api_url}/groups")
        # print(f" headers : {headers}")
        # print(f" post_data : {post_data}")
        response = requests.post(f"{api_url}/groups", headers=headers, json=post_data)
        # print(response)
        # print(response.json())
        group = response.json()
        # print(json.dumps(group, indent=4))
        group_id = group.get("id",-1)
        s.debug_log(f"Group Id  : {group_id}")
        result = {}
        result["group"] = group
        return result

    def mockup(self, data):
        s = Singleton()
        # s.debug_log(data)
        # get all params
        post_data = {}
        for k, v in data.items():
            # print(k,v)
            post_data[k] =  s.interpret_param(v)
        # s.debug_log(f"post_data: {post_data}")


        group = {'id': 1, 'name': 'Test Group'}
        group_id = group.get("id",-1)
        s.debug_log(f"Group Id  : {group_id}")

        result = {}
        result["group"] = group
        return result
