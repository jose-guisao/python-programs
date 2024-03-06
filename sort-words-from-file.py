with open('1661-0.txt', 'r', encoding="utf-8") as f:
    words = f.read().split()
words = list(set(words))
words.sort()
print(words)

