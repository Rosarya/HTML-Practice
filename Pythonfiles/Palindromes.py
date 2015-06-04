input_list = raw_input("Please input a word. ")

def palindrome(input_list):
	original = input_list
	palindrome = input_list[::-1]

	if palindrome == original:
		print "Your word is a palindrome"
	else:
		print "Your word is not a palindrome"

palindrome(input_list)