# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

# def biggie_size(a):
#     for num in range(0,len(a),1):
#         if a[num] > 0:
#             a[num] = "big"
#     print(a)
# biggie_size([-1, 3, 5, -5])

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

# def count_positives(a):
#     count = 0 
#     for num in range(0, len(a) ,1):
#         if a[num] > 0:
#             count += 1
#     a[len(a)-1] = count
#     return a
# print(count_positives([1,6,-4,-2,-7,-2]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

# def sum_total(a):
#     sum = 0
#     for num in range(0, len(a), 1):
#         sum += a[num]
#     return sum
# print (sum_total([6,3,-2]))

# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

# def average(a):
#     sum = 0
#     for num in range(0,len(a), 1):
#         sum += a[num]
#     return sum/len(a)
# print (average([1,2,3,4]))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

# def length(a):
#     return len(a)

# print(length([37,2,1,-9]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

# def minimum(a):
#     if len(a) == 0:
#         return False
#     min = a[0]
#     for num in range(0, len(a), 1):
#         if a[num] < min:
#             min = a[num]
#     return min 
# print(minimum([37,2,1,-9]))
# print(minimum([]))

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return 0

# def maximum(a):
#     if len(a) == 0:
#         return False
#     max = a[0]
#     for num in range(0,len(a),1):
#         if a[num] > max:
#             max = a[num]
#     return max
# print(maximum([37,2,1,-9]))
# print(maximum([]))


# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(a):
    mydict = {'sumTotal': 0, 'average':0, 'minimum':0, 'maximum':0, 'length':0}
    for num in range(0,len(a),1):
        mydict['sumTotal'] += a[num]
        mydict['length'] = len(a)
        if mydict['minimum'] > a[num]:
            mydict['minimum'] = a[num]
        if mydict['maximum'] < a[num]:
            mydict['maximum'] = a[num]
    mydict['average'] = mydict['sumTotal']/mydict['length']
    return mydict
print(ultimate_analysis([37,2,1,-9]))


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. 
# (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

# def reverse_list(a):
#     temp = 0
#     count = 0
#     for num in range(0,(len(a)-1)//2, 1):
#         temp= a[num] 
#         a[num] = a[(len(a)-1)-count]
#         a[(len(a)-1)-count] = temp
#         count += 1 
#     return a


# print (reverse_list([37,2,1,-9]))