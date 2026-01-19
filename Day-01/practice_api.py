import requests
import json

# url fetch the api data 

api_url = "https://api.restful-api.dev/objects"

# request to api 

def api_get_status():
    response = requests.get(url=api_url)
    
    # print(response.status_code)
    # print(response.json())
    # print all products name:
    # print(type(response.json()))
    try:
        data = response.json()
        # check api_Status _code : 200(ok)
        if response.status_code == 200:
            with open("products.json", "w") as file:
             json.dump(data, file, indent=4)
             print("✅ Data saved successfully to products.json\n")
             # access data from data use the item variable 
             for item in data:
                 print(f"product name: {item['name']}") # print item : name : like products name
                 print("Specifications:") # each time print 
                 # if data is None(null) in jsone file:
                 if item["data"] is not None:
                    # print nested dictionary key, value pair
                    for key, value  in item["data"].items():
                     print(f" {key}: {value}")
                 else:
                    # if data is None 
                    print(" No specifications available")
                 print("-" * 20)    
        else:
         # if status code is failed : 404
         print(f"api failed :status_code :{response.status_code}")
    # if try failed then expect is print
    except requests.exceptions.RequestException as e:
        print("API failed",e)
        print(type(e))

api_get_status()

