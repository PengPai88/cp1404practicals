"""
Word Occurrences
Estimate: 20 minutes
Actual:   25 minutes
"""

text = input("Text: ").split()
word_counts = {}

for word in text:
    word_counts[word] = word_counts.get(word, 0) + 1

words = list(word_counts.keys())
words.sort()

max_length = max(len(word) for word in words)
for word in words:
    print(f"{word:{max_length}} : {word_counts[word]}")