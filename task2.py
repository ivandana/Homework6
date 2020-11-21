
"""
Please use dictionary to keep the count of each letter. Read a text file named “book.txt” that may have multiple lines. 
Then create a “summary.txt” file that has the frequency of each letter, case-insensitive, i.e., “a” and “A” are the same letter. 
Each line has a record of the letter and frequency. The last line should be a summary to tell if the file has all 26 letters. 
"""


INPUT_FILE = "book.txt"
OUTPUT_FILE = "summary.txt"
READ_MODE = 'r'
WRITE_MODE = 'w'
ENGLISH_ALPHABET_COUNT = 26

input_file = open(INPUT_FILE, READ_MODE)
with input_file:
    data = input_file.read().upper()
    
char_dict = {}
for character in data:
    if character.isalpha(): # Only consider alphabets, ignore other characters.
        char_dict[character] = data.count(character)
  
output_file = open(OUTPUT_FILE, WRITE_MODE)
with output_file:
    for letters in sorted(char_dict.keys()):  # Sorting letters.
        output_file.write(f'{letters}: {char_dict[letters]}\n')

    if len(char_dict) == ENGLISH_ALPHABET_COUNT:
         output_file.write("\nIt has all letters.")
    
    else:
         output_file.write("\nIt doesn't have all letters.")

    
