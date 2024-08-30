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

import csv
with open(r"C:\Users\dqthi\Downloads\exercise-files\mini-access-log.txt") as file:
    reader = csv.reader(file,delimiter=' ', quotechar='"', skipinitialspace=True) 
    ip_count = {}
    for row in reader: 
        if row[0] in ip_count:
            ip_count[row[0]] += 1
        else:
            ip_count[row[0]] = 1

    # print the dictionary
    # for ip in ip_count:
    #     print(ip, ip_count[ip]) # ip_count[ip] is the value of the dictionary ip_count with key is ip
    

    a = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)
    for ip, count in a:
        print(ip, count)
