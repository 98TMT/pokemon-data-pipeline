import requests
import json
import os

def fetch_pokemon(name) :
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error; Could not retrieve data for {name}, {e}")
        return None

def transform_pokemon_data(raw_data):
    transformed = {
        "name": raw_data["name"],
        "id": raw_data["id"],
        "types": [t["type"]["name"] for t in raw_data["types"]],
        "abilities": [a["ability"]["name"] for a in raw_data["abilities"]],
        "stats": {s["stat"]["name"]: s["base_stat"] for s in raw_data["stats"]}
    }
    return transformed

def save_to_json(data, filename="pokemon_data.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"successfully saved data to: {filename}")

name_to_find = "pikachu"
raw_data = fetch_pokemon(name_to_find)

if raw_data:
    clean_data = transform_pokemon_data(raw_data)
    save_to_json(clean_data)

    print("Cleaned Data Preview")
    print(json.dumps(clean_data, indent=4))
