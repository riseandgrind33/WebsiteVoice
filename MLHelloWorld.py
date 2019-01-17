import speech_recognition as sr
import webbrowser as wb
import fbchat
import awscli
import public
import gtts

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak now!')
    audio = r.listen(source)
    print('Finished processing website request.')
try:
    text = r.recognize_google(audio)
    print('Sending you to:\t' + text)
    wb.get(chrome_path).open(text)

except Exception as e:
    print(e)
    
