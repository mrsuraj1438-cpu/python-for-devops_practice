import requests
import json


# API URLs for different joke sources
pj_url = "https://official-joke-api.appspot.com/random_joke"
dad_url = "https://icanhazdadjoke.com/"

def get_joke(url_type,mood):
    # Header tells API that we want JSON response
    header = {
        "Accept" : "application/json"
    }
    
    try: 
        # Make GET request to API
        response = requests.get(url=url_type,headers=header) 
        data = response.json() # convert response to JSON once  
        
        # Check if API request was successful
        if response.status_code == 200: 
            
            # Return joke based on selected mood
             if mood == "dad":
                 final_joke = data['joke']
                 
             if mood == "pj":
                final_joke = data["setup"] + " " + data["punchline"]
                
             return final_joke # print final joke according to your mood
         
        else:
            # Handles cases like 404, 500 errors
            print(f"API failed with status code:{response.status_code}")
    
    except requests.exceptions.RequestException as e:
        # Handles network issues, timeout, invalid URL, etc.
        print(f"Error fecthing joke : {e}")
        return None
    

# Ask user for joke type
mood = input("Which type of joke would you like hear? eg.(dad,PJ): ").lower()

# Select correct API based on user choice
if mood == "dad":
    url_type = dad_url
elif mood == "pj":
    url_type = pj_url
else:
    # Handle invalid input gracefully   
    print("Invalid Choice! Please type 'dad' or 'pj' .")
    url_type = None

if url_type:
    # Fetch joke from API
    final_joke = get_joke(url_type,mood) 
    print(final_joke)
    
    if final_joke:
        # Save joke into JSON file
        with open("myjoke.json", "w") as file:
            json.dump({"joke": final_joke}, file, indent=4)
        print("Joke saved to myjoke.json")
   



