import csv 
with open(r"C:\Users\dqthi\Downloads\exercise-files\wcfile.txt") as file:
    reader = csv.reader(file) 

# count how many character in the file
    character_count = 0 
    for one_character in reader:
        character_count += 1 
    print(f'The file contains {character_count} characters.')


# count how many lines in a file    
    row_count = 0
    for row in reader: 
        row_count += 1 
    print(f'It also contains {row_count} lines.')    

# what is the difference between csv.reader and file.read(
# search for for alphabetical characters in the file
# search for numbers and other characters in the file 
# count how many character in the file 
# count how many words in a file 

    # this can be done by reviewing the number of row in the file 
    
# what is self referantial?

import csv 
with open(r"C:\Users\dqthi\Downloads\exercise-files\wcfile.txt") as file:
    reader = csv.reader(file,delimiter=' ') 
    character_count = []    
    for one_character  in row:
        print(one_character)
        character_count.append(one_character)
        print(character_count)
        print(len(character_count))  
        
# count how many words in a file  
        word_count = 0
        for row in reader:
            word_count += len(row)
        print(f'It contains {word_count} words.')

import csv 
with open(r"C:\Users\dqthi\Downloads\exercise-files\wcfile.txt") as file:
    reader = csv.reader(file,delimiter=' ') 
    word_count = 0
    for row in reader:
        word_count += len(row) # 'len(row)' is the number of words in each row
        print (word_count)
    