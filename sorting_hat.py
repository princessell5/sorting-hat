
#### PART 1: Introduction ####
print("=== Sorting Hat Quiz ===")
print("Welcome to Hogwarts! It's time to find out which house you belong in! For each question, please type the number of the answer you choose.\nAre you ready? Time to put on the Sorting Hat...\n")

# Create a list containing each result of the quiz.
results = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

# Create a list 'tallies' that will keep score of each result. This list should be the same length as the 'results' list. Each entry in 'tallies' will keep score for the result with the same index in 'results'.
tallies = [0] * len(results)

# QUESTION 1
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



#### PART 2: Add Questions ####
# Now let's write some questions! Make sure your answer choices are either 1, 2, 3, or 4 so it will be added to your tallies list.

# QUESTION 2
#### YOUR CODE HERE ###







answer = int(input("Answer: "))
tallies[answer - 1] += 1

# QUESTION 3
#### YOUR CODE HERE ###







answer = int(input("Answer: "))
tallies[answer - 1] += 1

# QUESTION 4
#### YOUR CODE HERE ###







answer = int(input("Answer: "))
tallies[answer - 1] += 1

# QUESTION 5
#### YOUR CODE HERE ###







answer = int(input("Answer: "))
tallies[answer - 1] += 1



### PART 3: Report the result ####
# This line finds the index of the maximum score in 'tallies' (if two scores are tied, it takes the first one in the list). Then it finds the value with the corresponding index in 'results' and stores it in the variable 'result'.
max_number_from_talliest = max(tallies)
index_of_max_num = tallies.index(max_number_from_talliest)
result = results[index_of_max_num]

print("\nAfter a long pause, the Sorting Hat cries:")
print(result + "!")
