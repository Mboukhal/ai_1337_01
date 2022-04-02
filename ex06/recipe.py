#! /usr/bin/env python

cookbook = {
    "Sandwich's" : {
        "ingredients" : ["ham", "bread", "cheese", "tomatoes"],
        "meal" : "lunch",
        "prep_time" : 10
     },
    "Cake's" : {
        "ingredients" : ["flour", "sugar", "eggs"],
        "meal" : "dessert",
        "prep_time" : 60
    },
    "Salad's" : {
        "ingredients" : ["avocado", "arugula", "tomatoes", "spinach"],
        "meal" : "lunch",
        "prep_time" : 15
    }
}

def get_recipe(book):
    for key in book.items() :
        print(f"{key[0]}")

def get_recipe_details(recipe):
    print(f"Recipe for {recipe}:")
    ingredients = cookbook[recipe]["ingredients"]
    print(f"\tIngredients list: {ingredients}")
    meal = cookbook[recipe]["meal"]
    time = cookbook[recipe]["prep_time"]
    print(f"\tTo be eaten for {meal}")
    print(f"\tTakes {time} minutes of cooking.")

def del_recipe(recipe):
    cookbook.pop(recipe, None)

def add_recipe():
    print("Enter a name:")
    name = input()

    print("Enter ingredients:")
    ingredients = []

    for i in range(0, 3):
        item = input()
        ingredients.append(item)

    print("Enter a meal type:")
    meal = input()
    
    print("Enter a preparation time:")
    prep_time = int(input())

    new_recipe = {name : {"ingredients":ingredients ,"meal":meal,"prep_time":prep_time}}
    cookbook.update(new_recipe)


if __name__ == "__main__":

    print("Welcome to the Python Cookbook !")
    while True:
        print("""List of available option:
    1: Add a recipe
    2: Delete a recipe
    3: Print a recipe
    4: Print the cookbook
    5: Quit
        """)
        print("\nPlease select an option: ")
        cmd = input()
        if cmd == '1':
            add_recipe()
        if cmd == '2':
            print("\nPlease select recipe to delete: ")
            del_recipe(input())
        if cmd == '3':
            print("\nPlease enter a recipe name to get its details: ")
            inp = str(input())
            print()
            if inp in cookbook:
                get_recipe_details(inp)
                print()
            else:
                print("Sorry, this option does not exist.")

        if cmd == '4':
            print()
            get_recipe(cookbook)
            print()
        if cmd == '5':
            print("\nCookbook closed. Goodbye !")
            exit()
        