def main():
    user_fruit = input('Item: ').lower()
    nutrition_facts(user_fruit)



def nutrition_facts(fruit):
    calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "lemon": 15,
        "lime": 20,
        "kiwifruit": 90,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pineapple": 50,
        "plums": 70,
        "pear": 100,
        "sweet cherries": 100,
        "strawberries": 50,
        "tangerine": 50,
        "watermelon": 80
        }

    if fruit in calories:
        print(f"Calories: {calories[fruit]}")

if __name__ == "__main__":
    main()    