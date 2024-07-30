
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



