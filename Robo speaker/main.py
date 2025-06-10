import pyttsx3

if __name__ == '__main__':
    print('Welcome to Robo-Speaker 1.1 "Created by !HumxuH!"')
    print('NOTE: Type "q" to exit the program')

    engine = pyttsx3.init()

    while True:
        x = input("Enter what you want Robo to speak: ")
        if x == "q":
            engine.say("Program exited")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()