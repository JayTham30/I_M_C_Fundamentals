#EXCERCISE 1
fruits = ["apple", "banana", "cherry", "date"]
fruits.append("elderberry")
fruits.remove("banana")
fruits.sort

#print(fruits)

#EXCERCISE 2
student = {"name":"John Doe", "age":"25", "major":"Computer Science"}
student["major"] = "Electrical Engineering"
student["year"] = "Senior"

all_keys = student.keys()
all_values = student.values()
#print(all_keys)
#print(all_values)

#EXCERCISE 3
book = [{"title":"Don Quixote", "author":"Miguel de Cervantes", "year":"First part published in 1605, second part in 1615"},
        {"title":"A Tale of Two Cities", "author":"Charles Dickens", "year":"1859"},
        {"title":"The Lord of the Rings", "author":"J.R.R. Tolkien", "year":"The trilogy was published between 1954 and 1955"}
]


'''for title in book:
    print("Title:", title["title"])'''

third_book_year = book[2]["year"]
#print(f"Year of third book in list: {third_book_year}")

#EXCERCISE 4
courses = {"math":["Emma Johnson", "Ethan Smith", "Olivia Davis", "Liam Miller", "Sophia Wilson"],
           "history":["Noah Brown", "Ava Anderson", "Lucas Martinez", "Isabella Taylor", "Mason Thompson"],
           "chemistry":["Mia Harris", "Aiden Jackson", "Harper White", "Elijah Clark", "Abigail Turner"]
           }

new_students = ["Grace Robinson", "Caleb Mitchell", "Amelia Cooper", "Benjamin Foster", "Stella Reed"]
courses["math"].extend(new_students)

removing_student = courses["history"].pop(2)

#print(courses["chemistry"])

courses["physics"] = ["Scarlett Martinez", "Sebastian Carter", "Maya Patel", "Leo Ramirez"]

for course, students in courses.items():
    print(f"{course} students:")
    for student in students:
        print(f"  - {student}")
