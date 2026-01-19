import requests

# url ='https://jsonplaceholder.typicode.com/todos/1'
dad_url = "https://icanhazdadjoke.com/"

response = requests.get(url=dad_url)
data = response.json()
status = response.status_code

print(status)

print(response.json())
# print(dir(response))
# print(response.json())

# for key,value in response.json().items():
#     print(key,value)

# for key,value in response.json().items():
#     if key == "completed":
#         if value == "False":
#             print("The data is not completed in the  server.")

# for key,value in response.json().items():
#     if key == "userId":
#         if value in [1,2,3,4,5]:
#             print(f"User Found:{value}")

# for key,value in response.json().items():
#     if key == "userId":
#         if value in [100,2,3,4,5]:
#             print(f"User Found:{value}")
#         else:
#             print("user not found:")
            
 # Task:
'''
 Today’s goal is to use Python to interact with APIs and work with JSON data.

You will create a Python script that:

Calls a public API (example: GitHub API, JSONPlaceholder) list
Fetches data using the requests library
Parses the JSON response
Extracts meaningful information from the response
Prints the processed output to the terminal
Saves the processed data into a JSON file
'''