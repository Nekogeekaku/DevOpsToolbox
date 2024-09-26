import json
import requests
import config



class Group:
    def __init__(self, config):
        self.config = config
        self.api_url = config.get_setting('api_url')
        self.bearer_token = config.get_setting('bearer_token')
        self.headers = {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json"
        }
    def list(self):
        """ list groups in GitLab """

        response = requests.get(f"{self.api_url}/groups", headers=self.headers)
        return response.json()

    def create(self,group_name, parent_id=None):
        """ Create a new group in GitLab """
        data = {"name": group_name, "path": group_name.lower()}
        if parent_id:
            data["parent_id"] = parent_id
        response = requests.post(f"{self.api_url}/groups", headers=self.headers, json=data)
        return response.json()

    def delete(self,group_id):
        """ Delete a  group in GitLab """

        response = requests.delete(f"{self.api_url}/groups/{group_id}",headers=self.headers)
        return response.json()

            
