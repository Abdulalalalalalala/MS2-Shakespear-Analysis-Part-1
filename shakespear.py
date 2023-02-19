import re

# Open the file in read mode
with open('pg100.txt', 'r') as file:
    # Read the contents of the file
    essay = file.read()

# Remove punctuation and convert to lowercase
essay = re.sub(r'[^\w\s]', '', essay).lower()

# Split the essay into individual words
words = essay.split()

# Create an empty dictionary to store the word counts
word_counts = {}

# Loop through the words in the essay and add them to the dictionary
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Sort the dictionary by value in descending order and get the top 5 words
top_words = sorted(word_counts, key=word_counts.get, reverse=True)[:100]

# Print the top 5 words and their counts
for word in top_words:
    print(f"{word}: {word_counts[word]}")
