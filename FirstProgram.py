#FirstProgram.py 
#Name: Kylie Krusemark
#Date: 8/25/25
#Assignment: Lab 1
#Purpose: To ask a user for their name, and calculate their birth year.

from datetime import datetime

def main():
  print("First Program")
  #Say hello
  print("Hello!")

  #Ask for the user's name
  name = input("What is your name? ")

  #Use the user's name in the program.
  print("Nice to meet you",name)

  #Ask the user for their age.
  age = int(input("How old are you? (#): "))

  #Tell the user what year they were born in.
  #Assume that they have not had their birthday yet this year.
  current = datetime.now()
  CurrentYear = current.year
  BirthYear = CurrentYear - age - 1
  print("You were born in",BirthYear)

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
