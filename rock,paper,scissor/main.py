import random 
emojis = {'r': '🪨', 's':'✂️', 'p':'📄'}
choices = ('r','p','s')
playing = True
while playing:

    user_choice = input('what do you want to choose (r/p/s) ').lower().strip()
    com_choice = random.choice(choices)

    if user_choice not in choices:
        print ('invalid choice, please try again')
        continue

    print (f'you chose {emojis[user_choice]}')
    print (f'computer chose {emojis[com_choice]}')

    if user_choice == com_choice:
        print('its a draw')
    elif (
    (user_choice == 'r' and com_choice == 's') or
    (user_choice == 'p'and com_choice == 'r') or
    (user_choice == 's'and com_choice == 'p')):
        print ('you won')
    else:
        print ('you lost')

    play_again = input('do you want to play again (y/n) ').lower()
    if play_again == 'n':
        print('Thanks for playing')
        break
    
    