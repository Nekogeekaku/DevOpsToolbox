import yaml
from modules.singleton import Singleton


class Action:
    #def __init(self):
        # print("Plugin create_group constructor")
        # This is called when the plugin is loaded
    def name(self):
        return "save_to_delete_file"
    def definition(self):
        print("Give a definition of save_to_delete_file")
    def run(self, data):
        s = Singleton()
        post_data = {}
        for k, v in data.items():
            print(k,v)
            post_data[k] =  s.interpret_param(v)
        filename = post_data["filename"]
        with open(filename, 'w') as file:
            yaml.dump(s.to_delete_dict, file)

    def mockup(self, data):
        s = Singleton()
        post_data = {}
        for k, v in data.items():
            print(k,v)
            post_data[k] =  s.interpret_param(v)
        s.debug_log(post_data)
        filename = post_data["filename"]
        s.debug_log(f"filename: {filename}")
        s.debug_log(f"filedata: {s.to_delete_dict}")
        
