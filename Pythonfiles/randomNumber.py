import random

#need to pick a number between 1 and 100
#tells the user if guess was too high or two low 
#tells number of times guessed < NAAAAAAAAAAAAAAWWWWWWWWWWWWW BRO 
 #^only 1 try if same number 

#generate a number
secret_number = random.randint(1, 100)
print secret_number
guesses = 0 #Initialize a variable to store how many guesses the user has used

#get a number 
player_num = raw_input("Guess a whole number between 1 and 100 ")

#evaluate if guess is correct
while player_num != secret_number:
	#number too high
	if player_num < secret_number:
		player_num = input("Sorry, my number is higher then that. Guess again. ")

	#number too low 
	elif player_num > secret_number:
		player_num = input("Sorry, my number is lower then that. Guess again. ")
	#???
	elif:
		player_num = int(user_guess)
	#the needed except 
	#except:
		#print("\n") 	
	#not between 1-100:
	elif player_num < 0: 
		player_num = input("Sorry, that number is not betweeen 1 and 100 ")
	elif player_num > 101:
			player_num = input("that number is above 100 ")
	guesses+=1

#winner ding dig ding 
else:
	print("CONGRATULATIONS! YOU GUESSED MY NUMBER, {}.".format(secret_number))
	print("You took {} guesses!".format(guesses))

	
