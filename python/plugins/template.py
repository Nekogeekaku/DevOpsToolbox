class Plugin:
    # def __init__(self):
        # print("plugin Test: constructor")
        # this is called when the plugin is loaded
    def name(self):
        return "template"

    def cb(self):
        print("template plugin : an example of template")
    def run(self):
        print("running the template plugin")