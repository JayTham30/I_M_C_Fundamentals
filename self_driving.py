def move_forward():
    print("moving forward")

def turn(direction):
    print(f"{direction} turn.")

def start_engine():
    print("start engine")

def stopped_engine():
    print("stopped engine")

destination = input("Where do you want to go? ")

start_engine()
move_forward()

if destination == "school":
    turn("right")
    print("we arrived at school!")
elif destination == "grocery store" or destination == "dentist":
    turn("left")
    move_forward()
    if destination == "grocery store":
        turn("right")
        print("we arrived at grocery store")
    else:
        turn("left")
        print("we arrived at the dentist")
    
elif destination == "restaurant":
    move_forward()
    print("we arrived  at restaurant!")
else:
    print("invalid destination")

