# Mad Libs Game - Fill in the blanks with user input

print("Welcome to the Mad Libs Game! 🎭")
print("Fill in the blanks to create a fun story!\n")


name = input("Enter a name: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb: ")
place = input("Enter a place: ")
noun = input("Enter a noun: ")


story = f"""
Once upon a time, {name} went on an adventure to {place}. 
It was a {adjective} day, and everything seemed perfect. 
Suddenly, {name} decided to {verb} a {noun}. 
It was the best decision ever, and the adventure turned into an unforgettable memory!
"""


print("\n--- Here is your Mad Libs story! ---\n")
print(story)
print("Hope you enjoyed the game! 😊")
