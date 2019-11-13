
from Tkinter import *
import Tkinter as tk
from PIL import ImageTk, Image
from itertools import count
import speech_recognition as sr
import pyttsx3,os, datetime, sys, requests,wikipedia, wolframalpha, os, smtplib, random, webbrowser, pygame, subprocess,re,urllib,urllib2,random
from bs4 import BeautifulSoup as soup
from urllib2 import urlopen


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

class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)




class Widget:

	def __init__(self):
		root = Tk()
		root.title('Sarada(Version 1.0)')
	        root.config(background = 'CadetBlue1')
		root.geometry('1024x768')
		root.resizable(0,0)
		#root.iconbitmap("vegeta.gif")

		#text = Text(root)
		#text.insert(INSERT,"Hello World....")
		#text.pack()


		#img = ImageTk.PhotoImage(Image.open("assistant.gif"))

		panel = ImageLabel(root)
		panel.pack(side="top",fill="x",expand="yes")

		panel.load("sarada.gif")


		self.compText = StringVar()
		self.userText   = StringVar()

		self.userText.set('Click \'Start Listening\' to Give Commands')

		userFrame = LabelFrame(root,text="SANKALP",font=('Black ops one',10,'bold'))
		userFrame.pack(side="left")

		left2 = Message(userFrame,textvariable=self.userText,bg="CadetBlue1",fg='black')
		left2.config(font=("Comic Sans MS",15,'bold'))
		left2.pack(side="left")

		compFrame = LabelFrame(root,text="SARADA",font=('Black ops one',10,'bold'))
		compFrame.pack(side="right")

		left1 = Message(compFrame,textvariable=self.compText,bg="CadetBlue1",fg='black')
		left1.config(font=("Comic Sans MS",15,'bold'))
		left1.pack(side = "right")

		btn   = Button(root,text='Start Listening!',font=('Black ops one',20,'bold'),bg='CadetBlue1',fg='Blue',command=self.clicked).pack(side="left")

		btn2 = Button(root,text='Close!',font=('Black ops one',20,'bold'),bg='CadetBlue1',fg='Blue',command=root.destroy).pack(side="right")

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
			self.compText.set('Here are the list of things that I can do for you Sankalp. ')
			speak('Here are the list of things that I can do for you Sankalp. ')
			root = Tk()
			# root.geometry("500x100+300+300")
			root.geometry("500x100")
			newwin = Toplevel(root)
			display = Label(newwin,text="1. Open any Website.\n 2. Send an email. \n.3. Tell you about almost anything\n4. Top News For Today!(Pending)\n5.Tell the current time\n6.Launch any system application\n7. Play you a song(Pending)\n8. Change your Desktop Wallpaper(Pending)\n 9. Maintain your phone numbers\n10.Motivate you :)\n ")
			display.pack()



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

		elif 'send an email' in query:
			self.compText.set('Sure Sankalp. For whom do you want me to send the mail to?')
			speak('Sure Sankalp. For whom do you want me to send the email?')
			query = myCommand()
			self.userText.set('Listening...')
			self.userText.set(query)
			query = query.lower()

			if 'john' in query:
				self.compText.set('What should I say to him?')
				speak('What should I say to him?')
				content = myCommand()
				mail = smtplib.SMTP('smtp.gmail.com',587)
				mail.ehlo()
				mail.starttls()
				mail.login('your email','your password')
				mail.sendmail('your email','your email',content)
				mail.close()
				self.compText.set("Sankalp, Email has been sent successfully. You can check your inbox.")
				speak("Sankalp, Email has been sent successfully. You can check your inbox.")

			else :
				self.compText.set("I don\'t know what you mean!")
				speak("I don\'t know what you mean!")



		#Pending(Can be improved further in case of multiple results being returned)
		elif 'tell me about' in query:

			self.compText.set("Sure Sankalp. What do you want to know about?")
			speak("Sure Sankalp. What do you want to know about?")
			query = myCommand()
			self.userText.set('Listening...')
			self.userText.set(query)
			query = query.lower()

			self.compText.set("Sure Sankalp. I tell you about " + query + "  in a second")
			speak("Sure Sankalp. I tell you about " + query + "  in a xssecond")

			ny = wikipedia.page(query)
			self.compText.set(ny.content[:500].encode('utf-8'))
			text = ny.content[:500].encode('utf-8')

			#speak(text)

		#Pending
		elif 'tell me some news' in query:
			try:
				news_url = "https://news.google.com/news/rss"
				Client = urlopen(news_url)
				xml_page=Client.read()
				Client.close()
				soup_page=soup(xml_page,"lxml")
				news_list=soup_page.findAll("item")
				for news in news_list[:15]:
					self.compText.set(ny.content[:500].encode('utf-8'))
					speak(news.title.text.encode('utf-8'))
			except Exception as e:
				print(e)

		
		elif 'what is the time' in query:
			self.userText.set('What is the time')
			now = datetime.datetime.now()
			speak('Current time is %d hours %d minutes ' % (now.hour,now.minute))
			self.compText.set('Current time is %d hours %d minutes ' % (now.hour,now.minute))


		elif 'open application' in query:
			self.userText.set('Open an application')
			speak('Sure Sankalp! Which application do you want me to open?')
			self.compText.set('Sure Sankalp! Which application do you want me to open?')
			query = myCommand()
			self.userText.set('Listening...')
			self.userText.set(query)
			query = query.lower()
			appname = query +".app"
			subprocess.Popen(["open","-n","/Applications/" + appname],stdout=subprocess.PIPE)

			speak("I have launched the desired application, Sankalp")

		# Pending - This can be improved further by adding the searching feature can be added later
		elif 'add a new phone number' in query:
			self.userText.set('Add a new phone number')
			speak('Sure Sankalp! What is the name of the contact that you want to add ?')
			self.compText.set('Sure Sankalp! What is the name of the contact that you want to add ?')
			query = myCommand()
			self.userText.set('Listening...')
			self.userText.set(query)
			query = query.lower()

			speak('Please tell me the phone number of ' + query + " ?")
			self.compText.set('Please tell me the phone number of ' + query + " ?")
			query2 = myCommand()
			self.userText.set('Listening...')
			self.userText.set(query2)
			query2 = query2.lower()

			speak('Okay Sankalp. I am going to Save the contact to the database')
			self.compText.set('Okay Sankalp. I am going to Save the contact to the database')
			f= open("phoneContacts.txt","a+")
			f.write(query + " " + query2)

			speak('Okay done, Sankalp. I have saved the contact to the database.')
			self.compText.set('Okay done, Sankalp. I have saved the contact to the database.')

		elif 'i need some motivation' in query:
			self.userText.set('I need some motivation')

			list = ['The Way Get Started Is To Quit Talking And Begin Doing.',
				   'The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees Opportunity In Every Difficulty.',
				   "Do not Let Yesterday Take Up Too Much Of Today.",
				   "You Learn More From Failure Than From Success. Donnot Let It Stop You. Failure Builds Character.",
				   "It is Not Whether You Get Knocked Down, It is Whether You Get Up."
				 ]

			rand = random.randrange(0, 5, 1)

			speak(list[rand])
			self.compText.set(list[rand])



if __name__ == '__main__':

	greetMe()
	widget = Widget()
