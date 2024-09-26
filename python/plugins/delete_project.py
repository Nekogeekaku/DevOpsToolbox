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
        return "delete"
    def sub_action(self):
        return "project"
    def cb(self):
        print("project_create: this function create a project in a workspace.")
    def run(self, args):
        arg_length=len(args)
        if (arg_length < 5):
            print("Wrong number or argument for project_create")
            quit()
        if (arg_length == 5 and args[4]== "help"):
            print("Delete a project.")
            print("-----------------")
            print("toolbox gitlab delete project project_id")
            print("project_id: the id of the project to delete.")
            quit()
        print("running the plugin")
        with open('config/secrets.yml', 'r') as file:
            secrets = yaml.safe_load(file)
            headers = {"PRIVATE-TOKEN": secrets['gitlabapitoken']}
            api_url = secrets['gitlab_base_url']+"api/v4/projects/"+args[4]
            # DELETE /projects/:id
            response = requests.delete(api_url,headers=headers)
            print(response.json())
            print(response.status_code)
            print(response.headers["Content-Type"])

            