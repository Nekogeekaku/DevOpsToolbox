import json
import requests
from modules.singleton import Singleton


class Action:
    #def __init(self):
        # print("Plugin create_group constructor")
        # This is called when the plugin is loaded
    def name(self):
        return "list_group"
    def definition(self):
        print("Give a definition of list group")
    def run(self, data):
        s = Singleton()
        api_url = s.get_setting('API_URL')
        bearer_token = s.get_setting('BEARER_TOKEN')
        headers = {
            "Authorization": f"Bearer {bearer_token}",
            "Content-Type": "application/json"
        }
        print(f" url : {api_url}/groups")
        print(f" headers : {headers}")
        response = requests.get(f"{api_url}/groups", headers=headers)

        print(response)
        print(response.json())
        return response
    
    def mockup(self, data):
        s = Singleton()
        groups = [{'id': 1, 'name': 'Test Group 1'},{'id': 2, 'name': 'Test Group 2'}]
        s.debug_log(f"Groups  : {groups}")

        return groups
