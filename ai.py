import pyaudio
import speech_recognition as sr  
import smtplib
import webbrowser
import os

def voice1():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Welcome to voice assistent ");
        print("what is want to open site.... ")
        print("like.. shoping.. amazon /  medicin / book or other want to search")
        audio = r.listen(source)
        print("Times Up...")
    try:
        text = r.recognize_google(audio)
        k = ("{}".format(text))
        return k
    except:
        print("any problem")

def voice():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("now say")
        audio = r.listen(source)
        print("Times Up...")
    try:
        text = r.recognize_google(audio)
        k = ("{}".format(text))
        return k
    except:
        print("any problem")      
    
    

command = voice1()
from playsound import playsound


print (command)
if command == "amazon" or command == "shopping" or command == "shoppings":
	print("What item search")
	name = voice()
	print(name)
	prn = "https://www.amazon.in/s?k="
	print("opening " + name + "items")
	sear = prn+name
	webbrowser.open_new(sear)
if command == "medicin" or command == "dawa" or command == "medicins":
	print("What medicin search")
	name = voice()
	print(name)
	prn = "https://www.1mg.com/search/all?name="
	print("opening " + name + "medicin")
	sear = prn+name
	webbrowser.open_new(sear)    
else:
	print(command)
	prn = "https://www.google.com/search?rlz=1C1CHBF_enIN865IN865&ei=xNDEXcjNDYvLvgT74ZWYAQ&q="
	print("opening " + name + "in google")
	sear = prn+name
	webbrowser.open_new(sear)
