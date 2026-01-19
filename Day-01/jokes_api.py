import requests

pj_url = "https://official-joke-api.appspot.com/random_joke"
dad_url = "https://icanhazdadjoke.com/"

def get_joke(url_type,mood):
    # header add 
    header = {
        "Accept" = "application/json"
    }
    joke = requests.get(url=url_type,headers=header) 
    # print(joke.json())
    if mood == "dad":
        final_joke = joke.json()
    # final_joke = joke.json() ["setup"] + joke.json() ["punchline"]
    return final_joke

mood = input("Which type of joke would you like hear? eg.(dad,PJ)")
if mood == "dad":
    url_type = dad_url
elif mood == "pj":
    url_type = pj_url

final_joke = get_joke(url_type,mood)
print(final_joke)