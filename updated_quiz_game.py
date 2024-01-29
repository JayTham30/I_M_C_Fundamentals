import time

quiz_questions = [
    {
        'question': "What is the capital of France?",
        'options': ["Berlin", "Madrid", "Paris", "Rome"],
        'correct_ans': 3
    },
    {
        'question': 'Which planet is known as the "Red Planet"?',
        'options': ["Earth","Mars","Jupiter","Venus"],
        'correct_ans': 2
    },
    {
        'question': "In what year did the Titanic sink?",
        'options': ["1912","1920","1905","1931"],
        'correct_ans': 1
    },
    {
        'question': "What is the largest mammal in the world?",
        'options': ["Elephant","Blue Whale","Giraffe","Polar Bear"],
        'correct_ans': 2
    },
    {
        'question': 'Which element has the chemical symbol "O" on the periodic table?',
        'options': ["Oxygen","Gold","Iron","Uranium"],
        'correct_ans': 1
    },
]

def display_question(question_data):
    print(question_data["question"])

    for i, option in enumerate(question_data["options"], start=1):
        print(f" {i}. {option}")

def take_user_input():
    while True:
        user_answer = input("Your answer (1/2/3/4): ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            return int(user_answer)
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

def quiz():
    quiz_time_limit = 10
    start_time = time.time()

    score = 0
    correct_answers = []
    wrong_answers = []

    for question_data in quiz_questions:
        display_question(question_data)

        user_answer = take_user_input()

        if user_answer == question_data["correct_ans"]:
            score += 1
            correct_answers.append(question_data["question"])
        else:
            wrong_answers.append(question_data["question"])
        
        elapsed_time = time.time() - start_time
        remaining_time = max(0, quiz_time_limit - elapsed_time)
        
        if elapsed_time >= quiz_time_limit:
            print(f"\nYour time is up! You only had {quiz_time_limit} seconds!")
            break

        print(f"Time remaining: {int(remaining_time)} seconds\n")

    print("Quiz completed!\n")
    print(f"Your final score: {score}/{len(quiz_questions)}\n")
    print("Correctly answered questions:")
    for question in correct_answers:
        print(f"- {question}")
    print("\nIncorrect answered questions:")
    for question in wrong_answers:
        print(f"- {question}")

if __name__ == "__main__":
    quiz()
    