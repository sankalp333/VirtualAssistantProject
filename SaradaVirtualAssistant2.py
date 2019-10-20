from Tkinter import *
#from Tkinter import ttk
from PIL import ImageTk, Image
import speech_recognition as sr
import pyttsx3,os, datetime, sys, wikipedia, wolframalpha, os, smtplib, random, webbrowser, pygame, subprocess


#engine = pyttsx3.init()
#voices = engine.getProperty('voices')


def speak(audio):

	print('Sarada : ',audio)
#	engine.setProperty('voice',voices[len(voices)-1].id)
	#engine.say(audio)
	#engine.runAndWait()
	
	phrase = audio
	os.system("/usr/bin/say " + phrase)

def myCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)
	try:
		query = r.recognize_google(audio,language='en-in')
		print('User : ' + query + '\n')
		
	except sr.UnknownValueError:
		speak('Try again!')
		pass
	
	return query

def greetMe():
	currentH = int(datetime.datetime.now().hour)
	if currentH >=0 and currentH < 12:
		speak('Good Morning Sankalp! Give me a moment to get my systems ready.')
	
	if currentH >= 12 and currentH < 18:
		speak('Good Afternoon Sankalp!. Give me a moment to get my systems ready.')
	
	if currentH >= 18 and currentH != 0:
		speak('Good Evening Sankalp! Give me a moment to get my systems ready..')


class Widget:
	def __init__(self):
		root = Tk()
		root.title('Sarada(Version 1.0)')
		#root.config(background = 'Blue')
		root.geometry('350x600')
		root.resizable(0,0)
		#root.iconbitmap("vegeta.gif")
		img = ImageTk.PhotoImage(Image.open("jarvis.gif"))
		panel = Label(root, image = img)
		panel.pack(side="bottom",fill="both",expand="no")
		
		self.compText = StringVar()
		self.userText   = StringVar()
		
		self.userText.set('Click \'Start Listening\' to Give Commands')
		
		userFrame = LabelFrame(root,text="SANKALP",font=('Black ops one',10,'bold'))
		userFrame.pack(fill="both",expand="yes")
		
		left2 = Message(userFrame,textvariable=self.userText,bg='Green',fg='white')
		left2.config(font=("Comic Sans MS",10,'bold'))
		left2.pack(fill='both',expand='yes')
		
		compFrame = LabelFrame(root,text="SARADA",font=('Black ops one',10,'bold'))
		compFrame.pack(fill="both",expand="yes")
		
		left1 = Message(compFrame,textvariable=self.compText,bg='Magenta',fg='white')
		left1.config(font=("Comic Sans MS",10,'bold'))
		left1.pack(fill='both',expand='yes')
		
		btn   = Button(root,text='Start Listening!',font=('Black ops one',10,'bold'),bg='Blue',fg='Blue',command=self.clicked).pack(fill='x',expand='no')
		
		btn2 = Button(root,text='Close!',font=('Black ops one',10,'bold'),bg='Blue',fg='Red',command=root.destroy).pack(fill='x',expand='no')
		
		#speak('Hello, I am Sarada! What should I do for You?')
		self.compText.set('Hello I am Sarada! What should I do for you')
		
		root.bind("<Return>",self.clicked) #handle the enter key event of your keyboard
		root.mainloop()
	
	def clicked(self):
		print('Working')
		query = myCommand()
		self.userText.set('Listening...')
		self.userText.set(query)
		query = query.lower()
		#webbrowser.open('https:://www.youtube.com')
		
		if 'hello' in query:
			self.compText.set('What are you doing Sankalp?.')
			speak('What are you doing Sankalp?.')
		
		elif 'open youtube' in query:
			self.compText.set('okay')
			speak('Sure Sankalp. Watch only productive videos. Have fun!')
			webbrowser.open('https://www.youtube.com')
		
		elif 'bye' in query:
			self.compText.set('Bye ' + 'Sir' + ', have a good day.')
			speak('Bye ' + 'Sankalp' + ', Have a good day.' + 'I will take a nap for sometime')
		



if __name__ == '__main__':
	
	greetMe()
	widget = Widget()
	

