import json


# quick script to sort and prettify the 'ingredients.json' file
if __name__ == "__main__":
    with open('ingredients.json', 'r') as fp:
        ingreds = json.load(fp)
    with open('ingredients.json', 'w') as fp:
        json.dump(ingreds, fp, indent=4, sort_keys=True, ensure_ascii=False)
