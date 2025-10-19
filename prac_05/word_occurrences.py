"""
Word Occurrences
Estimate: 40 mins
Actual:   53 mins
"""

def main():
    text = input("Text: ").strip()
    words = text.lower().split()
    counts = {}

    for word in words:
        if word in counts:
            current = counts[word]
        else:
            current = 0
        counts[word] = current + 1

    longest_length = 0
    for word in counts.keys():
        length = len(word)
        if length > longest_length:
            longest_length = length

    sorted_words = sorted(counts.keys())

    for word in sorted_words:
        count = counts[word]
        print(f"{word:{longest_length}} : {count}")

main()
