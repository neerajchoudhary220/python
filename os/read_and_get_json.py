import json
with open('my.json') as f:
    data = json.load(f)
def folder_path(path):
  paths =path.replace('/','\\')
  print(paths)

folder_path(data['folder_path']['physio'])


