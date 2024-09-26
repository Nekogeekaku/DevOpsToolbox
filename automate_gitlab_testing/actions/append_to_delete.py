import json
import requests
from modules.singleton import Singleton


class Action:
    #def __init(self):
        # print("Plugin create_group constructor")
        # This is called when the plugin is loaded
    def name(self):
        return "append_to_delete"
    def definition(self):
        print("Give a definition of append_to_delete")
    def run(self, data):
        s = Singleton()
        post_data = {}
        for k, v in data.items():
            print(k,v)
            post_data[k] =  s.interpret_param(v)
        typeOfCreation =  post_data["type"]
        path = f"{typeOfCreation}.ids"
        id = post_data["id"]
        s.append_value_to_path(s.to_delete_dict,path,id)
        # s.to_delete_dict[post_data["type"]]['ids'].append(post_data["id"])

    def mockup(self, data):
        s = Singleton()
        post_data = {}
        for k, v in data.items():
            print(k,v)
            post_data[k] =  s.interpret_param(v)
        s.debug_log(post_data)
        typeOfCreation =  post_data["type"]
        path = f"{typeOfCreation}.ids"
        id = post_data["id"]
        s.append_value_to_path(s.to_delete_dict,path,id)
        # s.to_delete_dict[post_data["type"]]['ids'].append(post_data["id"])
