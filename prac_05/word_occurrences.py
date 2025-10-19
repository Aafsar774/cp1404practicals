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

    sorted_words = sorted(counts.keys())

    for word in sorted_words:
        count = counts[word]
        print(f"{word} : {count}")

main()
