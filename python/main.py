import os
import sys

path = "plugins/"
plugins = {}

# Load plugins
sys.path.insert(0, path)
for f in os.listdir(path):
    fname, ext = os.path.splitext(f)
    if ext == '.py':
        mod = __import__(fname)
        plugins[fname] = mod.Plugin()
sys.path.pop(0)

arg_length=len(sys.argv)
if arg_length<2:
    print("Available plugins")
    for plugin in plugins.values():
        plugin.cb()
    quit()
# display the functions and arguments
else:
    pluginname=sys.argv[1]
    for plugin in plugins.values():
        if (plugin.name()==pluginname):
            plugin.run()
   
