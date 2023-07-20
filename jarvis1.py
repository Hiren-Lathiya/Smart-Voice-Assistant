import pyttsx3 #pip install pyttsx3
import datetime 
import speech_recognition as sr  #pip install speechRecognition
import pyaudio
import wikipedia
import smtplib
import webbrowser as wb 
import psutil #for cpu and battry
import pyjokes 
import os 
import pyautogui #screenshot
import json
import requests
from urllib.request import urlopen
import wolframalpha 
import time 
import pywhatkit as kit 






engine=pyttsx3.init()
#engine.say('hello hiren royaal') #TEXT TO SPEECH
#engine.runAndWait()

wolframalpha_app_id='RLXQV6-7KL7J93R6W'

#SPEAK FUNCCTION
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#TIME FUNCTION
def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S") #24hr time formate
    speak("Current time is")
    print("Current time=",Time)
    speak(Time)

#time_()


#DATE FUNCTION
def date_():
    year= datetime.datetime.now().year
    month=datetime.datetime.now().month 
    date=datetime.datetime.now().day
    print(f"Current date=",date , month  , year) 
    speak("current date is")
    speak(date)
    speak(month)
    speak(year)
#date_()


#SEND MAILS
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'password')
    server.sendmail('your email id',to,content)
    server.close()

def joke():
    speak('okay,telling you joke:')
    speak(pyjokes.get_joke())

def screnshot():
    img=pyautogui.screenshot()
    img.save(r'C:\Users\VAIBHAV\Desktop\BE\7th\jarvis\ss.png') 
    speak('taking screnshot done sir')

#GREETING FUNCTION
def wishme():
    speak('welcome back mr. hiren bhhai')
    speak('keeeem chooow  ??? majaa ma')
    time_()
    date_()

    #greeting logic
    hour=datetime.datetime.now().hour 
    if hour>=6 and hour<12:
       speak("Good morning Hiren")
       print("Good morning Hiren")

    elif hour>=12 and hour<18:
        print("Good after noon Hiren")
        speak("Good after noon Hiren")
        
    elif hour>=18 and hour<24:
        print('good evening hiren')
        speak('good evening hiren')
        
    else:
        print('Good night Hiren')
        speak('Good night Hiren')
        
    print("Your assistant JARVIS is at your service. Please Tell me How can i help You Today? ")

    speak("Your assistant JARVIS is at your service. Please Tell me How can i help You Today? ")

#wishme()



def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print('Listning......')
        #r.pause_threshold=1
        audio = r.listen(source,phrase_time_limit=6)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language="en-US")
        print(query)
    except Exception as e:  
        print(e)
        print("Say that again please.... ")
        speak("i dont recognize Say that again please.... ")
        return 'none'
    return query

def cpu():
    usage=str(psutil.cpu_percent())
    speak('cpu is at'+usage)
    print('cpu is at'+usage)

    battery=psutil.sensors_battery()
    speak('Bettry is at')
    print('Bettry is at')
    print(battery.percent)
    speak(battery.percent)




def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('vaibhavpatel727@gmail.com', 'password')
    server.sendmail('vaibhavpatel727@gmail.com',to,content)
    server.close()

if __name__== '__main__' :

    wishme()

    while True:
        query=TakeCommand().lower()
        #all commands will be stored in lower case in query

        if 'time' in query:  #calling time function
            time_()

        elif 'date' in query:  #calling date function
            date_()

        # elif 'chrome' in query:
        #     try:
        #         speak('What should i Search')
        #         chromepath='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        #         search=TakeCommand().lower()
        #         wb.get(chromepath).open_new_tab(search)

        #     except Exception as e:
        #         print(e)
        #         speak('unable to search')

        
        elif 'wikipedia' in query:
            try:
                speak('Searching....')
                query=query.replace("wikipedia", " ")
                results=wikipedia.summary(query,sentences=3)
                speak('According to wikipedia...')
                print(results.encode('utf8'))
                speak(results)

            except Exception as e:
                print(e)
                speak('Sorry i am unable to find please Say again')

        elif 'mail' in query or "email" in query:
            try:
                speak("Pleas Tell me What should I Send?")
                content=TakeCommand()
                #speak('who is receiver?')
                #receiver=input(('enter email of receiver:'))
                receiver='hirenroyal123@gmail.com'
                to=receiver
                speak('sending mail please wait')
                sendEmail(to, content)
                speak(content)
                speak('email has been send.')
                print('email has been send.')
            except Exception as e:
                print(e)
                speak('Unable to send mail at a time.')

        elif 'youtube' in query:
            speak('What should i play ?')
            video=TakeCommand()
            speak('here we go to Youtube')
            wb.open('https://www.youtube.com/results?search_query='+video)

        elif 'google' in query or 'search' in query:
            speak('What should i Search ?')
            term=TakeCommand()
            speak('here we go to google')
            wb.open('https://www.google.com/search?q='+term)

        elif 'cpu' in query or 'Bettry' in query  or 'Battry' in query:
            cpu()

        elif 'joke' in query :
            joke()

        elif 'offline' in query:
            speak("Going offline sir!")
            quit()

        elif 'notepad' in query:
            speak('oppennig notepad sir!')
            notepad=r'C:\WINDOWS\system32\notepad.exe'
            os.startfile(notepad)

        elif 'msword' in query or 'word' in query :
            speak('oppennig notepad word!')
            word=r'C:\Program Files\Microsoft Office\Office16\WINWORD.EXE'
            os.startfile(word)

        elif 'excel' in query :
            speak('oppennig excel sir!')
            excel=r'C:\Program Files\Microsoft Office\Office16\EXCEL.EXE'
            os.startfile(excel)

        elif 'powerpoint' in query :
            speak('oppennig powerpoint sir!')
            pp=r'C:\Program Files\Microsoft Office\Office16\POWERPNT.EXE'
            os.startfile(pp)

        elif 'write note' in query or 'write' in query: 
            speak('what to write sir!')
            notes=TakeCommand()
            file=open('notes.txt','w')
            file.write(notes)
            speak('Done taking notes sir')


        elif 'show notes' in query or 'open notes' in query:
            speak('Showing notes')
            file=open('notes.txt','r')
            print(file.read())
        
        elif 'screenshot' in query:
            screnshot()

        elif 'music' in query or 'song' in query:
            song_directory= 'D:/Songs'
            music=os.listdir(song_directory)
            speak('okay playing song sir')
            os.startfile(os.path.join(song_directory, music[0]))

        elif 'garba' in query:
            song_directory= 'D:\\Songs\\Garba\\download'
            music=os.listdir(song_directory)
            speak('okay playing garba sir')
            os.startfile(os.path.join(song_directory, music[0]))

        elif 'remember that' in query:
            speak('What should i remember?')
            memory=TakeCommand()
            speak('you asked me to remember that'+memory)
            remember=open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember=open('memory.txt', 'r')
            speak('you ask me to remember that')
            speak(remember.read())

        elif  'where is' in query:
            query=query.replace('where is', "")
            location=query
            speak('You asked to locate '+location)
            wb.open_new_tab('https://www.google.com/maps/place/'+location)

        elif 'news' in query:
            try:
                jsonObj=urlopen('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=976989e3464f495a98f96055cf6009e2')
                data=json.load(jsonObj)
                i=1

                speak('here is some top headlines ')
                print(" ################## TOP HEADLINES ################# ")
                for k in data['articles']:
                    print(str(i)+'-'+k['title']+'\n')
                    print(k['description']+'\n')
                    speak(k['title'])
                    i += 1
                    if (i==5):
                        break

            except Exception as e:
                print(str(e))
        

        elif 'calculate' in query:
            client=wolframalpha.Client(wolframalpha_app_id)
            index=query.lower().split().index('calculate')
            query=query.split()[index + 1:]
            res=client.query(''.join(query))
            ans= next(res.results).text
            print('the answer is' +ans)
            speak('the answer is '+ans)


        elif 'what is' in query or 'who is' in query:
            client=wolframalpha.Client(wolframalpha_app_id)
            rest=client.query(query)

            try:
                print(next(rest.results).text)
                speak(next(rest.results).text)
            except StopIteration:
                print('No results')

        elif 'stop listening' in query or 'go to sleep' in query:
            speak('for how many seconds you want me to stop listning commands')
            ans=int(TakeCommand())
            time.sleep(ans)
            print(ans)

        elif 'log out' in query:
            os.system("shutdown -1")

        elif 'restart' in query:
            os.system('shutdown /r /t 1')

        elif 'shutdown' in query:
            os.system('shutdown /s /t 1')


 



        


        










        







        





