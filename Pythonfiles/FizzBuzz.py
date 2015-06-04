def fizzbuzz(number):
	#Function 
    if number % 3 == 0 and number % 5 == 0:
    	#Wow ok remember those % signs. (divided?)
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
    	#end the loop 
        return number

for number in range(1, 101):
    print fizzbuzz(number)
    #Don't forget to print 