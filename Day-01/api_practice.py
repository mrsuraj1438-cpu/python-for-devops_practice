import requests

# url api 

# url_api = "https://jsonplaceholder.typicode.com/todos/1"

# # how to access this api data

# response = requests.get(url=url_api)

# # print(response.status_code) # check success

# # show the data
# print(response.json())
# # print(dir(response))


# data = response.json()
# # print(data["title"])

# # for i in data:
# #     if i == "id":
# #         print(data[i])



# for i, j in data.items():
#     # if i == "id":
#         print(i,j)

# # def api_fun():
# #     for user in response:
# #         print(user["id"])


# access the joke api

# joke_url = "https://official-joke-api.appspot.com/random_joke"
new_url = "https://jsonplaceholder.typicode.com/todos/1"
# response = requests.get(url=joke_url)
response = requests.get(url=new_url)
# print(type(response))
print(response.status_code)
'''
def api_call():
    try:
        if response.status_code == 200:
            data = response.json()
            print(f"joke : {data["setup"] +" "+ data["punchline"]}")
        else:
            print("API failed")
            print("Status Code", response.status_code)
    except requests.exceptions.RequestException as e:
        print("API call failed",e)
        # print(type(e))
        api_call()
'''
# for key,value in response.json().items():
#     print(key,value)

# for key, value in response.json().items():
#     if key == "setup":
#         print(f"value of 'setup':{response.json()[key]}")

for key, value in response.json().items():
    if key == "id":
        if value in [10,22,33]:
            print("The user found")
        else:
            print("the user not found")
# import requests

# try:
#     requests.get("https://httpstat.us/200?sleep=10000", timeout=0.022)
# except requests.exceptions.RequestException as e:
#     print("Timeout error caught")
#     print(type(e))
#     print(e)
    

# else:
#     data = response.json()
#     print(data)
    

# print(response.status_code) # check status : if stat_code == 200 it is ok

# print(response.json())

# final_joke = response["setup"] + response["punchline"]

# print(final_joke)