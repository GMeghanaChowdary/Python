import pyttsx3
def text_to_speech():
    engine = pyttsx3.init()
    text = input("Enter text to convert to speech: ")
    engine.say(text)
    engine.runAndWait()
text_to_speech()
