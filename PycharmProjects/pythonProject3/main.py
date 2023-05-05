import speech_recognition as sr
import playsound
import googletrans
import pyttsx3
import gtts
import os
engine = pyttsx3.init()


rate = engine.getProperty('rate')
engine.setProperty('rate',150)
volume=engine.getProperty('volume')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say("Please say to translator we will translate it....")
engine.runAndWait()

recognizer = sr.Recognizer()
translator = googletrans.Translator()
input_lang = 'en'
output_lang = 'te'
try:
   with sr.Microphone() as source:
    print('Please speak now')
    voice = recognizer.listen(source)
    command = recognizer.recognize_google(voice, language=input_lang)
    print(command)

    translated = translator.translate(voice, dest=output_lang)
    print(translated.text)
    converted_audio = gtts.gTTS(translated.text, lang=output_lang)
    converted_audio.save('voice.mp3')
    playsound.playsound('voice.mp3')
except sr.UnknownValueError:
  print("Unable to recognize speech")
except sr.RequestError as e:
   print("Request error; {0}".format(e))
except Exception as e:
   print("Error during translation: {0}".format(e))