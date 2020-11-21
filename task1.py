"""
1. Reads from a file called text.txt which has content from https://www.whitehouse.gov/briefings-statements/remarks-president-trump-state-union-address-3/ 
2. Writes below statistics to a file called summary.txt
-	Total word count
-	Total character count
-	The average word length
-	The average sentence length
-	A word distribution of all words ending in “ly”
-	A list of top 10 longest words.
"""

from collections import Counter
import nltk
import ssl
# nltk is a very large package, pip3 does not download entire package at once to 
# preserve space so manual download is required.
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('punkt')

from nltk import sent_tokenize, word_tokenize
import string
import sys

INPUT_FILE = "text.txt"
OUTPUT_FILE = "summary.txt"
READ_MODE = 'r'
WRITE_MODE = 'w'

try:
    with open(INPUT_FILE, READ_MODE) as file:
        data = file.read()
except (OSError, IOError) as err:
    print(f"Error in reading from {INPUT_FILE} with error {err}.")
    sys.exit(0)
except Exception as error:
    print(f"Exception raised when reading from {INPUT_FILE} with error {error}.")
    sys.exit(0)

with open(OUTPUT_FILE, WRITE_MODE) as output_file:
    total_words = word_tokenize(data) #Returns all the words as a list including duplicates.
    english_words = []
    for word in total_words:  # Removing the punctuations from the word list to only have english words.
        if word not in string.punctuation:
            english_words.append(word)
    output_file.write(f"Total word count: {len(english_words)} \n")

    #Character count would also include punctuations.
    output_file.write(f"Total character count: {sum(len(word) for word in total_words)}\n")
    
    #Only calculating english words for word length i.e. excluding punctuations.
    output_file.write(f"The average word length: {round(sum(len(word) for word in english_words)/len(english_words))} \n")

    sentences = sent_tokenize(data) # Returns list of separate sentences.
    total_sentence_length = sum(len(s) for s in sentences)
    output_file.write(f"The average sentence length: {round(total_sentence_length/len(sentences))}\n\n")
    word_freq_dict = Counter(english_words) # Returns a dictionary of list of unique words and their frequency.
    output_file.write(f"A word distribution of all words ending in “ly”:\n")
    for word, frequency in word_freq_dict.items():
        if word.endswith("ly"):
            output_file.write(f"{word}: {frequency}\n")
    output_file.write("\n")

    #Sorting the words in descending order with key as length.
    sorted_words = sorted(word_freq_dict.keys(), key=len, reverse=True)
    top_10_words = ", ".join(sorted_words[:10])
    output_file.write(f"A list of top 10 longest words in descending order: \n{top_10_words}")
