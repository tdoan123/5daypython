mylist = [1 , 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]

number_count = {}
for one_number in mylist: 
    if one_number not in number_count:
        number_count[one_number] = 1
    else:
        number_count[one_number] += 1
print(number_count)


mylist2 = ['mot' , 'hai', 'ba', 'bon', 'nam', 'mot' , 'hai', 'ba', 'bon', 'nam', 'sau']

number_count2 = {}
for one_number in mylist2: 
    if one_number not in number_count2:
        number_count2[one_number] = 1
    else:
        number_count2[one_number] += 1
print(number_count2)

# conclusion:  
# when I use for loop to count the number of occurences of each element in a list, I can use dictionary to store the count value. 
# The key is the element, and the value is the count of the element.