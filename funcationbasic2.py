# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.

# def countDown(num):
#     arr = []
#     while num >= 0:
#         arr.append(num)
#         num -= 1
#     print(arr)
# countDown(5)

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

# def first_plus_length(a):
#     for i in a:
#         return a[0] + (len(a))

# x = first_plus_length([1,2,3,4,5])
# print(x)        

# Values Greater than Second - Write a function that accepts a list and creates a new list 
# containing only the values from the original list that are greater than its 2nd value.
# Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

# def values_greater_than_second(a):
#     newa = []
#     for num in range(0, len(a), 1): 
#         if (a[num]> a[1]):
#             newa.append(a[num])
#     print(len(newa))
#     return newa
# print (values_greater_than_second([5,2,3,2,1,4]))


# This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]
# def length_and_value(size,value):
#     newlist = []
#     while len(newlist) < size:
#         newlist.append(value)
#     return newlist

# print (length_and_value(6,2))
