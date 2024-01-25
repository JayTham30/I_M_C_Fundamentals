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
