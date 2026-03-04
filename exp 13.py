from collections import Counter
import string

# Take input from user
text = input("Enter a paragraph: ")

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans("", "", string.punctuation))

# Split into words
words = text.split()

# Count frequency
frequency = Counter(words)

# Display result
print("\nWord Frequency Distribution:\n")
for word, count in frequency.items():
    print(word, ":", count)
