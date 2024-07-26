
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


