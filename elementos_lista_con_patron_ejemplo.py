# https://www.geeksforgeeks.org/python-finding-strings-with-given-substring-in-list/
# obtener ciertos elementos de la listas a partir patron

# Python code to demonstrate
# to find strings with substrings
# using list comprehension

# initializing list
test_list = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']

# printing original list
print("The original list is : " + str(test_list))

# initializing substring
subs = 'Geek'

# using list comprehension
# to get string with substring
res = [i for i in test_list if subs in i]
