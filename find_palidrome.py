#Here’s a Python program that finds palindrome in a file and stores them in a list:
def is_palindrome(s):
    return s == s[::-1]

def find_palindromes_in_file(fname):
    with open(fname, "r", encoding="utf-8") as f:
        content = f.readlines()
        print(content)
    content = [x.strip() for x in content]
    palindromes = []
    for word in content:
        if is_palindrome(word):
          print(word)
          palindromes.append(word)
    return palindromes

fname = input("Enter file name: ")

print(find_palindromes_in_file(fname))

