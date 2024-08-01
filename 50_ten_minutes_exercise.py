'''
Exercise 1: Number guessing game 
For this exercise
- Write a function (guessing_game) that takes no arguments.
- When run, the function chooses a random integer between 0 and 100 (inclusive).
Then ask the user to guess what number has been chosen.
- Each time the user enters a guess, the program indicates one of the following:
- Too high/ Too low/ Just right
- If the user guesses correctly, the program exits. Otherwise, the user is asked to
try again.
- The program only exits after the user guesses correctly.
'''

import random

def guessing_name():
    answer = random.randint(0,100)
    print (answer)
    
    while True: 
        user_guess = int(input('what is your guess? ' ))
        
        if user_guess == answer: 
            print(f'Binggo, the answer is {answer}')
            break 
        
        if user_guess < answer: 
            print(f'Your guess of {user_guess} is lower than the answer')
        
        else:  
            print(f'Your guess of {user_guess} is higher than the answer')

guessing_name()

### today, try different scenarios 1) guess words, 2) providing hint for user response thus they can do better guess 



'''
Exercise 2: Summing numbers
- to write a mysum function that does the same thing as the
built-in sum function. However, instead of taking a single sequence as a parameter, it
should take a variable number of arguments. Thus, although you might invoke
sum([1,2,3]), you'd instead invoke mysum(1,2,3) or mysum(10,20,30,40,50)
'''

# Initial thougths: 
# Do i need to create an input function for users to input the number that they want to perform the sum funcion? 
# => nope the exercise does not ask me to do so? seem like how the fuction will generate the answers through manually input the numbers to print call

 

def mysum(*numbers): # type: ignore # 'splat' (aka *) enable the function mysum() to receive "infinate" argument  
    output = 0 
    for number in numbers: 
        output += number 
    return output

print(mysum(2,4,5,7))
print(mysum(30, 80, 32, 34))

# what happen if I dont use the 'splat -* '
def mysum(numbers): 
    output = 0 
    for number in numbers: 
        output += number 
    return output
print (mysum(2,4,5))
'''
{  
	"name": "TypeError",
	"message": "mysum() takes 1 positional argument but 3 were given",
	"stack": "---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
File c:\\\\     \\.py:6
      4         output += number 
      5     return output
----> 6 print (mysum(2,4,5))

TypeError: mysum() takes 1 positional argument but 3 were given"
}

'''

def mysum(numbers): 
    output = 0 
    for number in numbers: 
        output += number 
    return output
print (mysum(2))
'''
{
	"name": "TypeError",
	"message": "'int' object is not iterable",
	"stack": "---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
File c:\\\\     \\.py:6
      4         output += number 
      5     return output
----> 6 print (mysum(2))

File c:\\\\     \\.py:3
      1 def mysum(numbers): 
      2     output = 0 
----> 3     for number in numbers: 
      4         output += number 
      5     return output

TypeError: 'int' object is not iterable"
}
'''

# without the "*" 
    #   python understand that function mysum() only has one argurment
    #   for number in numbers cannt execute as there is only one 'int' which cannt be iterable


# what happen if i use str instead of int as an input 
def mysum(*numbers): 
    output = 0 
    for number in numbers: 
        output += number 
    return output
print (mysum('hello', 'morning'))

'''
{
	"name": "TypeError",
	"message": "unsupported operand type(s) for +=: 'int' and 'str'",
	"stack": "---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
File c:\\\\     \\.py:6
      4         output += number 
      5     return output
----> 6 print (mysum('hello', 'morning'))

File c:\\\\     \\.py:4
      2 output = 0 
      3 for number in numbers: 
----> 4     output += number 
      5 return output

TypeError: unsupported operand type(s) for +=: 'int' and 'str'"
}
'''

# seem like python does not like to have to str add together? nope not the case as two strs still can be add 
# for example: x = 'abc' y = 'def', i can still do x + y. 
# to follow up: read the document on "+="

'''
addition exercise to practice when I have time

a) The built-in version of sum takes an optional second argument, which is used as
the starting point for the summing. (That's why it takes a list of numbers as its
first argument, unlike our mysum implementation.) So sum([1,2,3], 4) returns
10, because 1+2+3 is 6, which would be added to the starting value of 4. Reimplement
your mysum function such that it works in this way. If a second argument
is not provided, then it should default to 0. Note that while you can write
a function in Python 3 that defines a parameter after *args, I'd suggest avoiding
it and just taking two arguments—a list and an optional starting point.

b)  Write a function that takes a list of numbers. It should return the average (i.e.,
arithmetic mean) of those numbers.

c)  Write a function that takes a list of words (strings). It should return a tuple containing
three integers, representing the length of the shortest word, the length
of the longest word, and the average word length.

d)  Write a function that takes a list of Python objects. Sum the objects that either
are integers or can be turned into integers, ignoring the others.
'''


'''
Exercise 3: Running time  
For this exercise, then, we'll assume that you run 10 km each day as part of your
exercise regime. 
    - You want to know how long, on average, that run takes.
    - Write a function (run_timing) that asks how long it took for you to run 10 km.
    - The function continues to ask how long (in minutes) it took for additional runs, until
    the user presses Enter. At that point, the function exits—but only after calculating and
    displaying the average time that the 10 km runs took.
For example, here's what the output would look like if the user entered three data
points:
Enter 10 km run time: 15
Enter 10 km run time: 20
Enter 10 km run time: 10
Enter 10 km run time: <enter>
Average of 15.0, over 3 runs
'''

record=input('How long it takes to complete your 10km:' )

# what is the possible input from the users?  
# typical response should be: hh:mm:ss 
# lets say my three run result are: 
    # 1st run = 01:20:35 
    # 2nd run = 00:35:60
    # 3rd run = 00:45:35
    # how to add the time with second,minute, and hour 
        # could not come up the answer by myself. ask chatgpt for suggestion, and its answer is quite helpful. I think through the response and redocument the solution and approach in my own words
            # to solve this, 1) convert all the input into second, 2) perform the request calculation (i.e.plus, minus, average, etc.) 3) convert the result back to the orignal format
                # 1) conver all the input into second: 
                    # using two function: 
                        # time_str.split(':'): 
                            # what it does? splits the 'time_str' string into a list of substrings whenever there's a colon (':')
                            # sample: if time_str is "01:30:45", then time_str.split(':') will result in the list ["01", "30", "45"].
                        # map(int, ...):
                            # what it does? The map function applies a given function (in this case, int) to each item of an iterable (in this case, the list ["01", "30", "45"]).
                            # sample: map(int, time_str.split(':')) will convert each string in the list to an integer 
                                # so ["01", "30", "45"] become [01, 30, 45]
                        # h, m, s = ...: 
                            # what is does? tuple unpacking. assign the result of tuple "map" in to respective variable 
                        
def conver_to_second (record):
    h, m, s = map(int, record.split(':'))
    return h*3600 + m*60 + s 

def average (record):
    
def convert_to_answer (record): 
    
    
print (record)
print (conver_to_second(record))

 
                        
'''
function to let user input how many time to run last week? 
    sample: 
        system display: how many time do you run this week?
        user_input: 3 

function to let user input the running stats for each run 
    sample:
        system display: what is the record for the 1st run? 
        user_input: hh:mm:ss 
        
        system display: what is the record for the 1st run? 
        user_input: hh:mm:ss 
    
        system display: what is the record for the 1st run? 
        user_input: hh:mm:ss

function to calculate the average   
    1) store the input into ?? 
    2) convert the input into second 
    3) perform the calculation 
    4) convert the calculation back to the format 
    
fucntion to return the answer to the users:  
'''

def get_run_info (): 
    while True: 
        try:
            run_info = int(input("input number of run you had: "))
            if run_info < 0: 
                raise ValueError("It cannt be right! # of running cannt be negative")
            return run_info
        except ValueError as e:
            raise ValueError(f'Invalid input: {e}. Please enter a valid number.')

def get_run_stats (run_info):
    run_stats_combined = [] 
    for i in range(run_info):
        while True:
            try:  
                get_run_stats = input(f'what is your record for the {i + 1} run in (hh:mm:ss)?')
                h, m, s = map(int, get_run_stats.split(":"))
                if h < 0 or m < 0 or s <0:  
                    raise ValueError("It cannt be right! your running time cannt be negative")
                if m > 60 or s >60: 
                    raise ValueError("your minutes or seconds cannt be larger than 60")
                run_stats_combined.append(get_run_stats)
                break 
            except ValueError as e:
                raise ValueError(f'Invalid input: {e}. Please enter valid format.')
    return run_stats_combined              
            
def time_to_second (time_str):
    h, m, s = map(int, time_str.split(':'))
    return h*3600 + m*60 + s 

def second_to_time (seconds):
    h = seconds // 3600 
    seconds %= 3600 
    m = seconds //60 
    s = seconds % 60   
    return f"{int(h):02}:{int(m):02}:{int(h):02}"

def calculate_average_time (run_stats):
    total_seconds = sum(time_to_second(time) for time in run_stats)
    average_seconds = total_seconds // len(run_stats)
    return second_to_time(average_seconds)

def main():
    run_info = get_run_info()
    run_stats_combined = get_run_stats(run_info)
    average_second = calculate_average_time(run_stats_combined)
    print (f'the average running time is {average_second}')

if __name__ == "__main__":
    main()
             
# to note down stuff that I learn from doing this exercise
              

'''
Exercise 4: 
For this exercise, you need to write a function (hex_output) that takes a hex number
and returns the decimal equivalent. That is, if the user enters 50, you’ll assume
that it's a hex number (equal to 0x50) and will print the value 80 to the screen. And
no, you shouldn't convert the number all at once using the int function, although it’s
permissible to use int one digit at a time.


'''
# 0x1357 -- base 16 
x = 7 * 16**0
y = 5 * 16**1
z = 3 * 16**2
e = 1 * 16**3  
print ( x + y + z + e  )
# the base number will start with 0, then the next digit is  n+1   
hex(4951)  # output: 0x1357  
# reserve the number from 4951 to become 1 5 9 4 

# ask for user input 
# 
conver_number = input('What number do you want to convert: ')
print (conver_number)

def hex_output(conver_number):
    conver_number = input('What number do you want to convert: ')
    total = 0  
    for index, one_digit in enumerate(reversed(conver_number)):
        total += int(one_digit) * 16 ** index 
    print (total)

hex_output(conver_number)


# exercise 5 - 6 are pig latin in word and sentence.  

# excercise 7 
'''
For this exercise, you'll write a function (called ubbi_dubbi) that takes a single
word (string) as an argument. It returns a string, the word's translation into Ubbi
Dubbi. So if the function is called with octopus, the function will return the string
uboctubopubus. And if the user passes the argument elephant, you'll output
ubelubephubant.
'''

def ubbi_dubbi (word):
    output = []
    for letter in word:  
        if letter in 'aeiou':
            output.append(f'ub{letter}')
        else: 
            output.append(letter)
    return ''.join(output)
# type(output) ? 
# type(ubbi_dubbi)?
ubbi_dubbi('hello world')

'''
how this function work?
- assign an argument 
- create a list 
- use for function to iterlate each component in the argument 
    - then check the condition of each component to see if 
        - has component that match with component in default string if yes: 
            append (add into the list) the component with 'ub' preface 
            if no. just add the component in the the list 
- display the output list in a word format using ''.join() to glue all the character in output without space in between => this turn output from list to string
  
'''
 
# what if I write it the other way around?  search for letter not in 'aeiou'? how does it impact the performance  

# exercise 8
'''
In this exercise, youll explore this idea by writing a function, strsort, that takes a
single string as its input and returns a string. The returned string should contain the
same characters as the input, except that its characters should be sorted in order, from
the lowest Unicode value to the highest Unicode value. For example, the result of
invoking strsort('cba') will be the string abc.
'''
def strsort (a_string):
    return ''.join(sorted(a_string))

strsort ('asdfasdf')

word = 'adsfasdvb'
print (sorted(word))
# output:  ['a', 'a', 'b', 'd', 'd', 'f', 's', 's', 'v']
# when I use sorted(list) function, the output return a new list of string or list from the input. 
# => in order for the output to display properly, need to create a string by using ''join() function  


'''
Consider a few other variations of, and extensions to, this exercise, which also use
str.split and str.join, as well as sorted:
 Given the string “Tom Dick Harry,” break it into individual words, and then sort
those words alphabetically. Once they're sorted, print them with commas (,)
between the names.
 Which is the last word, alphabetically, in a text file?
 Which is the longest word in a text file?
Note that for the second and third challenges, you may well want to read up on the
key parameter and the types of values you can pass to it. A good introduction, with
examples, is here: http://mng.bz/D28E.
'''

# exercise 9
'''
Write a function, firstlast, that takes a sequence (string, list, or tuple) and returns the first and last elements of that
sequence, in a two-element sequence of the same type. So firstlast('abc') will
return the string ac, while firstlast([1,2,3,4]) will return the list [1,4].
'''

def firstlast (word):
    resultfirst = word[:1]
    resultlast = word[-1:]
    result = word[:1] + word[-1:]
    print (resultfirst)
    print (resultlast) 
    print (result)
    print (type(word))
    print (type(result))
firstlast ('hello') # sequence type string 
firstlast ([1,2,3,4]) # sequence type list  
firstlast ((1,2,3,4)) # sequence type tuple  
'''
input:  
    firstlast ({1,2,3,4}) # sequence type set does not return

output: 
{
	"name": "TypeError",
	"message": "'set' object is not subscriptable",
	"stack": "---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
File c:\\Users\\dqthi\\OneDrive\\Coding_Journey\\CodeBreakThrough\\Beginner_Python_Programming_All-in-One_Tutorial_Series\\50_ten_minutes_exercise.py:11
      9 firstlast ([1,2,3,4]) # sequence type list  
     10 firstlast ((1,2,3,4)) # sequence type set   
---> 11 firstlast ({1,2,3,4})

File c:\\Users\\dqthi\\OneDrive\\Coding_Journey\\CodeBreakThrough\\Beginner_Python_Programming_All-in-One_Tutorial_Series\\50_ten_minutes_exercise.py:2
      1 def firstlast (word):
----> 2     resultfirst = word[:1]
      3     resultlast = word[-1:]
      4     result = word[:1] + word[-1:]

TypeError: 'set' object is not subscriptable"
}
'''
 
# explain why having more than argurment inputted does not work  
'''
input:  
def firstlast (word):
    pass
firstlast ('hello','morning','afternoon')
firstlast ([1,2,3,4], [2, 3, 4, 5])

output:  
{
	"name": "TypeError",
	"message": "firstlast() takes 1 positional argument but 3 were given",
	"stack": "---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
File c:\\Users\\dqthi\\OneDrive\\Coding_Journey\\CodeBreakThrough\\Beginner_Python_Programming_All-in-One_Tutorial_Series\\50_ten_minutes_exercise.py:10
      8 firstlast ('hello')
      9 firstlast ([1,2,3,4])
---> 10 firstlast ('hello','morning','afternoon')
     11 firstlast ([1,2,3,4], [2, 3, 4, 5])

TypeError: firstlast() takes 1 positional argument but 3 were given"
}

explaination: 
- in the def line, the default setting for function only alows the function to accept 1 argument, which is "word"  
=> when we call the function with more than 1 argument, the function gets confuse as it does not know how to do with the n+1 argument. Therefore return an error as above.  
'''    


