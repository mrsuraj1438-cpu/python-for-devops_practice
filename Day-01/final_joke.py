import json
final_joke = "Why don't scientists trust atoms? Because they make up everything."

with open("myjoke.json", "w") as file:
    json.dump({"joke": final_joke}, file, indent=4)
