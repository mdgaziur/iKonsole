import os
plugins=[]
def load_list(plugins):
    plugins=plugins.split('\n')
def is_plugin_exists(plugin):
    if plugin in plugins:
        return True
    else:
        return False
def import_plugins():
    for i in plugins:
        try:
            exec("import %s"%i)
        except:
            print("Error Importing plugin %s"%i)
            print("Maybe the plugin doesn't exists.")
cdir=os.path.dirname(__file__)
try:
    with open(cdir+"\\list.txt") as list:
        f=list.read()
        load_list(f)
except:
    print("list.txt is not available!")