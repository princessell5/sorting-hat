#### COLLEGE ADMISSIONS ASSIGNMENT ####
# Below are student's applications for UW Seattle 2020-2021
# Each list corresponds to a single student and we can find information about the student by doing:
#        list[0] = name 
#        list[1] = Cumulative GPA
#        list[2] = City Located 
#        list[3] = State Located 
#        list[4] = Major
emma = ['emma', 3.4, 'saN Jose', 'CA', 'biology']
derek = ['derek', 3.2, 'FremoNT', 'wa', 'communications']
tyler = ['tyler', 2.9, 'cHAPel Hill', 'nC', 'computer science']
karina = ['karinA', 2.1, 'daLLAs', 'tx', 'sociology']
lucas = ['LUcas', 3.5, 'HoustOn', 'tx', 'computer science']

# Each set corresponds to a single student and their classes:

emma_classes = {'AP Chemistry', 'AP Biology', 'English'}
derek_classes = {'AP Physics', 'Teaching Academy', 'Creative Writing'}
tyler_classes = {'AP Computer Science', 'Nanotechnology', 'Cisco'}
karina_classes = {'Biology', 'AP Art History'}
lucas_classes = {'AP Computer Science', 'AP Psychology'}

#### DO NOT CHANGE CODE ABOVE ####


#### PART 1 ####
# Add all five students to a list called all_students
# Tip: Look at the Python Cheat Sheet for a function to do this!

##### YOUR CODE HERE #####


















#### PART 2 ####
# Now the UW Seattle wants to process all of the students locations. Edit each student's city & state from their own list (for ex. Emma's list is emma) & save them to their own variable (for example: Emma's city & state can be in the variable emma_city & emma_state). 
# To process all of the student's locations, we want to for example, print 'San Jose, CA' with S and J and the state name acronym being capitalized for Emma's location. Essentially for the city, we want the first letter capitalized and the rest would be lowercase. For the the acronym of the state, we want all letters to be capitalized. 
# NOTE: We can get the upper case version of a string using the function string.upper() and lower case using string.lower(). See the example below:

""" 
# Uncomment this code (the 3-chained quotations) & run it!
state = 'wa'
city = 'kEnT'
capitalized_city = city[0].upper()    # capitalized should be 'K'
captialized_city_rest = city[1:].lower()    # lower_case should be 'ent'
print('reformatted : ' + capitalized_city + captialized_city_rest + ', ' + state.upper())
"""

##### YOUR CODE HERE #####
















 



#### PART 3 ####
# The University is complaining that the system that they used to retrieve information was broken and even the students' names are unformatted. They want to clean the data, and they are asking for your help. Reformat each list to have the first letter in the name & city capitalized (everything else lowercase), both letters in the state to be upper case.You can use your previous city & state variables to make this part easier!
# Ex: 
# Before modifying list student1 = ['emma', 3.4, 'saN Jose', 'CA', 'biology']
# After modifying list student1 = ['Emma', 3.4, 'San Jose', 'CA', 'biology']

##### YOUR CODE HERE #####



















#### PART 4 ####
# Let's try modifying the classes of each student's schedules contained in sets:
# 1) Add 'AP Biology', 'AP American Literature', & 'Racquet Sports' to Emma's classes
# 2) Remove 'Teaching Academy' from Derek's classes & add 'Basketball' to Derek's classes
# 3) Remove 'AP Computer Science' from Tyler's classes & add 'Cisco'
# 4) Add 'Chemistry' & 'Biology' to Karina's classes
# 5) Add 'Health', 'AP US History', & 'AP Psychology' to Lucas's classes
# For 1)-5), predict the length of each set after making these changes. Then, print out these sets along with their lengths with (for Emma's example): print(emma_classes, len(emma_classes))
# Was the elements in the set & their lengths what you expected to be printed after modifying them? Explain why your elements & length was printed this way. How is a set different from a list? (Write your answer as a comment below)

##### YOUR CODE HERE #####

















#### PART 5 ####
# Now that we have cleaned up our lists, we can print the output for the University. But UW Seattle is strictly not admitting students who are interested in Computer Science, because they have limited capacity, and also students with lower than a 3.0 GPA. Therefore use conditions to filter out students who don't meet the requirements. The report will be a series of print statements that state:

# Accepted: StudentName from City, State is interested in studying MajorName with a GPA of higher than or equal to a 3.0, so she is admitted to the University.
#
# OR 
#
# Rejected: StudentName from City, State is interested in studying MajorName, with a GPA of lower than or equal to a 3.0, so she does not meet the qualifications.
#
#
# For example, if we looked at the list student1, we would print:
# Accepted: Emma from San Jose, CA is interested in studying biology with a GPA of higher than or equal to a 3.0, so she is admitted to the University.

##### YOUR CODE HERE #####















