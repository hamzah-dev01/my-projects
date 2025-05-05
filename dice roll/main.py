import random

while True:
 user = input("roll the dice? (y/n) ").lower().strip()
 if user == 'y':
  die1 = random.randint(1,6)
  die2 = random.randint(1,6)
  print(f'({die1},{die2})')
 elif user == 'n':
  print('Thanks for playing')
  break
 else:
  print ('invalid entry, try using "y" or "n" ')


     
 

