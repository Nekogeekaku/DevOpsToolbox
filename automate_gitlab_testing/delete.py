import requests
import json
import yaml
from modules.config import Config
from modules.group import Group
from modules.project import Project






def main():
    # Initialize configuration
    config = Config()
    group = Group(config)
    project = Project(config)
    with open('to_delete.yaml', 'r') as file:
        to_delete = yaml.safe_load(file)
        print(to_delete)
        group_ids = to_delete['groups']['ids']
        project_ids = to_delete['projects']['ids']
        for id in project_ids:
            print(f"Project ID to delete: {id}")
            print(project.delete(id))
        for id in group_ids:
            print(f"Group ID to delete: {id}")
            print(group.delete(id))
 
    print("----------------- End of deletion -----------------------------")

if __name__ == "__main__":
    main()
