import json
import requests
import config



class Project:
    def __init__(self, config):
        self.config = config
        self.api_url = config.get_setting('api_url')
        self.bearer_token = config.get_setting('bearer_token')
        self.headers = {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json"
        }
    def list(self):
        """ list projects in GitLab """

        response = requests.get(f"{self.api_url}/projects", headers=self.headers)
        return response.json()


    def create_under_group(self,project_name, namespace_id):
        """ Create a new project in GitLab """
        data = {"name": project_name, "namespace_id": namespace_id}
        response = requests.post(f"{self.api_url}/projects", headers=self.headers, json=data)
        return response.json()


    def delete(self,project_id):
        """ Delete a  group in GitLab """

        response = requests.delete(f"{self.api_url}/projects/{project_id}",headers=self.headers)
        return response.json()

    def get_path_with_namespace(self,project_id):
        """ get path with namespace """
        project_info = requests.get(f"{self.api_url}/projects/{project_id}", headers=self.headers).json()
        return project_info['path_with_namespace']
