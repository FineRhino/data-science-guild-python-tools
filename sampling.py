# Python3 program to demonstrate
# the use of sample() function
# See https://www.geeksforgeeks.org/python-random-sample-function/

# import random
from random import sample

# Prints list of random items of given length
list1 = [1, 2, 3, 4, 5, 6, 7, 89, 101, 3000, 291859, 23, 43, 67, 87, 98, 120]

print (sample(list1,3))

# Prints list of random items of
# length 4 from the given string.
string = "GeeksforGeeks"
print("With string:", sample(string, 4))

# Prints list of random items of
# length 4 from the given tuple.
tuple1 = ("ankit", "geeks", "computer", "science",
          "portal", "scientist", "btech")
print("With tuple:", sample(tuple1, 4))


# Prints list of random items of
# length 3 from the given set.
set1 = {"a", "b", "c", "d", "e"}
print("With set:", sample(set1, 3))