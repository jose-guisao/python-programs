
def listToString(someList):
    """Write a function that takes a list value as an argument
     and returns a string with all the items separated by a comma
      and a space, with and inserted before the last item. For 
      example, passing the previous spam list to the function would 
      return 'apples, bananas, tofu, and cats'. But your function 
      should be able to work with any list value passed to it."""
    
    newList = ''
    for i in range(len(someList)-1):
        newList = newList + someList[i]+', '
    newList = newList + ' and ' + someList[-1]
    return(newList)


spam = ['apples', 'bananas', 'tofu', 'cats']
spam2 = ['cat', 'bat', 'rat', 'elephant','caballo','perro','burro','camello']
print(spam)
print(spam2)
print(listToString(spam2))
print(type(listToString(spam2)))
# for i in spam:
#     print(i)



