import pyttsx3

machine=pyttsx3.init()
machine.say("HII THERE , I AM YOUR SPEAK BOT . ENTER HERE WHAT YOU WANT ME TO SPEAK")
machine.runAndWait()

speak = input('ENTER WHAT YOU WANT ME TO SPEAK =\t')
print(""+speak)
machine.say(""+speak)
machine.runAndWait()


machine=pyttsx3.init()
machine.say(" . , THANKS FOR USING ME ..!")
machine.runAndWait()

