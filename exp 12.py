from collections import Counter
import string

# Sample text data (defined inside the program)
text = """
Data science is an interdisciplinary field that uses scientific methods,
processes, algorithms, and systems to extract knowledge and insights
from structured and unstructured data. Data analysis is an important
part of data science. Data science helps businesses make better decisions
and predict future trends.
"""

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans("", "", string.punctuation))

# Split into words
words = text.split()

# Count word frequencies
word_count = Counter(words)

# Display results
print("Word Frequency Distribution:\n")
for word, count in word_count.most_common():
    print(word, ":", count)
