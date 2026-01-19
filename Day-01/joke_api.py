import requests
import json

pj_url = "https://official-joke-api.appspot.com/random_joke"
dad_url = "https://icanhazdadjoke.com/"


def get_joke(url_type,mood):
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(url=url_type ,headers=headers)

    print(f"Status_code: {response.status_code}")
    data = response.json()
    if response.status_code == 200:
            if mood == "dad":
               final_joke = response.json()["joke"]
            if mood == "pj":
             final_joke = response.json()["setup"] +" "+ response.json()["punchline"]
 
            return final_joke   
    # print(f"final joke :{final_joke}")

mood = input("Which joke would you like to hear? eg. (Dad, PJ):").lower()

# whihc type of joke what you want : dad or pj
if mood == "dad":
    url_type = dad_url
elif mood == "pj":
    url_type = pj_url  
else:
    url_type = dad_url

final_joke = get_joke(url_type,mood)
print(final_joke)

# save the data into json file

if final_joke:
    print("\n😂 Joke:")
    print(final_joke)
    with open("joke.json", "w") as file:
         json.dump({"joke": final_joke}, file, indent=4)
    print("\n💾 Joke saved successfully in joke.json")

else:
    print("❌ Failed to fetch joke")