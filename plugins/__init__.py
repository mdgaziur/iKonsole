import os
def import_plugin(plugins):
    list=list.split('\n')
    print(list)
os.path.dirname(__file__)
try:
    with open(__file__+"/list.txt") as list:
        list=list.read()
        import_plugin(list)
except:
    print("list.txt is not available!")