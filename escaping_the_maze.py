# while loop 

while True:
    print("You are in a maze of twisty little passages, all alike.")
    print("Where do you want to go? (left or right)")
    direction = input(">")
    if direction == "left":
        print("You have fallen into a pit of spikes.")
        break
    elif direction == "right":
        print("You have escaped the maze.")
        break
    else:
        print("Not a valid option, try again.")
        continue
print("Game Over")
