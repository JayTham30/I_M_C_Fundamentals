global user_password

def checks_pass():
    
    main_char = 7
    special_char = ["!", "@", "#", "$", "%", "&"]
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # has_main_char = False
    # has_special_char = False
    # has_numbers = False
    # strong_pass = False


    while True:

        has_main_char = False
        has_special_char = False
        has_numbers = False
        strong_pass = False

        user_password = input('Enter your password (or type "quit" to exit): ')

        if user_password.lower() == "quit":
            print("\nExiting the Password Checker.")
            break


    #checks for length
        len_user_input = len(user_password)
        if len_user_input >= main_char:
            has_main_char = True
        else:
            print(f" \u2022Password must be {main_char} character long.")
            has_main_char = False
        

    #checks for special char
        special_char_count = 0
        for char in special_char:
            if char in user_password:
                has_special_char = True
                special_char_count += 1
                break

        if has_special_char:
            has_special_char = True
        else:
            print(" \u2022Password does not contain any special character!")
            has_special_char = False
        
            
    #checks for numbers
        num_count = 0

        for num in numbers:
            if str(num) in user_password:
                has_numbers = True
                num_count += 1
                break
        
        if has_numbers != True:
            print(" \u2022Password does not contain any numbers!")


    #checks for uppercase
        has_uppercase = any(char.isupper() for char in user_password)

        if has_uppercase != True:
            print(" \u2022Password does not contain any uppercase letters!")

    
    #checks the strength of password

        if has_numbers and has_main_char and has_special_char and has_uppercase:
            strong_pass = True

        if len_user_input >= 12 and strong_pass == True:
            print("You have a strong Password!\n")
        elif num_count >= 2 and strong_pass == True:
            print("You have a strong Password!\n")
        elif special_char_count >= 2 and strong_pass == True:
            print("You have a strong Password!\n")
        elif strong_pass == True:
            print("Your password is acceptable!\n")
        
    
def main():
        
        print("Welcome to the Password Checker!\n"
            "A strong password must meet the following criteria: \n"
            "- At least 7 characters long \n- Include at least 1 special character \n- Include at least 1 number \n- Include at least 1 uppercase letter\n")
        
        checks_pass()


if __name__ == "__main__":
    main()

