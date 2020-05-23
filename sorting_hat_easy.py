print("=== Sorting Hat Quiz ===")
print("Welcome to Hogwarts! It's time to find out which house you belong in! For each question, please type the number of the answer you choose.\nAre you ready? Time to put on the Sorting Hat...\n")

# Create a variable to keep track of scores for each result.
gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

# Now let's write some questions!

# Q1
print("Question 1")
print("What's your favorite element?")
print("1: Fire")
print("2: Earth")
print("3: Air")
print("4: Water")

# input() prompts the user to enter an input. The input is by default a string so we need to cast it into an integer. Then we save this input in the variable 'answer'. 
answer = int(input("Answer: "))

# We can use conditionals to evaluate which result the user's answer corresponds to. We give that result a point that we will tally later.
if answer == 1:
  gryffindor += 1
elif answer == 2:
  hufflepuff += 1
elif answer == 3:
  ravenclaw += 1
elif answer == 4:
  slytherin += 1
else:
  print("Invalid answer.")
print()



# Time to report the result!

result = 'gryffindor'
max_points = gryffindor

if slytherin > max_points:
  result = 'slytherin'
if hufflepuff > max_points:
  result = 'hufflepuff'
if ravenclaw > max_points:
  result = 'ravenclaw'

print("\nAfter a long pause, the Sorting Hat cries:")
print(result + "!")
