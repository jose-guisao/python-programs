##read file with utf-8
fname = input("Enter file name: ")
with open(fname, "r", encoding="utf-8") as f:
    text = f.read()
    print(text)


##Searching for: python program to count words from a file
##script from bing

fname = input("Enter file name: ")
num_words = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)

print("Number of words:")
print(num_words)

# =================================
import wget
url = "https://gutenberg.org/ebooks/71049.txt.utf-8"
wget.download(url, 'C:/Users/admin/OneDrive/Documents/python-programs/71049.txt.utf-8')

# https://gutenberg.org/ebooks/71049.txt.utf-8

# ==================================
#Here’s a Python program that finds palindrome in a file and stores them in a list:
def is_palindrome(s):
    return s == s[::-1]

def find_palindromes_in_file(file_name):
    with open(file_name) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    palindromes = []
    for word in content:
        if is_palindrome(word):
            palindromes.append(word)
    return palindromes

fname = input("Enter file name: ")

print(find_palindromes_in_file(fname))
