userInput = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right" ')

if userInput == "left":
    userInput= input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ')

    if userInput == "wait":
        userInput = input("You arrive at theisland unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")

        if userInput == "red":
            print("It's a room full of fire. Game Over.")

        elif userInput == "blue":
            print("You enter a room of beasts. Game Over.")

        elif userInput == "yellow":
            print("You found the treasure! You Win!")

        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")