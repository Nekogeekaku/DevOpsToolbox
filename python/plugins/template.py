class Plugin:
    # def __init__(self):
        # print("plugin Test: constructor")
        # this is called when the plugin is loaded
    def tool(self):
        return "template"
    def action(self):
        return "template"
    def sub_action(self):
        return "template"
    def name(self):
        return "template"

    def cb(self):
        print("template plugin : an example of template")
    def run(self):
        print("running the template plugin")