import requests
import json
import csv

response = requests.get("https://jsonplaceholder.typicode.com/users")

# loading json strings into python objects and users as list of dictionaries
users = json.loads(response.text)

# opening the csv file for writing

with open ('users.csv','w') as f:
    writer = csv.writer(f)

    # write a header to a file
    writer.writerow(("Name","City","GPS","Compamy"))

    #iterating over the users list

    for user in users:
      name = user['name']
      city = user['address']['city']
      lat = user['address']['geo']['lat']
      lng = user['address']['geo']['lng']

      #constructing the GPS coordinates in form of (lat,lng)
      geo = f'({lat},{lng})'
      company_name = user['company']['name']

      #writing to csv file
      csv_data =(name,city,geo,company_name)

      writer.writerow(csv_data)
    

