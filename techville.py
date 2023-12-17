def arrival_announcement():
    print(f"you have arrived to {destination}")

def move_forward():
    print("moving forward")

def turn(direction):
    print(f"turning {direction}")

def start_engine():
    print("starting engine")

def stop_engine():
    print("stopping engine")

def follow_roundabout(exit_number):
    print(f"taking exit number {exit_number} from the roundabout")

def enter_roundabout():
    print("entering roundabout")

roundabout = ["hospital", "mall", "airport", "university", "stadium"]

start_engine()
destination = input("Where would you like your destination to be? ")

if destination == "library":
    move_forward()
    turn("left")
    arrival_announcement()
elif destination == "tech park":
    move_forward()
    turn("right")
    arrival_announcement()
elif destination in ["hospital", "mall", "airport", "university", "stadium"]:
    move_forward()
    enter_roundabout()
    exit_number = 0
    if destination == "hospital":
        exit_number = 1
        follow_roundabout(exit_number)
        arrival_announcement()
    elif destination == "mall":
        exit_number = 2
        follow_roundabout(exit_number)
        move_forward()
        turn("right")
        arrival_announcement()
    elif destination == "airport":
        exit_number = 3
        follow_roundabout(exit_number)
        arrival_announcement()
    elif destination == "university" or "stadium":
        exit_number = 4
        follow_roundabout(exit_number)
        move_forward()
        if destination == "university":
            turn("left")
            arrival_announcement()
        else:
            turn("right")
            arrival_announcement()
else:
    print("Invalid destination")

stop_engine()


    
