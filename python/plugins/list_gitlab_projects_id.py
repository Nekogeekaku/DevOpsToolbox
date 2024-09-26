import yaml
import requests
import json

class Plugin:
    # def __init__(self):
        # print("plugin Test: constructor")
        # this is called when the plugin is loaded
    def tool(self):
        return "gitlab"
    def action(self):
        return "list"
    def sub_action(self):
        return "projectids"
    def cb(self):
        print("gitlab list projectids: this function list project ids in a workspace.")
    def run(self, args):
        arg_length=len(args)
        if (arg_length < 5):
            print("Wrong number or argument for list_projects")
            quit()
        if (arg_length == 5 and args[4]== "help"):
            print("list_projects: this function list project ids in a workspace.")
            print("toolbox gitlab list projectids workspace_id")
            print("workspace_id: the id of the workspace to  list project ids from.")
            quit()
        print("running the plugin")
        with open('config/secrets.yml', 'r') as file:
            secrets = yaml.safe_load(file)
            headers = {"PRIVATE-TOKEN": secrets['gitlabapitoken']}
            api_url = secrets['gitlab_base_url']+"api/v4/groups/"+args[4]+"/projects"
            # GET /groups/:id/projects

            response = requests.get(api_url,headers=headers)
            # print(response.json())
            # print(response.status_code)
            # print(response.headers["Content-Type"])
            for project in response.json():
                print(str(project["id"]))
            