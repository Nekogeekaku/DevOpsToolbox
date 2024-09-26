import yaml



class Config:
    def __init__(self, config_path="config/config.yaml"):
        self.config_path = config_path
        self.settings = self.load_config()

    def load_config(self):
        """Load the configuration file from the given path."""
        try:
            with open(self.config_path, 'r') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            raise FileNotFoundError("The configuration file was not found.")
        except yaml.YAMLError as exc:
            raise RuntimeError("Error parsing the YAML file: {}".format(exc))

    def get_setting(self, key):
        """Retrieve a setting value by key."""
        return self.settings.get(key, None)