
# exercise 1 
"""
Ask the user what today's weather is
And then:
(1) If it's rain or snow -- print something negative
(2) If it's sun -- print something positive
(3) If it's neither -- print that you don't know what it is
"""

user_input = input("what todays weather is?")
if (user_input == "rain" or 
    user_input == "snow"): 
    print ("what is so suck! I miss the sun")
elif user_input == "sunny":
    print ("what is so nice! I enjoy the sun so much")
else:  
    print ("I dont know what " + user_input + " is")
    
    
x = None

type(x)

# Everthing in Python, in a boolean context, is True 
# except:..........
# - False 
# - None 
# - 0 
# - anything empty  

name = input('enter your name: ')
if name != '':
    print('Hello, ' + name)
else:
    print('hey! you didnt enter a name')
    
name = input('enter your name: ')
if name: # name is a string... non empty strings are True in a boolean context 
    print('Hello, ' + name)
else:
    print('hey! you didnt enter a name')
    
name = input('enter your name: ')
if not name: # name is a string... empty strings are False in a boolean context 
    print ('hey! you didnt enter a name')
else:
    print('Hello, ' + name) 
    
'''
interger 
'''    
x = 10 
y = 3 
x + y 
x - y 
x * y
x / y # always return float 
x // y # return interger  
x ** y  # x to the y power 
x % y  # modulus --- remainder after taking x/y  
 
x = x + 1 # right executed first then left.   
x += 1  as 

x > y 
x < y 
x >= y 
x <= y 
x != y 

x = 10 
y = x 
x = 20 
y 

y = '2'
type(y)

y = int(y)
type(y)

#0x => hex number 
#0b => oct number  
#0o => binary number

s = 'abcd' 
type (s)

print(s)
s 
len(s)

x = 'abcd'
y = 'efgh'
x + y 

len(x + y)

print('Hello')

print ('0' * 60)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
len(alphabet)


alphabet[25]
alphabet[6] = '3'
# strings are immutable 

s = 'abc\nasdf'
print(s)
len(s)
s

s = 'abc\tedh\tasdfsad'  #create a space 
print(s)

alphabet[::]

# exercise 3 
"""
Pig Latin: 
- to translate a word from english into Pig Latin
(1) of the first leter is a vowel -- a,e,i,o or u then add 'way' into the end of the word
- elephant -> elepahntway
- octopus -> octopusway 
- elegant -> elgantway 

(2) if the first letter is *not* a vowel, then move the first letter to the end of the word, and add "ay" 
- computer -> omputercay 
- table -> abletay 
- microphone -> icrophonemay   

(3) ask the user to enter one word in english  - no punctuation, no capital letters  
(4) and print the translation into Pig Latin  
"""

english = input('input english to translate, do not use punctuation and no capital letters: ')
vowel = ['a', 'e', 'i', 'o', 'u']
if vowel == english[0]:
    pig_latin = english + 'way'
    print('Pig Latin: ', pig_latin)
    
else: 
    pig_latin = english[1:] + english[0] + 'ay'
    print('Pig Latin: ', pig_latin) 
    
# FUNCTION(DATA)
# DATA.METHOD()
alphabet.upper()




'''
exercise 1: ask for user input nummber 
ask for user name: 
=> print the user name with the number of time they input in the system 
'''

number_print = int(input("how many time you want your name to be printed?; "))
user_name = input('What is your name?: ')
for number in range(number_print):
    print (user_name)

'''
exercise 2: ask for the user name, print out their name following the tree format, untill the user name is fully printed
'''
user_name = input('What is your name?: ')
name = ''  
for letter in user_name: 
    name += letter 
    print (name)
    
# why when I put the variable 'name' inside the for loop, the output only print each letter per row, rather than creating a tree like this solution  
user_name = input('What is your name?: ')
for letter in range(len(user_name)):
    print(user_name[: letter + 1])
    

'''

exercise: 42 
ask a users to enter a bunch of nummber until user input <enter> (i.e empty string).backend: do the sum and average, then return the sum and average result
'''


'''while True: 
    numbers = int(input('tell me a number in your head: '))
    number_input = []
    number_input.append(number)    
    print(number_input)
    '''
# the code above generate out the outcome for 4
'''
[4]
[4]
'''

#while True: 
#    numbers = int(input('tell me a number in your head: '))
#    store_number = []
#    store_number.append(numbers)
    
    
store_number = []
#numbers = int(input('tell me a number in your head: '))
#store_number.append(numbers)
while True:
    numbers = int(input('tell me a number in your head: '))
    store_number.append(numbers)
    total = float(sum(store_number))
    average = total / len(store_number)
    print(f'input value= {store_number}')
    print(f'total input = {total}')
    print(f'average input = {average:.2f}')    
    if not numbers: 
        break 

# get to this point so far, yet the part that Im missing is how to use break, => when user press enter, the output will show the result, instead of it is showing each time like currently I have 

store_number = []
while True:
    numbers = int(input('tell me a number in your head: '))
    if not number: 
        break 
    
store_number.append(numbers)
total = float(sum(store_number))
average = total / len(store_number)
    
print(f'input value= {store_number}')
print(f'total input = {total}')
print(f'average input = {average:.2f}')   
# why the output does not calculate and return the function?  

# I think the reason is because the system report an error from the code, that's why it stop, and not execute the codeline below 
'''  
{
	"name": "ValueError",
	"message": "invalid literal for int() with base 10: ''",
	"stack": "---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In[64], line 3
      1 store_number = []
      2 while True:
----> 3     numbers = int(input('tell me a number in your head: '))
      4     if not number: 
      5         break 

ValueError: invalid literal for int() with base 10: ''"
}
'''

# exercise 51 
"""
Pig Latin: 
- to translate a word from english into Pig Latin
(1) of the first leter is a vowel -- a,e,i,o or u then add 'way' into the end of the word
- elephant -> elepahntway
- octopus -> octopusway 
- elegant -> elgantway 

(2) if the first letter is *not* a vowel, then move the first letter to the end of the word, and add "ay" 
- computer -> omputercay 
- table -> abletay 
- microphone -> icrophonemay   

(3) ask the user to enter one word in english  - no punctuation, no capital letters  
(4) and print the translation into Pig Latin  

=> now try the full sentence 
"""

word = input('Enter a word: ')
if word[0] in 'aeiou':
    print (word + 'way')
else: 
    print (word[1:] + word[0] + 'ay')


sentence = input('Enter a sentence: ')
list = sentence.split()
print(sentence)
print(list)
new_sentence = []
for word in list: 
    if word[0] in 'aeiou':
        new_word = word + 'way'
        new_sentence += [new_word]
    else: 
        new_word = word[1:] + word[0] + 'ay'
        new_sentence += [new_word]

new_sentence_list = ' '.join(map(str,new_sentence)) # use map() method 

print(new_sentence)    
print(new_sentence_list)

# for different method, check out the following link 
# https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/


sentence = input('Enter a sentence: ')
list = sentence.split()
print(sentence)
print(list)
new_sentence = []
for word in list: 
    if word[0] in 'aeiou':
        new_sentence.append(word + 'way')
    else: 
        new_sentence.append(word[1:] + word[0] + 'ay')
    
print(' '.join(new_sentence))    

# review this code 


list = [10, 20, 13, 4]
list.sort()

# tuples 
# tuples: immutable, contain anyting

t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
type(t)
t[9]

t[2:8:3]

for one_time in t: 
    print (one_time, end=',')
    
t = ('abc','def', 'ghi', 'jkl')
for one_time in t: 
    print (one_time)
    
book1 = ('title1', 10.99)
book2 = ('title2', 15.50)

book1[1]
'ghi' in t

'g' in t 

# tuples are immutable 

# constant is different with immutable   

sum([10,20,30,40,50])
# tuple is more much more memories efficient  

t = t + t
t

t += t 
t

t = (10, 20 , 30 )
type(t)

t = 10, 20, 30 

t = (10) 
type(t)
# int
# the reason is because () is acting as cover, similar to the way that doing () for math 
# to make the tuple 
t = (10,) # comma means: Im a tuple 
type(t)

# unpacking 
# three different types of sequences: string, list, tuple
mylist = [10, 20, 30]
x = mylist  
x

x, y, z = mylist 
x
y
z

t = (100, 200, 300)
x, y, z = t
x
y
z

title, price = book1
title    
price

x = 100
y = 200 

y, x = x, y 
x
y


s = 'abc'
for one_item in enumerate(s):
    print(one_item)

'''
(0, 'a')
(1, 'b')
(2, 'c')
'''

s = 'abc'
for index, one_letter in enumerate(s):
    print(f'{index}: {one_letter}')
'''
0: a
1: b
2: c
'''    

# converting to-from tuples 
s = 'abcd'
list(s) # turn the element of string 's' into a list, list run a for loop of s, then put into a list 
tuple(s)

mylist= [10, 20, 30, 40]
tuple(mylist)
# tuple run a for loop in my list then put the elements into it own tuple

list(t) # turn a tuple from list  

t = ('abc', 'def', 'ghi')
'***'.join(t)
# join() is a string method, not a list method because we can actual pass any sequent of string to join and it will work 

# 60: sorting tuples 

t = (30, 20, 40, 10, 7, 15)
t.sort()

sorted(t, reverse=False)
# this sorted is a build in function rather than a method 
mylist = [(5,3), (5,2), (4,8), (4,6)]
sorted(mylist)


# 61 - exercise - People 
'''
ask the user, repeatly, to enter a person's name (first name + space + lastname)
Thinh Doan 
Create a list of tuples in which each tuple has 2 elements 
- last name
- first name 

[('thinh', 'doan'), ('last2', 'first2'), ('last3', 'first3')]
- print the people's name, last name first (as a phone book), sorted by last name  
- when they enter an empty string instead of a name, stop asking and print the name
- if they enter a string without any space, scold them a bit
'''
phone_book = []
while True: 
    user_name = input('your first and last name is (first name + space + last name)').strip()
    if not user_name:
        break
    if ' ' not in user_name: # damn it, why didnt I think about this one before :) 
        print('hey follow through instruction')
#    if user_name[-1] != ' ': # what is the better way to check on this?  
#        print('hey not correct')
    else: 
        user_name2 = tuple(user_name.split(' '))
        phone_book.append(user_name2)
        print (user_name)
        print (user_name2)
print(phone_book)    
# the codeline above does not sort the last name in order  

phone_book = []
while True: 
    user_name = input('your first and last name is (first name + space + last name)').strip()
    if not user_name:
        break
    if ' ' not in user_name: # damn it, why didnt I think about this one before :) 
        print('hey follow through instruction')
#    if user_name[-1] != ' ': # what is the better way to check on this?  
#        print('hey not correct')
    first_name, last_name = user_name.split()
    phone_book.append((last_name, first_name))

for last_name, first_name in sorted(phone_book):
    print(f'{last_name}, {first_name}')


# section 7: Dictionaries 
# 63: intro to dictionaries 

d = {} # emply dict with curly braces 
d[100] = 10
d[200] = 20
d[500] = 30
len(d)
 
d[100]
d[200]
# {100: 10, 200: 20, 500: 30}
# key:value format 
d = {100:10, 205:20, 315:30}
d
d[4567] = 40
d
# add new key and value 
d[4567] = 99
d
# keys in dictionary is unquie. the only changes are the values of the keys  
# can be use any immutable type
d = {'a':1, 'b':2, 'c':3}
d['a']
# search on used for the keys and has to be exact 
 
# exercise 8: restaurant 
'''
create a dict containing a restaurant menu.
the item will be the dict keys. 
the prices will be the dict values 

ask the user (customer) repeatly what they want to order  


(1) if they give us an empty string, stop asking and give the total bill 
(2) if they ask for something that 'is' on the menu. say how much it costs and add it to the total - and have them order something else.  
(3) if they ask for something that is *not* on the menu, then tell them dotnt carry this product, and have them try again. 
'''

# creat a dictionary of meny and prices 
# ask for menu function 
# search for the respons 
    # if menu is in the dictionary, sum and add up 
    # if menu is not, tell them you dont have today  
# generate summary of order and total amount  

menu = {'sandwich': 10, 
        'coffee': 15,
        'salad': 8}
total = 0
while True:
     user_input = input('What can i serve you today? ').strip()
     if not user_input: 
         break
     if user_input in menu: 
        total += menu[user_input]
        print (f'{user_input} is {menu[user_input]}, total is {total}')
     if user_input not in menu:
        print (f'we do not serve {user_input} today')
print (f'Total is {total}')         
# hey so happy that I constaintly solving all the exercise by mysele :) 
# the solution, he was using else if and else: which is different than mine. review to understand the differences and rationale  

# 66: get and set default 
d
d['a']
d['z']
d.get('a')
d.get('z', 'no such key')
# d.get() is equivalent to d[] the difference is it does not return valueerror, rather it allows on option to return value in the event that no such key found 

# I want to add the key value pair 'x:5' but only if 'x' is not currently in d
# setdefault -- takes a key and value
# - if the key exits, it return the current value 
# - if the key does NOT exit, it adds the key value-pair and return the value 

d.setdefault('x',100)
d.setdefault('y',500)
d

s = 'abcd'
for one_item in s: 
    print (one_item)
    
for one_item in d: 
    print (one_item)
    
d.keys()

d.values()
for one_item in d.values():  
    print (one_item)

'''
1
2
3
100
500
'''

d.items() # return key value pair in tuples format: 
d.items()

for one_item in d.items():  
    print (one_item)
'''
('a', 1)
('b', 2)
('c', 3)
('x', 100)
('y', 500)
'''    

for key, value in d.items():
    print (f'{key}={value}')
'''
unpack the key and value of the dictionary 
a=1
b=2
c=3
x=100
y=500
'''

# 68: Exercise 9: rainfall
'''
ask user two questions? 
first question: what city? 
second question: how much rain fell there?  
mm of rain 
''' 

rain_dict = {}

while True:  
    city = input('what city? ').strip()
    if not city: 
        break 
    else: 
        rain = int(input('how much rain fell there yesterday? ')) 
        if city in rain_dict: 
            rain_dict[city] += rain
        else:   
            rain_dict.setdefault(city,rain) 
    print (rain_dict)
        
 
for city, rain in rain_dict.items():
    print(f'{city}: {rain}')

# 70: how do dicts work? 
d = {'a':1, 'b':2, 'c':3} # O(1) - constant time 
myList = [10, 20, 30] # O(n) -- time is proportional to the length 
# hash function 

hash('abcd')
globals()

# Section 8: 
# 71 Intro to sets 

# set is a list, that have all the values are unquie and quickly searchable  
# or: a dictionary only week key, not with value 

s = set() 
s.add(20)
s.add(30)
s.add(40)
# set make sure uniqueness, and key only  
s = {10, 20, 30, 40}
s
print(s)  
# if I want to create an empty set  => s = set()



s = {10, 20, 30, 40 }
s.add(50)
s.add(50.0)
s.update (20, 30, 40)
s.update([20, 30 , 40, 50 , 60])

s.remove(30)

# 74 | Exercise 10: Dollar store  
# dollar store: have a lot of item, but all have the same price 
# ask the user, again and again, what they awant to buy.  
# if they give an empty string, exits and give the total bill 
# if they give a string taht is in our inventory,  then add $1 to the total 
# if they give a string that isn't in our inventory, scold them  


### to come back on this exercise, skip this for now as the focus is to get through the remaining sections within today.  

# 76 | Set Operations 
s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

s1 - s2 # show me what is in s1 but *NOT* in s2
# {50, 60}
s2 - s1 # show me what is in s2 but *NOT* in s1 
# {50, 60}

# what elements is in either s1 or s2, but not in both?  
s1.symmetric_difference(s2) 
# symmetric_difference is basically ... xor 
s1 ^ s2 # uses the bitwise ^ operator 

s3 = {20, 30}
# is s3 a subset of s1? 
s3 < s1 
# is s2 a subset of s1?
s2 < s1 

# union means to combine them 
s1 | s2 # return a set with all elements from both! 
# the result will definately not containt duplicate values because as a set itself, it doesnt have duplicate values 

s1 & s2 # return a set with elements in both 

# 71 | Exercise 11 | Spelling bee 
'''
define a word that contains 7 different letters 
(or it can just be a collection of 7 different letters )

- ask the user to enter a string 
- if the string contains only those letter from the 7, say 'yay' 
- if not, then say 'boo' 
'''


default_str = {'a','b','c','d','e','f','g'}
letter_set = set()

while True:
    user_input = input('enter your word: ').strip()
    if not user_input: 
        break 
    for letter in user_input: 
        letter_set.add(letter)
print (letter_set)
if letter_set == default_str: 
    print ('Yay')
else: 
    print ('Boo')
# why '<' does not work? is it because letter_set contain equal the element of default_str? 
# try this by having letter_set has less elements than default_str 
# yes, my thought was correct, when i tried letter_set with less elments, the operation works 



# split the word and put them into a set 

# match the letter into the define set 
# if the elements in the input is a subset or equal to the define set, you are good 
# if False => return 'boo' 

# below is the solution 
letters = set('abcdefg')
while True:
    user_input = input('enter your word: ').strip()
    if not user_input:
        break
    elif set(user_input) <= letters: 
        print (f'Yes, {user_input} only uses our letters') 
    else: 
        print (f'No, {user_input} uses other letters') 

'''
note from reflecting the solution: 
- miss understood the question, i though the user input has to have 7 characters.  
- my approach is manually define the elements of the set, while the solution use the default function, which is smart.  
- the same thing for the user input, i converted the user input into a list of character, then put them in set. Didnot know that I create a set from a list. Thought I could do it. 

'''
