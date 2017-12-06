#!/usr/bin/python3

import sys
from math import floor

def print_help():
	help_text = """ Welcome in help of evil_tomcat script.
	Description:
	The  evil tomcat python script eats frightened mice, which stand in a queue, one  after  other.
	The evil tomcat eats the first of them and puts the second mouse on the end of queue. 
	Script takes a number of mice and returns serial number of mouse, which will be eaten as the last.

	usage: ./evil_tomcat.py [ARGUMENTS]

	ARGUMENTS:
	n 			number of mouses in the queue, has to be positive whole number (non-zero)
	--help 		for help
	"""
	print(help_text)
	sys.exit(0)

def recursive_evil_tomcat(lst,flag):
	if (len(lst) == 1):
		return lst[0]

	#append every second item, and depends if you ends before this on odd or even index
	new_lst = [lst[x] for x in range(len(lst)) if ((x+flag)%2==1)]
	
	#second parameter in recursion means, you  will know where to start next iteration on odd or even index,
	#from the sum of the last and this iteration and doesn't need more values than 0,1 so mod 2
	#for ex. 11 -> 2,4,6,8,10 on indexes from 12 until 16 -> 2,6,10 on idexes fom 17 until 19 -> 6 result
	result = recursive_evil_tomcat(new_lst,(len(lst)%2+flag)%2) 
	return result 

def evil_tomcat(argv):
	if (len(argv) == 1 and argv[0].isdigit()):
		n = int(argv[0])
		if (n == 0):
			sys.stderr.write("Please put positive non zero number\n")
			sys.exit(1)
		elif (n == 1):
			return 1
		lst = [(i+1)*2 for i in range(floor(n/2))]  #list starts from 1 and every even mouse will stay alive and goes to the of queue
		result = recursive_evil_tomcat(lst,n%2)
		return result

	elif(len(argv) == 1 and argv[0] == "--help"):
		print_help()
	else:
		sys.stderr.write("Wrong arguments for more information, use ./evil_tomcat.py --help\n")
		sys.exit(1)


if __name__ == "__main__":
	result = evil_tomcat(sys.argv[1:])
	print(result)
