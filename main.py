
answer = input ("What you like to play ?(yes/no)")

if answer.lower().strip() == "yes":

    answer = input("you reahed a crossroads , would you like to left or right").lower().strip()
    if answer == "left" :
        answer == input("You encounter a monster , would you like to run or attcak.")

        if answer == "attack" :
            print("The was not a great idea , you lost")
        else :
            print ("Good choice you made it away  safely")

            answer = input("You see a car and a plane .Which would you like to take (car/plane)")
            if answer == "plane ":
                print ("Unfortunately you don't know how to fly ... Game Over")
            else:
                print(" You won !")

    elif answer == "right":
        print("You walked aimlesly to the right and fall on the patch of ice.You injjures your leg and cannot continue .Game Over ! ")
    else :
        print ("Invalid choise, you left")
else :
    print ("That's to bad")

