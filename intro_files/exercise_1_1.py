# this section is about reading and writing files in python 
# 1) load the file, 
# 2) separate the data using delimiter
# 3) store the first column which is a unique ip address into a list

# import csv
# with open(r"C:\Users\dqthi\Downloads\exercise-files\mini-access-log.txt") as file:
#     reader = csv.reader(file,delimiter=' ', quotechar='"', skipinitialspace=True)
#     ip_list = []
#     for row in reader:
#         if row[0] not in ip_list:
#             ip_list.append(row[0])
#         else:
#             continue
#     len(ip_list)
#     print (ip_list)
# try out the approach where I count each request per IP, and store the count value as a dictionary value


# import csv
# with open(r"C:\Users\dqthi\Downloads\exercise-files\mini-access-log.txt") as file:
#     reader = csv.reader(file, delimiter=' ', quotechar='"', skipinitialspace=True)
    
#     first_row = next(reader)  # Get the first row
#     print(first_row[3])    
    
#     for index, word in enumerate(first_row):
#         print(f"Word {index+1}: {word}")


for one_line in open (r"C:\Users\dqthi\Downloads\exercise-files\mini-access-log.txt"): 
    print(one_line)
    # turn the file data into a list of strings 

counts = {}
    
for one_line in open (r"C:\Users\dqthi\Downloads\exercise-files\mini-access-log.txt"): 
    ip_address = one_line.split()[0]
    
    if ip_address not in counts:
        counts[ip_address] = 0 
    
    else:
        counts[ip_address] += 1

for key, value in counts.items(): 
    print(f'{key} made {value} requests')


    # each line turn into a list of strings 


# each line is a list of strings, separated by a space