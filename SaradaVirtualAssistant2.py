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
		root.geometry('1024x768')
		root.resizable(0,0)
		#root.iconbitmap("vegeta.gif")
		
		
		img = ImageTk.PhotoImage(Image.open("assistant.gif"))
		panel = Label(root, image = img)
		panel.pack(side="top",fill="x",expand="no")
		
		
		self.compText = StringVar()
		self.userText   = StringVar()
		
		self.userText.set('Click \'Start Listening\' to Give Commands')
		
		userFrame = LabelFrame(root,text="SANKALP",font=('Black ops one',10,'bold'))
		userFrame.pack(side="left")
		
		left2 = Message(userFrame,textvariable=self.userText,bg="green",fg='black')
		left2.config(font=("Comic Sans MS",15,'bold'))
		left2.pack(side="left")
		
		compFrame = LabelFrame(root,text="SARADA",font=('Black ops one',10,'bold'))
		compFrame.pack(side="right")
		
		left1 = Message(compFrame,textvariable=self.compText,bg="green",fg='black')
		left1.config(font=("Comic Sans MS",15,'bold'))
		left1.pack(side = "right")
		
		btn   = Button(root,text='Start Listening!',font=('Black ops one',20,'bold'),bg='Blue',fg='Blue',command=self.clicked).pack(side="left")
		
		btn2 = Button(root,text='Close!',font=('Black ops one',20,'bold'),bg='Blue',fg='Red',command=root.destroy).pack(side="right")
		
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
		
		elif 'bye' in query:
			self.compText.set('Bye ' + 'Sankalp' + ', Have a good day.' + 'I will take a nap for sometime')
			speak('Bye ' + 'Sankalp' + ', Have a good day.' + 'I will take a nap for sometime')
		
		elif 'what can you do' in query:
			self.compText.set('Here are the two things that I can do for now Sankalp. I can open websites for you. I can also search information on wikipedia for you' )
			speak('Here are the two things that I can do for now Sankalp. I can open websites for you. I can also search information on wikipedia for you')
		
		elif 'open a website' in query:
			self.compText.set("Sure Sankalp. Which website do you want me to open for you?")
			speak("Sure Sankalp. Which website do you want me to open for you?")
			query = myCommand()
			self.userText.set('Listening...')
			self.userText.set(query)
			query = query.lower()
			self.compText.set("Sure Sankalp. I will open " + query + " site for you in a second")
			speak('Sure Sankalp. I will open ' + query + ' site for you in a second')
			webbrowser.open('https://' + query + '.com')
		
		elif 'i need some information' in query:
			self.compText.set("About what Sankalp?")
			speak("About what Sankalp?")
			query = myCommand()
			self.userText.set('Listening...')
			self.userText.set(query)
			query = query.lower()
			self.compText.set("Sure Sankalp. I will tell you about " + query + " in a second")
			speak("Sure Sankalp. I will tell you about " + query + " in a second")
			speak("'" + wikipedia.summary(query,sentences=2) + "'")
		



if __name__ == '__main__':
	
	greetMe()
	widget = Widget()
	

