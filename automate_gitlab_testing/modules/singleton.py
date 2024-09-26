from modules.config import Config

class Singleton:
    _instance = None
    settings = None  # Shared variable
    config = None
    to_delete_dict = None
    group = None
    project = None
    gitutilities = None
    artifacts = None
    # usage is 
    # from singleton import Singleton
    # s = Singleton()
    # print(s.value) 
    # s.value = "Updated from module1"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls.settings = {}
            cls.artifacts = {}
            cls.to_delete_dict = {}
        return cls._instance

    def init_config(cls, config_path="config/config.yaml"):
        cls.config = Config(config_path)

    def get_setting(self, key):
        """Retrieve a setting value by key."""
        return self.settings.get(key, None)
    def set_setting(self, key, value):
        """Retrieve a setting value by key."""
        self.settings[key] = value

    def debug_log(self, data):
        if (self.get_setting("DEBUG_MODE") == True):
            print(data)

    def navigate_to_path(self,d, path):
        keys = path.split('.')
        for key in keys:
            d = d[key]
        return d
    def append_value_to_path(self,d, path, value):
        keys = path.split('.')
        base = d
        for key in keys[:-1]:
            d = d.setdefault(key, {})
            print(f"key: {key} // {d}")
        d=d.setdefault(keys[-1], [])

        print(base)
        print(keys[-1])
        d.append (value)

    def interpret_param(self,value):
        result =None
        #path = ""#'$var1.group.name'
        if str(value).isnumeric() :
            result = value
        elif value[0] == '$':
            path = value[1:]
            result = self.navigate_to_path(self.artifacts,path)
        else:
            result = value
        return result