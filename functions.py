def dollarizer(word):
    return word.replace("s", "$")

def eurizer(word):
    return word.replace("e", "€")

def replacer(word, char1, char2):
    return word.replace(char1, char2)

def wonky_text(word):
    dollar = dollarizer(word)
    return eurizer(dollar)

def celsius_to_fahrenheit(temp_in_c):
    temp_in_f = int(temp_in_c) * 1.8 + 32
    return temp_in_f

def age_in_days(age):
    days = age * 365
    return days

def simple_interest(principal, rate_of_int, time_in_years):
    si = principal * rate_of_int * time_in_years
    return si

def plan_finances(principal, rate_of_int, time_in_years, final_amount):
    si = principal * rate_of_int * time_in_years / 100
    final_after_int = principal + si
    if final_after_int >= final_amount:
        print(f"The desired final amount {final_amount} is achievable.")
        return True  
    else:
        print(f"The desired final amount {final_amount} is NOT achievable")
        return False
        
    
print(plan_finances(1000, 5, 2, 1200))


