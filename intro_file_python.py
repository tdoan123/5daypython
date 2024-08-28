f = open(r"C:\Users\dqthi\Downloads\exercise-files\mini-access-log.txt")
for one_line in f: 
    print(one_line, end=' ')
    
for one_line in f: 
    print (one_line.split('-')[0], end= '')

# what do I write code directly from here, been used to coding in jupiter environment setting where each line of code execute separately 

print ('hello')

# nice, this is much better, after I have jupiter format on the right side.  
# the requirements are:
# 1) each line begins with an IP address
# 2) iterate over the file to get the IP address 
# 3) print out the IP address with the number of time they are making request (ignore what type of request)


[one_line.split("-")[0]                     # expression
 for one_line in f:
    print(one_line, end='')# iteration             
]

for one_line in f: 
    print (one_line.split('-')[0], end= '')

f.close() 