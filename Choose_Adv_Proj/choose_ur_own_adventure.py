name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirtroad, it has come to an end and you can go left or right. Which way would you like to go?").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. Type 'walk' to walk around or 'swim' to swim across: ")

    if answer == "swim":
        print("You swam across and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water, and lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back?(cross/back)")

    if answer == "back":
        print("YOu go back and lose :(")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? Type 'yes' or 'no': ")

        if answer == "yes":
            print("You talk to the stranger and they give you gold. YOU WIN!")
        elif answer == "no":
            print("You ignore the stranger which offends them so they kill you. You lose :( ")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for playing", name)