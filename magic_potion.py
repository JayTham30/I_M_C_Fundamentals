potions = {
    "invisibility potion": ["moonstone", "dragon scale", "fairy dust"],
    "flying potion": ["phoenix feather", "troll tooth", "mermaid scale"],
    "healing potion": ["unicorn horn", "elf hair", "golden apple"]
}


print("Welcome to the Magic Potion Shop!\nHere are the potions we offer:\n-Invisibility Potion\n-Flying Potion\n-Healing Potion\n")
chosen_potion = input("Which potion would you like to buy ingredients for? ").lower()


if chosen_potion in potions:
    print(f"The ingredients for {chosen_potion} are: \n")

    for ingredient in potions[chosen_potion]:
        print(f"{ingredient}")

    print("Let's start buying the ingredients! \n")
    all_ingredients_purchased = True


    for ingredient in potions[chosen_potion]:
        while all_ingredients_purchased == True:
            buy_current_potion = input(f"Do you want to buy {ingredient}? (Yes/No): ").lower()

            if buy_current_potion == "yes":
                print(f"You bought {ingredient}")
                break
            elif buy_current_potion == "no":
                print("You chose to stop shopping")
                all_ingredients_purchased = False
                break
            else:
                print('Invalid input. Please enter "yes" or "no".')
    if all_ingredients_purchased:
        print(f"Congratulations! You bought all the ingredients for {chosen_potion}.")
else:
    print("Invalid potion choice. Please choose a valid potion.")
          
'''

# Potions and their ingredients
potions = {
    "invisibility potion": ["moonstone", "dragon scale", "fairy dust"],
    "flying potion": ["phoenix feather", "troll tooth", "mermaid scale"],
    "healing potion": ["unicorn horn", "elf hair", "golden apple"]
}

# Display the list of potions
print("Choose a potion:")
for potion in potions:
    print(f"- {potion}")

# Ask the user to choose a potion
chosen_potion = input("Enter the name of the potion you want: ").lower()

# Check if the chosen potion exists
if chosen_potion in potions:
    print(f"\nIngredients for {chosen_potion}:")

    # Display ingredients for the chosen potion
    for ingredient in potions[chosen_potion]:
        print(f"- {ingredient}")

    all_ingredients_purchased = True  # Flag to track all ingredients are purchased

    # Buy ingredients
    for ingredient in potions[chosen_potion]:
        while True:
            buy_current_ingredient = input(f"Do you want to buy {ingredient}? (yes/no): ").lower()

            if buy_current_ingredient == "yes":
                print(f"Bought: {ingredient}")
                break  # Move to the next ingredient
            elif buy_current_ingredient == "no":
                print(f"Skipped: {ingredient}")
                print("Shopping canceled. Not all ingredients purchased.")
                all_ingredients_purchased = False
                break  # Exit the loop and shopping
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    if all_ingredients_purchased:
        print(f"Congratulations! You bought all the ingredients for {chosen_potion}. Enjoy your potion!\n")
else:
    print("Invalid potion choice. Please choose a valid potion.")

'''