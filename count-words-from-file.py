##Searching for: python program to count words from a file
##script from bing
import wget
url = "https://gutenberg.org/files/1661/1661-0.txt"
##url = "https://gutenberg.org/ebooks/71049.txt.utf-8"
wget.download(url, 'C:/Users/admin/OneDrive/Documents/python-programs/1661-0.txt')

fname = input("Enter file name: ")
num_words = 0

with open(fname, "r", encoding="utf-8") as f:
    for line in f:
        words = line.split()
        num_words += len(words)

print("Number of words:")
print(num_words)
