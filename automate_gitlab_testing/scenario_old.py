import yaml
import requests
import json
#https://dummyjson.com/products/1

# Define a simple actions handler
def fetch_data(url):
    response = requests.get(url)
    return response.json()

def process_data(data, process_type):
    if process_type == "filter":
        # Example: filter out items with len of item > 10
        return [item for item in data if len(item) > 10]
    return data

def save_results(data, destination):
    with open(destination, 'w') as f:
        json.dump(data, f)

# Command mapping to function calls
actions = {
    "fetch_data": fetch_data,
    "process_data": process_data,
    "save_results": save_results
}

def execute_scenario(scenario_file):
    with open(scenario_file, 'r') as file:
        scenario = yaml.safe_load(file)
        
    variables = {}
    for step in scenario['scenario']:
        action = step['action']
        params = step['params']
        # Replace parameter variable names with actual values
        resolved_params = {k: (variables[v] if v in variables else v) for k, v in params.items()}
        # Execute action
        result = actions[action](**resolved_params)
        # Save result to variable if needed
        if 'save_as' in step:
            variables[step['save_as']] = result

# Example usage
if __name__ == "__main__":
    execute_scenario('scenario.yaml')