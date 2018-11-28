# x = [ [5,2,3], [15,8,9] ] 
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Bryant'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Andres', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 30} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30


# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through 
# each dictionary in the list and prints each key and the associated value. For example, given the following list:  

# iterateDictionary(students) 
# # should output: (it's okay if these pairs end up on separate lines; bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
# def iterateDictionary(s):
#     for num in range(0,len(s),1):
#             print (f"first_name - {s[num]['first_name']}, last_name - {s[num]['last_name']}")

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# iterateDictionary(students)

# def iterateDictionary2(key_name, some_list):
#     for num in range(0, len(some_list), 1):
#         print(f"{some_list[num][key_name]}")

# iterateDictionary2('last_name',students)

# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def printInfo(my_Dict):
#     for k in my_Dict:
#         print(f"{(len(my_Dict[k]))} {k.upper()} ")
#         for num in range(len(my_Dict[k])):
#             print(f"{my_Dict[k][num]}")
# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


