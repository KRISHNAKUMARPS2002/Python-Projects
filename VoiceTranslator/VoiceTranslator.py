import googletrans
import speech_recognition
import gtts
import playsound

input_lang = "hi"
output_lang = "fr"

recognizer = speech_recognition.Recognizer()

# Run the code in a while loop until the user says "quit"
while True:
    with speech_recognition.Microphone() as source:
        print("Speak now")
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=input_lang)
        print(text)

    translator = googletrans.Translator()
    translation = translator.translate(text, dest=output_lang)
    print(translation.text)

    converted_audio = gtts.gTTS(translation.text, lang=output_lang)
    converted_audio.save("hello.mp3")
    playsound.playsound("hello.mp3")

    user_input = input("Type 'quit' to exit or press Enter to continue: ").lower()
    if user_input == "quit":
        print("Exiting the program.")
        break


