#### COLLEGE ADMISSIONS ASSIGNMENT ####
# Below are students application for UW Seattle 2020-2021
# Each list corresponds to a single student and we can find information about the student by doing:
#        list[0] = name 
#        list[1] = Cumulative GPA
#        list[2] = City Located 
#        list[3] = State Located 
#        list[4] = Major
student1 = ['emma', 3.4, 'saN Jose', 'CA', 'biology']
student2 = ['derek', 3.2, 'FremoNT', 'wa', 'communications']
student3 = ['tyler', 2.9, 'cHAPel Hill', 'nC', 'computer science']
student4 = ['liz', 4, 'new YoRK City', 'ny', 'computer engineering']
student5 = ['marie', 3.1, 'charLOTTESVILLE', 'vA', 'civil engineering']
student6 = ['JohnsoN', 3.0, 'durhAM', 'Nc', 'electrical engineering']
student7 = ['karinA', 2.1, 'daLLAs', 'tx', 'sociology']
student8 = ['LUcas', 3.5, 'HoustOn', 'tx', 'computer science']
#### DO NOT CHANGE CODE ABOVE ####





#### PART 1 ####
# Add all five students to a list called all_students

##### YOUR CODE HERE #####











# Now the UW Seattle wants to process all of the students state locations, but ignoring case. Write a series of print statements that will print each applicant's City and State. For example, for Emma we want to print 'San Jose, CA' with S and J and the state name being capitalized. Note we can get the upper case version of a string using the function string.upper() and lower case using string.lower(). See the example below:
"""
state = 'wa'
city = 'kEnT'
capitalized = city[0].upper()    # capitalized should be 'K'
lower_case = city[1:].lower()    # lower_case should be 'ent'
print('reformatted : ' + capitalized + lower_case + ', ' + state.upper())
"""

##### YOUR CODE HERE #####









# The University is complaining that the system that they used to retrieve information was broken, and the students' name, and locations. They want to clean the data, and they are asking for your help. Reformat each list to have the first letter in the name and city capitalized (everything else lowercase), both letters in the state to be upper case.
# Ex: 
# Before modifying list student1 = ['emma', 3.4, 'saN Jose', 'CA', 'biology']
# After modifying list student1 = ['Emma', 3.4, 'San Jose', 'CA', 'biology']

##### YOUR CODE HERE #####












#### PART 2 ####
# Now that we have cleaned up our lists, we can print the output for the University. But UW Seattle is strictly not admitting students who are interested in Computer Science, because they have limited capacity, and also students with lower than a 3.0 GPA. Therefore use conditions to filter out students who don't meet the requirements. The report will be a series of print statements that state:

# Accepted: StudentName from City, State is interested in studying MajorName, so she is admitted to the University
#
# OR 
#
# Rejected: StudentName from City, State is interested in studying MajorName, but she does not meet the qualifications.
#
#
# For example, if we looked at the list student1, we would print:
# 'Emma from San Jose, WA is interested in studying Biology, so she is admitted to the University.







