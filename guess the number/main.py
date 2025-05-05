import random

random_number = random.randint(1,100)
while True:
    try:
        user = int(input("Guess the number between 1 and 100 ---> "))
        if user < random_number:
            print("you're guessing lower than the expected one, try again!")
        elif user > random_number:
         print("you're guessing higher than the expected one, try again!")
        else:
         print ('well done!, you guessed right')
         break
    except:
     print("please enter a number")