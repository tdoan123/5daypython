# define function
# function is similar to oepration in math 

# passing 'data' into function 
# example: round(2.5)  => passing argument/data '2.5' into function 'round' 

# Day 1 Exercise  
# Variable and  Data Type: 
# Python consists of 4 different typs 
# 1: integer
address_number = 1234
# 2: float
house_number = 12.34
# 3: string
street_name = "Victoria Street" 
# 4: boolean
house_address = False

print("address_number: ", address_number)
print("house_number: ", house_number)
print("street_name: ", street_name)
print("house_address:", house_address)

# Basic Operation and Strings: 
# Math Operation 
number_1 = 40
number_2 = 30
addition = number_1 + number_2
subtraction = number_1 - number_2
multiplication = number_1 * number_2    
division= number_1 / number_2
modulus = number_1 % number_2  # what is modulus? 
# modulus is the remainder of a division operation. 
# for example, 5 % 2 = 1, 1 is the remainder of 5 divided by 2. 

print("number_1: ", number_1)
print("number_2: ", number_2)

print("addition: ", addition)
print("subtraction: ", subtraction)
print("multiplication: ", multiplication)
print("division: ", division)
print("modulus: ", modulus)

# String Operation
string1= "Hello" 
string2= "World" 
# Concatenation 
sample_concatenation = string1 + " the " + string2
print("concatenation_sample:", sample_concatenation)

# Slicing 
sliced_start_from_begining = sample_concatenation[0:2]
print("1.sliced_sample:", sliced_start_from_begining)
sliced_start_from_ending = sample_concatenation[-4:]
print("2.sliced_sample:", sliced_start_from_ending)
slice_every_2 = sample_concatenation[::2]
print("3.sliced_sample:", slice_every_2)
slice_every_2_start_from_1 = sample_concatenation[1::2]
print("4.sliced_sample:", slice_every_2_start_from_1)
slice_in_between = sample_concatenation[1:5]
print("5.sliced_sample:", slice_in_between)
slice_reverse = sample_concatenation[::-1] 
print("6.sliced_sample:", slice_reverse)

# Methods 
# 1: upper() 
upper_string = sample_concatenation.upper()
print("upper_string:", upper_string)
# 2: lower() 
lower_string = sample_concatenation.lower()
print("lower_string:", lower_string)
# 3: len() 
length_of_string = len(sample_concatenation)
print("length_of_string:", length_of_string)
# 4: replace() 
replace_string = sample_concatenation.replace("Hello", "Hi")
print("replace_string:", replace_string)
# 5: split() 
split_string = sample_concatenation.split()
print("split_string:", split_string)
# 6: strip() # what is strip? 
# strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
strip_string = sample_concatenation.strip()
print("strip_string:", strip_string)
# 7: find() # what is find? 
# find() method returns the index of first occurrence of the substring (if found). If not found, it returns -1
find_string = sample_concatenation.find("the")
print("find_string:", find_string)
# 8: count() #what is count? 
# count() method returns the number of occurrences of a substring in the given string.
count_string = sample_concatenation.count("the")
print("count_string:", count_string)
# 9: join()  #what is join? 
# join() method takes all items in an iterable and joins them into one string.
join_string = " ".join(["Hello", "the", "World"])
print("join_string:", join_string)
# 10: startswith() # what is startswith? 
# startswith() method returns True if a string starts with the specified prefix(string). If not, it returns False.
startswith_string = sample_concatenation.startswith("Hello")
print("startswith_string:", startswith_string)
# 11: endswith() # what is endswith? 
# endswith() method returns True if a string ends with the specified suffix. If not, it returns False.
endswith_string = sample_concatenation.endswith("World123")
print("endswith_string:", endswith_string)
# 12: isalpha() # what is isalpha? 
# isalpha() method returns True if all the characters are alphabet letters (a-z).
# If not, it returns False.
isalpha_string = sample_concatenation.isalpha()
print("isalpha_string:", isalpha_string)
# 13: isnumeric() # what is isnumeric? 
# isnumeric() method returns True if all the characters are numeric (0-9). If not, it returns False.
isnumeric_string = sample_concatenation.isnumeric()
print("isnumeric_string:", isnumeric_string)
# 14: isdigit() # what is isdigit? 
# isdigit() method returns True if all the characters are digits, otherwise False.
isdigit_string = sample_concatenation.isdigit() 
print("isdigit_string:", isdigit_string)
# 15: islower() # what si islower? 
# islower() method returns True if all the characters are in lower case, otherwise False.
islower_string = sample_concatenation.islower()
print("islower_string:", islower_string)

# Lists, Tuples, and Dictionaries: 
# List 
schools = ["school1", "school2", "school3"]
print("schools:", schools)

# Tuble # what is tuple? 
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# Tuple is written with round brackets.
schools_in_tuble = ("school1", "school2", "school3")
print("schools_in_tuble:", schools_in_tuble)

numbers = (1, 2, 3, 4, 5) 
print("numbers:", numbers) 

# Dictionary 
my_house = {'address': address_number, 'house_number': house_number, 'street_name': street_name}
print("my_house:", my_house)

# List operation 
add_school = schools.append("school4")
print("add_schools:", schools)
append_school = schools.append("school5")
print("append_schools:", schools)
remove_school = schools.remove("school2")
print("remove_schools:", schools)
pop_school = schools.pop(1)
print("pop_schools:", schools)
sort_school = schools.sort() 
print("sort_schools:", schools)
reverse_school = schools.reverse()
print("reverse_schools:", schools)
count_school = schools.count("school1")
print("count_schools:", count_school)
index_school = schools.index("school1")
print("index_schools:", index_school) # why the result is 2? is it support to be 0? 

# link for sample of list operation from python documentation: 
# https://docs.python.org/3/tutorial/datastructures


# Tuple and Dictionary operation 
# Tuple and Dictionary are immutable, so there are no operation for tuple.
# link for sample of tuple and dictionary operation from python documentation:
# https://docs.python.org/3/tutorial/datastructures
# => as tuple and dictionary are immutable, there are no operation for tuple and dictionary. then how to modify the information in tuple and dictionary??? 
# => to modify the information in tuple and dictiokwnary, I have to create a new tuple/dictionary and assign the new value to the tuple/dictionary. 
# => for example: 
# => my_house = {'address': address_number, 'house_number': house_number, 'street_name': street_name}
# => my_house['house_number'] = 1234.56
# => print("my_house:", my_house)  

# Write Programs Using If-else Statements to Check Conditions   
if address_number == 12345: 
    print("address_number is 12345")
elif address_number == 1234:    
    print("address_number is 1234") 
else:   
    print("address_number is not 1234 or 12345") 
    
# Use for and while Loops to Iterate Over Sequences
# for loop
for school in schools: 
    print(school)  

# while loop 
i = 0
while i < len(schools): 
    print(schools[i])
    i += 1
# need to think of some more sample for while loop 

#search for further exercise 

    
    
    