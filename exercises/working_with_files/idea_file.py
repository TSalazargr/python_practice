import random

def add_idea():
  f = open("ideas.txt", "a")
  idea = input("Write your idea down here: ")
  f.write(f"{idea}\n")
  print("Nice! Your idea has been stored!")
  f.close()

def load_idea():
  f = open("ideas.txt", "r")
  ideas = f.read().split("\n")
  f.close()
  ideas.remove("")
  if ideas: # Checks if there any ideas in the variable
    print(random.choice(ideas))
  else:
    print("No ideas found. Add some ideas first.")

while True:
  option = input("Would you like to (A)dd an idea  or (L)oad a random idea (L)?: A/L ").upper().strip()
  while option != "A" and option != "L":
      option = input("I couldn't understand the command. Try again. Would you like to add an idea (A) or load a random idea (L)?: A/L").upper().strip()
  if option == "A":
    add_idea()
  elif option == "L":
    load_idea()


    
