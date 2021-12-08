import pprint
#udemy class chapter/lesson 18		
theBoard = {'top-L':' ','top-M':'X','top-R':' ','mid-L':' ','mid-M':' ','mid-R':' ','low-L':'','low-M': ' ','low-R': ' '}
		
pprint.pprint(theBoard)
		
#theBoard = {'top-L':' ','top-M':'X','top-R':' ','mid-L':' ','mid-M':' ','mid-R':' ','low-L':' ','low-M': ' ','low-R': ' '}
		
theBoard['top-M'] = ' '
		
pprint.pprint(theBoard)

'''
def printBoard(board):
    print(board['top-L'+'|'+board['top-M']+'|'+board['top-R'])
		      
def printBoard(board):
    print(board['top-L'+'|'+board['top-M']+'|'+board['top-R'])

def printBoard(board):
		print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
		      print('-----')
		      
SyntaxError: unexpected indent
>>>'''
def printBoard(board):
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-----')
    print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
    print('-----')
    print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])

theBoard={'top-R':'O','top-M':'O','top-L':'O'}
		      
theBoard={'top-R':'O','top-M':'O','top-L':'O'}

theBoard={'top-R':'O','top-M':'O','top-L':'O'}
		      
#theBoard=['top-R':'O','top-M':'O','top-L':'O']
		      
theBoard={'top-R':'O','top-M':'O','top-L':'O'}
		      
printBoard(theBoard)
		      
print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])

	      
theBoard={'top-R':'O','top-M':'O','top-L':'O',\
	      'mid-L':'X','mid-M':'X','mid-R': '',\
	      'low-R':'X','low-M':' ','low-L': ''}
	      
theBoard
	      
printBoard(theBoard)
'''theBoard={'top-R':'O','top-M':'O','top-L':'O',\
	      'mid-L':'X','mid-M':'X','mid-R':' ',\
	      'low-R':'X','low-M':' ','low-L':' '}
	      
printBoard(theBoard)
	      

type(theBoard)
type('hello')
	      
''' 
