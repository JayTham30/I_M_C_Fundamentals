"""
#Prompt 1
Upercase = input("Please enter a sentence: ")
print(Upercase.upper())

#Prompt 2
num_words = input("Please enter a paragraph: ")
print(len(num_words.split()))

#Prompt 3
if_digits = input("Please enter a string: ")
print(if_digits.isdigit())

#Prompt 4
a_to_o = input("Please enter another string: ")
print(a_to_o.replace("a", "o"))

#Prompt 5
name = input("Please enter your full name: ")
initials = name.split()
print(f"{initials[0][0]}.{initials[1][0]}".upper())
"""
#Prompt 6
len_str = input("Please enter one more string: ")
print(len(len_str))