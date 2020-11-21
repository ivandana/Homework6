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
    if character.isalpha():
        char_dict[character] = data.count(character)
  
output_file = open(OUTPUT_FILE, WRITE_MODE)
with output_file:
    for letters in sorted(char_dict.keys()):
        output_file.write(f'{letters} {char_dict[letters]}\n')

    if len(char_dict) == ENGLISH_ALPHABET_COUNT:
         output_file.write("\nIt has all letters.")
    
    else:
         output_file.write("\nIt doesn't have all letters.")

    