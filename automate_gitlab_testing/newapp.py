import os
import sys
from modules.singleton import Singleton
import yaml

action_path="actions/"
actions ={}

# load Actions
def load_action():
    sys.path.insert(0,action_path)
    for f in os.listdir(action_path):
        fname, ext = os.path.splitext(f)
        if ext == '.py':
            mod = __import__(fname)
            actions[fname] = mod.Action()
    sys.path.pop(0)
    return actions

def run_action(acton_name, data):
    result = None
    for action in actions.values():
        if action.name() == acton_name:
            #result = action.mockup(data)
            result = action.run(data)
    return result



def execute_scenario(scenario_file):

    # load all available actions
    actions = load_action()
    # init th singleton
    s = Singleton()

    with open(scenario_file, 'r') as file:
        scenario = yaml.safe_load(file)

    variables = {}
    for k, v in scenario['variables'].items():
        s.set_setting(k,v)
    myvalue = s.get_setting('API_URL')
    s.debug_log(f"API_URL: : {myvalue}")
    # for a in scenario['actions']:
    #     print(a)
    #     # Get the first key-value pair
    #     first_key, first_value = next(iter(a.items()))

    #     print("First key:", first_key)
    #     print("First value:", first_value)        # action_name = k
    #     # print(f"-------------------- action : {action_name} ----------------------------")
    #     # action_name = v.get('name',None)
    #     # if action_name:
    #     #     print(f"action name: {action_name}")
    #     # # Get the first key
    #     # first_key = next(iter(data))

    #     # # Remove the first key-value pair
    #     # data.pop(first_key)
    
    for action in scenario['actions']:
        # The first element is always the action name
        first_key = next(iter(action))
        action_name = first_key
        action.pop(first_key)

        print(f"-------------------- action : {action_name} ----------------------------")
        action_id = action.get('id',None)
        # if action_id:
        #     print(f"action id: {action_id}")
        # 
        # print(action)
        
        # action = { }
        data = {}
        if action:
            params = action.get('params',None)
            if params:
                data = params
        s.debug_log(f"-------------------- data : {data}")

        artifact = run_action(action_name,data)
        if action:
            artifact_definitions = action.get('artifact',None)
            if artifact_definitions:
                path = None
                for k, v in artifact_definitions.items():

                    if k== "path":
                        path = v
                        s.artifacts[path]={}
                    else:
                        s.artifacts[path][k] = artifact[v]
                        # print(k,v)
        # s.debug_log(f"artifacts : {s.artifacts}")
    s.debug_log(f"to_delete_dict : {s.to_delete_dict}")
       

def main():


    # load all available actions
    actions = load_action()
    # init th singleton
    s = Singleton()

    # Set up the global variables
    # this will be loaded from the yaml variables part later on
    s.settings['API_URL']="https://gitlab.com/api/v4"
    s.settings['BEARER_TOKEN']="glpat-eiWMakeeYvoDvSxs_yWK"
    s.settings['DEBUG_MODE']=True

# username: 'Nekogeekaku'
# base_name: 'gitlab.com'
    print("-------------------- List of groups test ----------------------------")

    action_name = "list_group"
    data = { }
    run_action(action_name,data)


    print("-------------------- Creation of groups test ----------------------------")

    # init the data. TODO get from the yaml file
    action_name = "create_group"
    data = { "parent_id": 75764245,"group_name": "MyRootGroup"}
    run_action(action_name,data)




if __name__ == "__main__":
    execute_scenario('scenario2.yaml')
    # main()


# def create_project(project_name, namespace_id, with_readme=True):
#     """ Create a new project in GitLab """
#     data = {"name": project_name, "namespace_id": namespace_id}
#     response = requests.post(f"{API_URL}/projects", headers=headers, json=data)
#     if with_readme and response.status_code == 201:
#         project_id = response.json()["id"]
#         init_project_with_readme(project_id, project_name)
#     return response.json()

# def init_project_with_readme(project_id, project_name):
#     """ Initialize a project with a README file """
#     import git
#     import tempfile
#     import os
#     repo_url = f"git@gitlab.com:{project_name}.git"
#     with tempfile.TemporaryDirectory() as tmpdirname:
#         repo = git.Repo.init(os.path.join(tmpdirname, project_name))
#         origin = repo.create_remote('origin', repo_url)
#         with open(os.path.join(tmpdirname, project_name, 'README.md'), 'w') as f:
#             f.write(f"# {project_name}\nInitial README file")
#         repo.index.add(['README.md'])
#         repo.index.commit("Initial commit with README")
#         origin.push(refspec='master:master')




# def main():
#     # Initialize configuration
#     config = Config()
#     group = Group(config)
#     project = Project(config)
#     to_delete_dict = {}
#     to_delete_dict['groups'] = {'ids': []}
#     to_delete_dict['projects'] = {'ids': []}

#     # response_json = project.list()
#     # print(json.dumps(response_json, indent=4))
#     # response_json = group.list()
#     # print(json.dumps(response_json, indent=4))
#     print("-------------------- Creation of groups ----------------------------")

#     # Create root group : Not possible in gitlab.com
#     root_group = group.create("MyRootGroup")
#     print(json.dumps(root_group, indent=4))
#     # Example usage
#     # Create a subgroup
#     root_id = 75764245 #in gitlab.com
#     # root_id=root_group["id"]
#     # to_delete_dict['groups']['ids'].append(root_id)
#     subgroup = group.create("SubGroup", parent_id=root_id)
#     print(json.dumps(subgroup, indent=4))
#     subgroup_id = subgroup["id"]
#     to_delete_dict['groups']['ids'].append(subgroup_id)
#     print(f"Subgroup ID to delete : {subgroup_id}")


#     print("-------------------- Creation of project ----------------------------")


#     project_data = project.create_under_group("first project",subgroup_id)
#     project_data_id = project_data["id"]
#     print(json.dumps(project_data, indent=4))
#     to_delete_dict['projects']['ids'].append(project_data_id)

#     print(f"project ID to delete : {project_data_id}")

#     # project_with_readme = create_project("ProjectWithREADME", subgroup["id"], with_readme=True)
#     # project_without_readme = create_project("ProjectWithoutREADME", subgroup["id"], with_readme=False)

#     with open('to_delete.yaml', 'w') as file:
#         yaml.dump(to_delete_dict, file)

#     # print(project.delete(project_data_id))
#     # print(group.delete(subgroup_id))
#     # print(group.delete(root_id))

# if __name__ == "__main__":
#     main()
