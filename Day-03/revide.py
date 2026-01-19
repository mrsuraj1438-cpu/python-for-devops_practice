import requests

url ='https://jsonplaceholder.typicode.com/todos/1'
# dad_url = "https://icanhazdadjoke.com/"

def joke():
        
    headers = {
            "Accept": "application/json"
        }
    response = requests.get(url=url,headers=headers)
    data = response.json()
    status = response.status_code
    print(status) # check status code
    print(data)
    # print(response.json()['joke'])


joke()