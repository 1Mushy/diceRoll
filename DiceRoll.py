"""
Made by Jack Baker and Jed Gascho
=D
A random program for rolling large amounts of dice, because thats what America needs.
"""


#random number importations
from numpy import random

#graph stuff, in beta

#import sys
#import matplotlib
#matplotlib.use('Agg')
#import matplotlib.pyplot as plt


#defining things
diceSide = "Waffles"
#claiming our code XD
print("---------------------\nDice Roller \nMade by Jed and Jack\n---------------------\nPlease install Numpy 1.19.3 (this version is crucial) on your system for this program to work\nRead comments to find how to install Numpy 1.19.3\n---------------------")

#Commands listed below are ways to install Numpy 1.19.3

#pip install numpy==1.19.3
#python -m pip install numpy--1.19.3


#checking to see if user input is integer; pertaining to the dice sides
while True:
 diceSide = input("Enter the number of sides of the dice you would like to roll: ")
 try:
    intCheck = int(diceSide)
    int(diceSide)
    break
 except ValueError:
    print("Only an integer please!")


#checking to see if user input is integer; pertaining to the amount of times the dice should be rolled
while True:
 diceRollCount = input("Enter the times you would like the dice to be rolled: ")
 try:
   intCheckRollCount = int(diceRollCount)
   int(diceRollCount)
   break
 except ValueError:
    print("Only an integer please!")


#define the array to store the variables in
diceOutput = [] 

#repeat this the amount of times; one repeat = one roll
for waffle in range(int(diceRollCount)):
  diceRandomOutput = random.randint(1,int(diceSide)+1)
  #get a random number in the range of the dice
  
  #print(diceRandomOutput) #print the number if desired. DO NOT ENABLE ITS TOXIC
  diceOutput.append(diceRandomOutput) # and append it to the array
else: # once its finished
 print("I rolled your dice with " + str(diceSide) + " sides for you " + str(diceRollCount) + " times!")
 
 #sorts the results
 diceOutput.sort()

 #prints the results
 print("Here are the results: \n" + str(diceOutput))
 print("Here are your numbers all added up: " + str(sum(diceOutput)))


#add space
 print("")
 print("")

#keeps window open
 input("Press enter to close...")

 #graph stuff, beta for now

 #plt.hist(diceOutput)
 #plt.show()
 #plt.savefig(sys.stdout.buffer)
 #sys.stdout.flush()
