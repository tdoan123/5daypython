# everything is an object means: 
# (1) everytbing has a type/class
# (2) everything has attributes/values 

x = 100  
type(x)

x = "Hello"
type(x) 

x = [10, 20, 30] 
type(x) 
# asking for the type of x means asking for the type of values that x holds. 

# class acts as a manufacuturer of objects. 
# for example, car manufacturer produces cars. 
# class 'int' product objects of type integer.  
# class 'str' product objects of type string.
# class 'list' product objects of type list.

list('hello') # make the value within '' become a list of characters ['h', 'e', 'l', 'l', 'o']
str('1234') # make the value within '' become a string '1234'
int('5678') # make the value within '' become an integer 5678

# class itsself is also an object. 
# class is a blueprint for creating objects.    
# factory's factory = type -- every class's type is "type".

type(type)

a # identifier = name = variable or function.. an objecti of some sort  
# search is LEGB (rule: Local, Enclosing, Global, Built-in)

a.b # .b means: look for the name ("attribute") b inside of the object a. 

a  = 'abcd'
dir(a) # "dunder" means double underscore.  

a.upper()
   
import os 
os.sep # os.sep is an attribute of the os module.

# differences between function and method:
mylist= [10, 20, 30] 
sum(mylist) # 'sum' is a function.takes a list as an argument.  

class Foo(object):
    pass

type(Foo)   

Foo()

f = Foo()
type(f)# 'type' is a function.

dir('Foo')

dir(f)

f = Foo()
vars() # global namespace 
# def bar(): 

class Foo(object):
    def __init__(self):
        self.x = 100 # I want to add 'x' to the object self that is pointed to by 'f'.
        self.y = [10, 20, 30]
        self.z = 'hello'
        
f = Foo()
vars(f) # vars() is a function.
        
g = Foo()
vars(g)

# self is convention. 'self' is the object itself. 
# __init__ is a special method.
# __init__ is called when an object is created.

class Foo(object):
    def __init__(self,x, y, z):
        self.x = x 
        self.y = y
        self.z = z

f = Foo(100, [10, 20, 30], 'hello')
vars(f)

class Foo(object):
    def __init__(self,x = 123, y = 345, z = 'hello'):
        self.x = x 
        self.y = y
        self.z = z
        
f = Foo()

############# Exercise #############
"""(1) Scoop class -- each instance is one scoop of ice cream

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')

print(s1.flavor)  # chocolate
"""
class Scoop(object):
    def __init__(self, flavor):
        self.flavor = flavor
s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')

print(s1.flavor)  # chocolate        
print(s2.flavor)  # vanilla
print(s3.flavor)  # coffee

for scoop in [s1, s2, s3]:
    print(scoop.flavor)  # chocolate, vanilla, coffee

# what if I want to create a dictionary of favor? 
# I want to create a dictionary of flavor.
"""
(2) Person class -- name, e-mail address, and phone number
    Create several people, and iterate over them in a list 
    and print their names (similar to a phone book)

    Change the e-mail address of one person, and show
    that it has changed by printing your list a second time
"""
class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

p1 = Person('Alice', 'asdf@gmail.com', '123-456-7890')
p2 = Person('Bob', 'sad@hotmail.com','234-567-8901')
p3 = Person('Charlie', 'happy@yahoo.com', '345-678-9012')

people = [p1, p2, p3]
for person in people:
    print(person.name)
    print(person.email)
    print(person.phone)
    print('')

p3.email = 'delightful@iclould.com'

people = [p1, p2, p3]
for person in people:
    print(person.name)
    print(person.email)
    print(person.phone)
    print('')

"""        
(3) Create a BankAccount class. It'll have a single
    attribute (per instance), transactions -- a list of floats

    Every time you deposit, append a positive float
    Every time you withdraw, append a negative float

    (a) create two different accounts
    (b) add a number of transactions +/- to each account
    (c) show, for each account, the number of transactions
    and the average amount per transaction, as well as
    the current balance.  (assume it starts at 0)"""
    
class BankAccount:
    def __init__(self):
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.transactions.append(amount)
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            self.transactions.append(-amount)
        else:
            print("Withdrawal amount must be positive.")

    def get_number_of_transactions(self):
        return len(self.transactions)

    def get_average_transaction(self):
        if self.transactions:
            return sum(self.transactions) / len(self.transactions)
        else:
            return 0

    def get_balance(self):
        return sum(self.transactions)


# Create two different accounts
account1 = BankAccount()
account2 = BankAccount()

# Add transactions to each account
# Account 1
account1.deposit(100.0)
account1.withdraw(35.0)
account1.deposit(50.0)
account1.withdraw(5.0)
account1.withdraw(5.0)
account1.withdraw(5.0)
account1.withdraw(5.0)
account1.withdraw(200.0)

# Account 2
account2.deposit(100.0)
account2.withdraw(50.0)
account2.deposit(100.0)
account2.withdraw(30.0)

# Function to display account details
def display_account_details(account, account_name):
    print(f"Details for {account_name}:")
    print(f"Number of transactions: {account.get_number_of_transactions()}")
    print(f"Average amount per transaction: {account.get_average_transaction():.2f}")
    print(f"Current balance: {account.get_balance():.2f}")
    print('-' * 30)

# Display details for each account
display_account_details(account1, "Account 1")
display_account_details(account2, "Account 2")