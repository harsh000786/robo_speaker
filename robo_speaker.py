

import pyttsx3
e = pyttsx3.init()
if __name__== "__main__":
    print("Welcome to Robospeaker 1.1. created by Harsh")
    while (True):
        x = input("Enter what do you want to speak  ")
        if (x == "q"):
            e.say("bye bye friend")
            e.runAndWait()
            break
        e.say(x)
        e.runAndWait()

