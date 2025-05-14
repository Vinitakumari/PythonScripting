import pickle
instances = {"instanceName": "web", "ports":["22","80","144"]}

with open ('instances.dat' ,'wb') as f:
    pickle.dump(instances,f)

with open ('instances.dat','rb') as  f:
   loaded_instances =pickle.load(f)
   print(loaded_instances)