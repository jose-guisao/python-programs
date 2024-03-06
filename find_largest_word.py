def longest_word(filename):
    with open(filename, 'r', encoding="utf-8") as infile:
        words = infile.read().split()
        max_len = len(max(words, key=len))
        return [word for word in words if len(word) == max_len]

print(longest_word('1661-0.txt'))
