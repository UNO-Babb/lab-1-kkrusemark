#MadLib.py
#Name: Kylie Krusemark
#Date: 8/25/25
#Assignment: Lab 1
#Purpose: To ask a user for words, and print a story with the supplied words

def main():
  print("Madlib")
  #Ask user for words
print("Hello! I'd like your help writing a story.")
PlaceName = input("Give me a place name: ")
creature = input("Give me a creature: ")
verb1 = input("Give me a verb: ")
noun1 = input("Give me a noun (plural): ")
adjective = input("Give me an adjective: ")
food = input("Give me a food: ")

  #Print the story with the user supplied words.s
print("Long, long ago in a village called,", PlaceName, "there was a", creature, "on the loose.")
print("The", creature, "was causing much trouble because it kept", verb1 + "ing", noun1 + ".") 
print("Now this was a problem because", PlaceName, "had very few", noun1 + ".")
print("To fix their problem, a brave man caught the", creature, "and called it", adjective + ".")
print("This surprised the", creature + ", and it stopped", verb1 + "ing", noun1 + ".") 
print("To celebrate, the villagers had a large feast of", food + ". The end!")

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
