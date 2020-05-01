import math

robotX = 0
robotY = 0
movement = 0
distance = 0
moving = True

while moving:
    choice = input("\nEnter to move, UP, DOWN, LEFT, RIGHT or CALC: ")
    if choice == "UP":
        print("\nCurrent Location: ", robotX, ",", robotY)
        movement = int(input("Enter number of steps to move up: "))
        robotY = robotY + movement
        print("New Location: ", robotX, ",", robotY)
    elif choice == "DOWN":
        print("\nCurrent Location: ", robotX, ",", robotY)
        movement = int(input("Enter number of steps to move down: "))
        robotY = robotY - movement
        print("New Location: ", robotX, ",", robotY)
    elif choice == "LEFT":
        print("\nCurrent Location: ", robotX, ",", robotY)
        movement = int(input("Enter number of steps to move left: "))
        robotX = robotX + movement
        print("New Location: ", robotX, ",", robotY)
    elif choice == "RIGHT":
        print("\nCurrent Location: ", robotX, ",", robotY)
        movement = int(input("Enter number of steps to move right: "))
        robotX = robotX + movement
        print("New Location: ", robotX, ",", robotY)
    elif choice == "CALC":
            distance = math.sqrt(robotX**2 + robotY**2)
            print("\nDistance from start: ", int(distance))
