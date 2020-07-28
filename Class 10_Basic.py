

import random                                               #import the random function to ranndomly select a move for the computer.
print('Welcome to Rock Paper Scissor')                      
a =int(input('How many times do you want to play?: '))      #take in input in variable 'a' on the number of times the player wants to play.

l = 0                                                       #the variables l,w and t will record the wins and losses for the player and the computer.
w = 0
t = 0

for i in range(0,a):                                        #this is the loop where the game will be played, which will move the number of times the player wants to play.
    
    move = input('Your move: ')                             #take in input in variable 'move' on the move of the player.
    move = move.lower()                                     #makes the input lowercase.
    move = move.strip()                                     #mkaes the input spaces go away.
    print('You played', move)
    
    for j in range (1,10):
        move2 = random.randrange(1,4)
        if move2 == 1:
            move2 = 'rock'    
        elif move2 == 2:
            move2 = 'paper'     
        else:
            move2 = 'scissor'
        j+=1
        
    print('Computer Played', move2)
    
    if move == 'rock' and move2 == 'paper':
        print('You lose')
        l+=1
        
    elif move == 'rock' and move2 == 'scissor':
        print('You win')
        w+=1
        
    elif move == 'rock' and move2 == 'rock':
        print('You tied')
        t+=1
        
    elif move == 'paper' and move2 == 'scissor':
        print('You lose')
        l+=1  
        
    elif move == 'paper' and move2 == 'rock':
        print('You win')
        w+=1
        
    elif move == 'paper' and move2 == 'paper':
        print('You tied')
        t+=1  
        
    elif move == 'scissor' and move2 == 'rock':
        print('You lose')
        l+=1  
        
    elif move == 'scissor' and move2 == 'paper':
        print('You win')
        w+=1   
        
    elif move == 'scissor' and move2 == 'scissor':
        print('You tied')
        t+=1  
        
    else:
        print('Please input a valid try')
        
print()
print('Winning:',w)
print('Losing:',l)
print('Tied:',t)

w = w+t
l = l+t

print()

if w>l:
    print('You won the match!')
elif w==l:
    print('You tied the match!')
else:
    print('You lost the match!')
