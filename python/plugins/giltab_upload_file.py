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
        return "project"
    def sub_action(self):
        return "upload"
    def name(self):
        return "project_upload"
    def cb(self):
        print("project_upload: this function create a project in a workspace.")
    def run(self, args):
        arg_length=len(args)
        if (arg_length < 5):
            print("Wrong number or argument for project_upload")
            quit()
        if (arg_length == 5 and args[4]== "help"):
            print("Create a project in a workspace.")
            print("--------------------------------")
            print("toolbox gitlab project upload workspace_id source destination")
            print("workspace_id: the id of the workspace to create the project into.")
            print("source: path of the file to upload.")
            print("destination: destination path.")
            quit()
        print("running the plugin")
        with open('config/secrets.yml', 'r') as file:
            secrets = yaml.safe_load(file)
            headers = {"PRIVATE-TOKEN": secrets['gitlabapitoken']}
            api_url = secrets['gitlab_base_url']+"api/v4/projects/"
            datas = {
            "name": args[6],
            "description": "New Project",
            "path": args[5],
            "namespace_id": args[4],
            "initialize_with_readme": "true"
            }

            # convert into JSON:
            y = json.dumps(datas)
            # the result is a JSON string:
            print(y)
            
    #         curl --request POST --header "PRIVATE-TOKEN: <your-token>" \
    #  --header "Content-Type: application/json" --data '{
    #     "name": "new_project", "description": "New Project", "path": "new_project",
    #     "namespace_id": "42", "initialize_with_readme": "true"}' \
    #  --url "https://gitlab.example.com/api/v4/projects/"

            response = requests.post(api_url,headers=headers, data=datas)
            # print(response.json())
            print(response.json())
            print(response.status_code)
            print(response.headers["Content-Type"])

            