#To ask the user on how many dices to be rolled, and then after the dices have been rolled, the user is asked again if you want to roll more dices.

#Imports the random and sys class.
import random,sys

#A function to ask the user on how many dices to be rolled.
def HowManyDicesToBeRolled():
    while True:
        try:
            HowManyDicesToBeRolledEntered=int(input("Please enter a number no more than 100 on how many dices would you like rolled? and then press enter."))
        except ValueError:
            print("You have not entered a number.")
            continue
        else:
            if (HowManyDicesToBeRolledEntered < 1 or HowManyDicesToBeRolledEntered > 100):
                print("You have entered " + str(HowManyDicesToBeRolledEntered))
                continue
            else:
                RollDices(HowManyDicesToBeRolledEntered)

#A function to roll the dices.
def RollDices(HowManyDicesToBeRolledEntered):
    DicesRolled=1
    while(DicesRolled<=int(HowManyDicesToBeRolledEntered)):
        Dice=random.randint(1,6)
        print('Dice ' + str(DicesRolled) + ' is ' + str(Dice))
        DicesRolled=DicesRolled+1
    RollMoreDicesQuestion()

#A function to ask the user if they would like to roll more dices.
def RollMoreDicesQuestion():
    RollMoreDices = str(input("Would you like to roll more dices? please press Y for Yes or N for No and then press enter."))
    if RollMoreDices in ('Y','y'):
        HowManyDicesToBeRolled()
    elif RollMoreDices in ('N','n'):
        input("Press any key and then press enter to exit")
        sys.exit()
    else:
        print("You have entered " + RollMoreDices + ", please enter Y for Yes or N for No and then press enter.")
        RollMoreDicesQuestion()

#Runs the HowManyDicesToBeRolled function.
HowManyDicesToBeRolled()