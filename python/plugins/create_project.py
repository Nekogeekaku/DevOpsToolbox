import yaml
import requests
import json

class Plugin:
    # def __init__(self):
        # print("plugin Test: constructor")
        # this is called when the plugin is loaded
    def name(self):
        return "project_create"
    def cb(self):
        print("project_create: this function create a project in a workspace.")
    def run(self, args):
        arg_length=len(args)
        if (arg_length < 3):
            print("Wrong number or argument for project_create")
            quit()
        if (arg_length == 3 and args[2]== "help"):
            print("project_create: this function create a project in a workspace.")
            print("toolbox create workspace_id path name")
            print("workspace_id: the id of the workspace to create the project into.")
            print("path: the path of the project.")
            print("name: the name of the project.")
            quit()
        print("running the plugin")
        with open('config/secrets.yml', 'r') as file:
            secrets = yaml.safe_load(file)
            headers = {"PRIVATE-TOKEN": secrets['gitlabapitoken']}
            api_url = secrets['gitlab_base_url']+"api/v4/projects/"
            datas = {
            "name": args[4],
            "description": "New Project",
            "path": args[3],
            "namespace_id": args[2],
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

            