import csv 
with open(r"C:\Users\dqthi\Downloads\exercise-files\wcfile.txt") as file:
    reader = csv.reader(file,delimiter=' ') 

# count how many character in the file
    all_characters = []
    
# count how many words in a file
    word_count = 0
    for row in reader: # row is a list of row in the file, loop one row after another, then 
        word_count += len(row)  # insert the number of words of each row thorugh [len(row) gives the number of words in a row]
    print(word_count)


# count how many lines in a file    
    row_count = 0
    for row in reader: 
        row_count += 1 
    print(f'It also contains {row_count} lines.')    


# Open the file in read mode
with open(r"C:\Users\dqthi\Downloads\exercise-files\wcfile.txt") as file:
    # Read the entire content of the file
    content = file.read() 
    # Count the number of characters in the content
    


    # Print the character count
    print(f'The file contains {character_count} characters.')




# search for for alphabetical characters in the file
# search for numbers and other characters in the file 
# count how many character in the file     
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


# Open the file in read mode
with open(r"C:\Users\dqthi\Downloads\exercise-files\wcfile.txt") as file:
    # Read the entire content of the file
    content = file.read()

# count how many character in the file
character_count = len(content)

# Split the content into lines
lines = content.splitlines()

# Count the number of lines
line_count = len(lines)

# Initialize word count
word_count = 0

# Iterate over each line
for line in lines:
    # Split the line into words
    words = line.split()
    # Add the number of words in the line to the total word count
    word_count += len(words)

# Print the line count and word count
print(f'The file contains {character_count} characters, {line_count} lines and {word_count} words.')

import csv

# Initialize counters
character_count = 0
word_count = 0
line_count = 0

# Open the file in read mode
with open(r"C:\Users\dqthi\Downloads\exercise-files\wcfile.txt") as file:
    # Create a CSV reader object with space as the delimiter
    reader = csv.reader(file, delimiter=' ')
    
    # Iterate over each row in the CSV reader
    for row in reader:
        # Increment the line counter
        line_count += 1
        word_count += len(row)
    print(line_count)
    print(word_count) 
    
    for row in reader:
        # Count the number of words in the row
    
        # Count the number of characters in the row
        for word in row:
            character_count += len(word)
        # Add spaces between words to the character count
        character_count += len(row) - 1
        
        # Add one for the newline character at the end of each line
        character_count += 1

# Print the counts for characters, words, and lines
print(f'The file contains {character_count} characters, {line_count} lines, and {word_count} words.')


counts = {'line': 0,
          'words': 0, 
          'characters': 0}

unique_words = set() 

for one_line in open (r"C:\Users\dqthi\Downloads\exercise-files\wcfile.txt"):
    counts['line'] += 1
    counts['words'] += len(one_line.split())
    counts['characters'] += len(one_line)
    unique_words.update(one_line.split())
    
counts['unique_words'] = len(unique_words)
for key, value in counts.items():
    print(f'The file contains {value} {key}')
    
# should be thinking set when there is a request for unique values

