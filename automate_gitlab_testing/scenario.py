import yaml
import actions
from modules.singleton import Singleton

def execute_scenario(scenario_file):
    with open(scenario_file, 'r') as file:
        scenario = yaml.safe_load(file)
        
    variables = {}
    for step in scenario['scenario']:
        action = step['action']
        print(f"Executing : {action} ...")
        # params = step['params']
        params = step.get('params',None)
        # Replace parameter variable names with actual values
        if params:
            resolved_params = {k: (variables[v] if v in variables else v) for k, v in params.items()}
          # Dynamically execute action
        if hasattr(actions, action):
            func = getattr(actions, action)
            if params:
                result = func(**resolved_params)
            else:
                result = func()
            # Save result to variable if needed
            if 'save_as' in step:
                variables[step['save_as']] = result
        else:
            raise ValueError(f"No such action '{action}' defined.")

# Example usage
if __name__ == "__main__":
    s = Singleton()
    
    execute_scenario('scenario.yaml')
