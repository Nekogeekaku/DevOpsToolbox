import yaml
import requests

class Plugin:
    # def __init__(self):
        # print("plugin Test: constructor")
        # this is called when the plugin is loaded
    def name(self):
        return "projects"
    def cb(self):
        print("projects: this function list all available projects in a workspace.")
    def run(self, args):
        print("running the plugin")
        with open('config/secrets.yml', 'r') as file:
            secrets = yaml.safe_load(file)
            headers = {"PRIVATE-TOKEN": secrets['gitlabapitoken']}
            api_url = secrets['gitlab_base_url']+"api/v4/namespaces/"+secrets['Group_ID']
            response = requests.get(api_url,headers=headers)
            # print(response.json())
            print(response.json()['name'])
            print(response.status_code)
            print(response.headers["Content-Type"])

            api_url = secrets['gitlab_base_url']+"api/v4/groups/"+secrets['Group_ID']+"/projects"
            response = requests.get(api_url,headers=headers)
            # print(response.json())
            print(response.status_code)
            print(response.headers["Content-Type"])
            for project in response.json():
                print(project["name"]+": "+str(project["id"]))