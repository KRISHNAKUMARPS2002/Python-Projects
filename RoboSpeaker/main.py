import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("Welcome To RoboSpeaker Created by Krishna Kumar")
    while True:
        x = input("Enter what you want to speak (enter 'q' to quit): ")
        if x.lower() == "q":
            speak("bye bye friend")
            break
        speak(x)
