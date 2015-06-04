alist = [1, 2, 3, 4, 5, 6, 7]


def check(alist):
	check = input("What number is in the list? ")
	if check in alist:
		print "True"
	if check not in alist:
		print "False"
		
check(alist)

