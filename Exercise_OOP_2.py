class Person(object): 
    def __init__(self, name, email_address, phone_number):
        self.name = name 
        self.email_address = email_address 
        self.phone_number = phone_number 

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email_address}, Phone: {self.phone_number}"

p1 = Person("John", "asdf@hotmail.com", "1234567890")
p2 = Person("Jane", "asdf@yahoo.com", "0987654321") 
p3 = Person("Joe", "aasdf@outlook.com", "1231231234")

phone_book = [p1, p2, p3]
for contact in phone_book: 
    print(contact)

# this work pretty well, yet when I input the following code, it does not work. 
'''
print (p1)
=> output: <__main__.Person object at 0x000002C175E9B210>
but when I ask for print(p1.name) or print(p1.email_address) or print(p1.phone_number), it works.

print (phone_book)
=> output: <__main__.Person object at 0x000002C175EDF4D0>
''' 

# type(phone_book) 
# output: <class 'list'> 

# type(p1)
# output: __main__.Person
