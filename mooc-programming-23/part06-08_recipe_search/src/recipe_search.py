# Write your solution here
def search_by_name(filename: str, word: str):
    
    recipe_list = []
    with open(filename) as recipes:
        for line in recipes:
            line = line.replace("\n", "")
            parts = line.split(",")
            recipe_list.append(parts)

    for i in recipe_list:
        for x in i:
            if word in x.lower():
                print(x)

def ingredients_dict(filename):
    recipes = {}
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line and not line.isdigit():
                recipe_name = line
                recipes[recipe_name] = {'time': None, 'ingredients': []}
            elif line.isdigit():
                recipes[recipe_name]['time'] = int(line)
            elif line:
                recipes[recipe_name]['ingredients'].append(line)
    print(recipes)




ingredients_dict('src/recipes1.txt')
# search_by_name('src/recipes1.txt', 'cake')