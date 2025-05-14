import json

instances = {"instanceName": "web", "ports":["22","80","144"]}

with open ('instances.json','w') as f:
   json.dump(instances,f, indent=4)

with open('instances.json','r') as f:
    loaded_json =json.load(f)
    print (loaded_json)