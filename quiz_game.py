questions_options = {
    "What is the capital of France?":["London","Berlin","Paris","Rome"], #Paris
    'Which planet is known as the "Red Planet"?':["Earth","Mars","Jupiter","Venus"], #Mars
    "In what year did the Titanic sink?":["1912","1920","1905","1931"], #1912
    "What is the largest mammal in the world?":["Elephant","Blue Whale","Giraffe","Polar Bear"], #Blue Whale
    'Which element has the chemical symbol "O" on the periodic table?':["Oxygen","Gold","Iron","Uranium"] #Oxygen
    }

# Indexing to select specific values for answering.
 
all_keys = list(questions_options.keys())
all_values = list(questions_options.values())
question_1 = all_keys[0]
question_2 = all_keys[1]
question_3 = all_keys[2]
question_4 = all_keys[3]
question_5 = all_keys[4]

score = 0
correct_ans = []
wrong_ans = []

user_ans1 = input(f"{question_1}\n"
              f"1.{all_values[0][0]}\n"
              f"2.{all_values[0][1]}\n" 
              f"3.{all_values[0][2]}\n" 
              f"4.{all_values[0][3]}\n" 
              "Your answer (1/2/3/4): ")
if user_ans1 == "3":
    print("Correct!")
    score += 1
    correct_ans.append(question_1)
else:
    print(f"Wrong! the coorect answer is {all_values[0][2]}")
    wrong_ans.append(question_1)


user_ans2 = input(f"{question_2}\n" 
              f"1.{all_values[1][0]}\n" 
              f"2.{all_values[1][1]}\n"
              f"3.{all_values[1][2]}\n" 
              f"4.{all_values[1][3]}\n"
              "Your answer (1/2/3/4): ")
if user_ans2 == "2":
    print("Correct!")
    score += 1
    correct_ans.append(question_2)
else:
    print(f"Wrong! the coorect answer is {all_values[1][1]}")
    wrong_ans.append(question_2)

user_ans3 = input(f"{question_3}\n" 
              f"1.{all_values[2][0]}\n" 
              f"2.{all_values[2][1]}\n"
              f"3.{all_values[2][2]}\n" 
              f"4.{all_values[2][3]}\n"
              "Your answer (1/2/3/4): ")
if user_ans3 == "1":
    print("Correct!")
    score += 1
    correct_ans.append(question_3)
else:
    print(f"Wrong! the coorect answer is {all_values[2][0]}")
    wrong_ans.append(question_3)

user_ans4 = input(f"{question_4}\n"
              f"1.{all_values[3][0]}\n" 
              f"2.{all_values[3][1]}\n" 
              f"3.{all_values[3][2]}\n"
              f"4.{all_values[3][3]}\n"
              "Your answer (1/2/3/4): ")
if user_ans4 == "2":
    print("Correct!")
    score += 1
    correct_ans.append(question_4)
else:
    print(f"Wrong! the coorect answer is {all_values[3][1]}")
    wrong_ans.append(question_4)

user_ans5 = input(f"{question_5}\n" 
              f"1.{all_values[4][0]}\n" 
              f"2.{all_values[4][1]}\n" 
              f"3.{all_values[4][2]}\n"
              f"4.{all_values[4][3]}\n"
              "Your answer (1/2/3/4): ")
if user_ans5 == "1":
    print("Correct!\n")
    score += 1
    correct_ans.append(question_5)
else:
    print(f"Wrong! the coorect answer is {all_values[4][0]}\n")
    wrong_ans.append(question_5)


print(f"You scored: {score}/5")

print("Questions you got right:\n"
      f"{correct_ans}\n")

print("Questions you got wrong:\n"
      f"{wrong_ans}")








