
import pyttsx3
import os



engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()

print('''

Hello World
Hi
Dummy
    

''')



directory = '/movie'

contents = os.listdir(directory)

for item in contents:
    print(item)