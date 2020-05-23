print("=== Sorting Hat Quiz ===")
print("Welcome to Hogwarts! It's time to find out which house you belong in! For each question, please type the number of the answer you choose.\nAre you ready? Time to put on the Sorting Hat...\n")

# Create a variable to keep track of scores for each result.
# gryffindor = 0
# hufflepuff = 0
# ravenclaw = 0
# slytherin = 0

# Create a list containing each result of the quiz.
results = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

# Create a list 'tallies' that will keep score of each result. This list should be the same length as the 'results' list. Each entry in 'tallies' will keep score for the result with the same index in 'results'.
tallies = [0] * len(results)

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

# Add a point in 'tallies' for the result that corresponds to the user's answer. Remember that list indexing starts at 0. 
tallies[answer - 1] += 1

# We can use conditionals to evaluate which result the user's answer corresponds to. We give that result a point that we will tally later.
# if answer == 1:
#   gryffindor += 1
# elif answer == 2:
#   hufflepuff += 1
# elif answer == 3:
#   ravenclaw += 1
# elif answer == 4:
#   slytherin += 1
# else:
#   print("Invalid answer.")
# print()

# Your turn! Create some questions of your own using Q1 as an example!
# ...


# Time to report the result!

# This line finds the index of the maximum score in 'tallies' (if two scores are tied, it takes the first one in the list). Then it finds the value with the corresponding index in 'results' and stores it in the variable 'result'.
result = results[tallies.index(max(tallies))]

print("\nAfter a long pause, the Sorting Hat cries:")
print(result + "!")
