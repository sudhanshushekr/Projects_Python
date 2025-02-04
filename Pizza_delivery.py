print("Welcome to the python pizza delevery")

size = input("What is the size do you want? S,M,L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

else:
    print("Please enter the correct size")


# add based on the paparini chouce 

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M":
        bill += 3
    elif size == "L":
        bill += 3





if extra_cheese == "Y":
    bill += 1



print(f"Your final bill is {bill}")
# print(f"Your final bill is {bill}")
