print("\033[1;36mROBUX PERCENTAGE CALCULATOR") # title
print("\033[1;31mMade by duckstz") # credit :)
# while true so it can repeat after you finished putting in your stuff
while True:
    print("\033") # space
    Robux = input("\033[1;32mRobux Amount:\033[1;36m ")
    Percent = input("\033[1;32mEnter \033[1;31m1 \033[1;32mor \033[1;31m2 \033[1;32mor \033[1;31m3\033[1;32m | 1 = [UGC], 2 = [Tshirt/shirt/pants/gamepasses/etc], 3 = [ROBUX TO USD]:\033[1;36m ")
    

    ChosenPercent = 0.7
    ChosenWord = "Robux after Tax Would be: "
 # chosen perecentage :)
    #UGC
    if Percent == "1":
        ChosenPercent = 0.3
    #normal
    if Percent == "2":
        ChosenPercent = 0.7
    #usd
    if Percent == "3":
        ChosenPercent = 0.0035
        ChosenWord = "Robux to USD would be: "

    #check sometime later if ChosenPercent doesnt match to 1 or 2.
    #check to see that robux is numeric
    Check = Robux.isnumeric()

    # Calculate percentage also a check to error incase yeah
    if Check:
        percentageToRobux = (float(Robux) * ChosenPercent)
        print("\033") # space"
        print("\033[1;32m",ChosenWord,f"\033[1;33m{percentageToRobux}", sep="") # this seperates and puts the right word in the place :)
    else:
        print("\033[1;31mYour input has to be numeric! Please enter a number!") # catches error and brings u back to the beginning!
