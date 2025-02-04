print('''         
             ...                            
             ;::::;                           
           ;::::; :;                          
         ;:::::'   :;                         
        ;:::::;     ;.                        
       ,:::::'       ;           OOO\         
       ::::::;       ;          OOOOO\        
       ;:::::;       ;         OOOOOOOO       
      ,;::::::;     ;'         / OOOOOOO      
    ;:::::::::`. ,,,;.        /  / DOOOOOO    
  .';:::::::::::::::::;,     /  /     DOOOO   
 ,::::::;::::::;;;;::::;,   /  /        DOOO  
;`::::::`'::::::;;;::::: ,#/  /          DOOO 
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O 
  `:::::`::::::::;' /  / `:#                  
   ::::::`:::::;'  /  /   `#              
''')

print("-----------------------Welcome to the Treasure Hunt Game!!------------------")

print("Your mission is to find the treasure.")

choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right": ').lower()

if choice1 == 'left':
    choice2 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat or "swim" to swim across: ').lower()
    
    if choice2 == 'wait':
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors: one red, one yellow, and one blue. Which color do you choose? ").lower()
        
        if choice3 == 'red':
            print("It's a room full of fire. Game Over.")

        elif choice3 == 'yellow':
            print("You found the treasure! You Win!")

        elif choice3 == 'blue':
            print("You enter a room of beasts. Game Over.")

        else:
            print("You chose a door that doesn't exist. Game Over.")

    else:
        print("You got attacked by angry trout. Game Over!")

else:
    print("You fall into a hole. Game Over!")
