import time
import json

# Define subjects and their respective questions
subjects = ["Geography", "Science", "History", "Math", "Programming"]
subject_questions = {
    "Geography": [
        {"question": "What is the capital of France?", "options": ["London", "Berlin", "Paris", "Rome"], "correct_answer": 3},
        {"question": "Which river is the longest in the world?", "options": ["Nile", "Amazon", "Yangtze", "Mississippi"], "correct_answer": 2},
        {"question": "What is the largest desert in the world?", "options": ["Sahara Desert", "Gobi Desert", "Antarctic Desert", "Atacama Desert"], "correct_answer": 1},
        {"question": "Which river is the longest in Asia?", "options": ["Yangtze River", "Mekong River", "Ganges River", "Yellow River"], "correct_answer": 4}
    ],
    "Science": [
        {"question": 'Which planet is known as the "Red Planet"?', "options": ["Earth", "Mars", "Jupiter", "Venus"], "correct_answer": 2},
        {"question": "What is the largest mammal in the world?", "options": ["Elephant", "Blue Whale", "Giraffe", "Polar Bear"], "correct_answer": 1},
        {"question": "What is the chemical symbol for gold?", "options": ["Au", "Ag", "Fe", "Cu"], "correct_answer": 1},
        {"question": "Which gas do plants absorb during photosynthesis?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "correct_answer": 2}
    ],
    "History": [
        {"question": "In what year did the Titanic sink?", "options": ["1912", "1920", "1905", "1931"], "correct_answer": 1},
        {"question": 'Who was the first President of the United States?', "options": ["Thomas Jefferson", "George Washington", "Abraham Lincoln", "John Adams"], "correct_answer": 2},
        {"question": "Which war is also known as the Great War?", "options": ["World War I", "World War II", "Vietnam War", "Korean War"], "correct_answer": 1},
        {"question": "What ancient civilization built the pyramids?", "options": ["Roman", "Greek", "Maya", "Egyptian"], "correct_answer": 4}
    ],
    "Math": [
        {"question": "What is the result of 5 × (8 - 3)?", "options": ["25", "30", "35", "40"], "correct_answer": 2},
        {"question": "Solve for x in the equation 2x + 7 = 15.", "options": ["4", "5", "6", "8"], "correct_answer": 1},
        {"question": "What is the square root of 144?", "options": ["10", "12", "14", "16"], "correct_answer": 2},
        {"question": "If a triangle has angles of 90, 45, and 45 degrees, what type of triangle is it?", "options": ["Equilateral", "Isosceles", "Scalene", "Right-angled"], "correct_answer": 4}
    ],
    "Programming": [
        {"question": "What does the acronym 'HTML' stand for?", "options": ["Hypertext Markup Language", "Hyper Transfer Markup Language", "High-level Text Markup Language", "Home Tool Markup Language"], "correct_answer": 1},
        {"question": "In Python, what is the result of 2 + 3 * 4?", "options": ["14", "20", "24", "None of the above"], "correct_answer": 1},
        {"question": "What is the purpose of the 'if' statement in programming?", "options": ["Looping", "Decision-making", "Function declaration", "Variable assignment"], "correct_answer": 2},
        {"question": "Which programming language is known for its use in web development?", "options": ["Java", "C++", "Python", "JavaScript"], "correct_answer": 4}
    ]
}


def load_questions():
    try:
        with open("subject_questions.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
def save_questions(subject_questions):
    with open("subject_questions.json", "w" ) as file:
        json.dump(subject_questions, file)

subject_questions = load_questions()

def add_questions():
    new_subject = input("Please enter a subject: ").capitalize()
    new_question = input("Please enter a question: ")
    new_options_input = input('Please give your questions four options separeated by a "," with no spaces: ')
    new_options = new_options_input.split(',')
    new_answer = int(input("Please enter the index of the correct answer: "))

    if new_subject not in subject_questions:
        subject_questions[new_subject] = []
        subjects.append(new_subject)

    subject_questions[new_subject].append({
        "question": new_question,
        "options": new_options,
        "correct_answer": new_answer
    })

    save_questions(subject_questions)

    print(subjects)
    print(subject_questions.keys())
    print(subject_questions[new_subject])
    print("Question added successfully!")

def select_subject():
    print("Select a subject:")
    for i, subject in enumerate(subjects, 1):
        print(f"{i}. {subject}")
    while True:
        try:
            choice = int(input("Enter the number corresponding to your choice: "))
            if 1 <= choice <= len(subjects):
                return subjects[choice - 1]
            else:
                print("Invalid choice. Please enter a number between 1 and", len(subjects))
        except ValueError:
            print("Invalid input. Please enter a number.")

def run_quiz(questions):
    score = 0
    correct_ans = []
    wrong_ans = []

    quiz_time_limit = 60
    start_time = time.time()

    for i, question in enumerate(questions, 1):
        print(f"{i}. {question['question']}")
        for j, option in enumerate(question['options'], 1):
            print(f"   {j}. {option}")

        user_ans = input("Your answer (1/2/3/4): ")
        correct_index = int(user_ans) - 1

        if question['options'][correct_index] == question['options'][question['correct_answer'] - 1]:
            print("Correct!")
            score += 1
            correct_ans.append(question['question'])
        else:
            #print(f"Wrong! The correct answer is {question['options'][question['correct_answer'] - 1]}")
            wrong_ans.append(question['question'])

        if time.time() - start_time >= quiz_time_limit:
            print("Time is up! Quiz completed.")
            break

    finished_time = time.time() - start_time

    print(f"\nYou scored: {score}/{len(questions)}")
    print("Questions you got right:")
    print(f"{correct_ans}")
    print("Questions you got wrong:")
    print(f"{wrong_ans}")
    print(f"You've finished the quiz in {finished_time:.2f} sec.")

user_menu = input("Would you like to\n1) Take a quiz\n2) Add question: ")

if user_menu == "1":
    selected_subject = select_subject()
    selected_questions = subject_questions.get(selected_subject, [])

    print(f"\n{selected_subject} Quiz:")
    run_quiz(selected_questions)
elif user_menu == "2":
    add_questions()
else:
    print("Please select either option 1) or option 2)")
