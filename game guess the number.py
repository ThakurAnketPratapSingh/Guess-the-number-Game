f=open("game.txt","r+")
import random
a=random.randint(1,100)
name=input('Enter your name :- ')
f.write(name)
print('\nGuess the number 1 to 100\n')
print('Number of guesses is limited to only 9 times \n')
i=8
while(i>-1):
	print('***************************************************')
	try:
		n=int(input('Guess the number =  '))
		print()
	except Exception as e:
		print(f'plesae enter {e}')
		continue
	if(n>a):
		print('You enter greter number please enter less number\n')
	elif(n<a):
		print('You enter less number please enter greter number\n')
	else:
		print('YOU WIN\n')
		print(i,'number of guesses left\n')
		break
	
	print(i,'number of guesses left\n')
	i-=1
if(i==-1):
	print('***************************************************')
	print('GAME OVER\n')
	print('Guessing number = ',a)
f.close()