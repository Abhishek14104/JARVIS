import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLib  # Ensure this library is correctly implemented
import urllib.parse
import requests
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import openpyxl

recognizer = sr.Recognizer()

# Initialize the pyttsx3 engine
engine = pyttsx3.init()  

newsApi = "https://newsapi.org/v2/top-headlines?country=us&apiKey=a855e1f4c89c47408ef85a31712eee5c"

EMAIL_ADDRESS = 'pythontesting14104@gmail.com'
EMAIL_PASSWORD = 'type your app password'

def speak(text):
    engine.say(text)
    engine.runAndWait()
    print(f"Jarvis said: {text}")  # Print statement for debug
    
def searchNameInExcel(name):
    try:
        df = pd.read_excel('list.xlsx')
        if 'Name' in df.columns and 'Email' in df.columns:
            matchingRow = df[df['Name'].str.lower() == name.lower()]
            if not matchingRow.empty:
                email = matchingRow.iloc[0]['Email']
                speak(f"{name} is found in list and their email is {email}.")
                return email
            else:
                speak(f"{name} is not found in the list.")
                return None
        else:
            speak("The columns 'Name' and/or 'Email' do not exist in the Excel file.")
            return None
    except FileNotFoundError:
        speak("The file 'list.xlsx' was not found.")  # Consistent file name
        return None
    except Exception as e:
        speak(f"An error occurred: {e}")
        return None

# Add the listen_for_audio function to handle speech input
def listen_for_audio(recognizer, prompt):
    speak(prompt)
    with sr.Microphone() as source:
        print(prompt)
        audio = recognizer.listen(source)
    return recognizer.recognize_google(audio)

def sendEmail(recipientEmail, recipientUserName):
    recognizer = sr.Recognizer()  # Create a recognizer instance
    
    try:
        confirmation = listen_for_audio(recognizer, f"Are you sure you want to send an email to {recipientUserName}?")
        print(f"Confirmation: {confirmation}")
        
        if 'cancel' in confirmation.lower():
            speak("Email sending cancelled.")
            return
        
        if 'yes' not in confirmation.lower() and 'yup' not in confirmation.lower() and 'send it' not in confirmation.lower():
            speak("Email sending cancelled.")
            return

        subject = listen_for_audio(recognizer, f"What should be the subject of the email to {recipientUserName}?")
        print(f"Subject: {subject.capitalize()}")
        
        if 'cancel' in subject.lower():
            speak("Email sending cancelled.")
            return

        body = listen_for_audio(recognizer, f"What should be the body of the email to {recipientUserName}?")
        print(f"Body: {body.capitalize()}")
        
        if 'cancel' in body.lower():
            speak("Email sending cancelled.")
            return
        
        final_confirmation = listen_for_audio(recognizer, f"Please confirm! that you want to send an Email to {recipientUserName} with the subject '{subject}' and the message '{body}'")
        print(f"Final Confirmation: {final_confirmation}")
        
        if 'cancel' in final_confirmation.lower():
            speak("Email sending cancelled.")
            return
        
        if 'yes' not in final_confirmation.lower() and 'yup' not in final_confirmation.lower() and 'send it' not in final_confirmation.lower():
            speak("Email sending cancelled.")
            return
        
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipientEmail
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        s.sendmail(EMAIL_ADDRESS, recipientEmail, msg.as_string())
        
        speak("Email sent successfully.")
        print(f"Email sent to {recipientEmail} named as {recipientUserName}")
        s.quit()
        
    except Exception as e:
        print(f"An error occurred: {e}")

def processCmd(cmd):
    # print(f"Command received: {cmd}")  
    
    if any(phrase in cmd.lower() for phrase in ["send mail to", "send an email to", "send email to", "send a mail to"]):
        name = None
        for phrase in ["send mail to", "send an email to", "send email to", "send a mail to"]:
            if phrase in cmd.lower():
                name = cmd.lower().split(phrase, 1)[1].strip()
                break
    
        if name:
            email = searchNameInExcel(name)
            if email:
                sendEmail(email, name)
            else:
                speak("Email not found for the specified name.")
        else:
            speak("Please specify the recipient's name.")

    # Handle other commands (not relevant for speech)
    # Add your command handling logic here
    elif cmd.lower().startswith("play"):
        song = cmd.lower().split(" ", 1)[1]
        songLink = musicLib.music.get(song)  # Ensure musicLib is implemented
        if songLink:
            webbrowser.open(songLink)
        else:
            speak("I couldn't find the song in the music library.")
            
    elif "search spotify for" in cmd.lower():
        search_query = cmd.lower().split("search spotify for", 1)[1].strip()
        if search_query:
            webbrowser.open(f"https://open.spotify.com/search/{search_query}")
        else:
            speak("Please specify what you want to search on Spotify.")
    
    elif "google" in cmd.lower():
        search_query = cmd.lower().split("google", 1)[1].strip()
        if search_query:
            encoded_query = urllib.parse.quote(search_query)
            webbrowser.open(f"https://www.google.com/search?q={encoded_query}")
        else:
            speak("Please specify what you want to search on Google.")
        
    elif "search youtube for" in cmd.lower():
        search_query = cmd.lower().split("search youtube for", 1)[1].strip()
        if search_query:
            encoded_query = urllib.parse.quote(search_query)
            webbrowser.open(f"https://www.youtube.com/results?search_query={encoded_query}")
        else:
            speak("Please specify what you want to search on YouTube.")
    
    elif "youtube for" in cmd.lower():
        search_query = cmd.lower().split("youtube for", 1)[1].strip()
        if search_query:
            encoded_query = urllib.parse.quote(search_query)
            webbrowser.open(f"https://www.youtube.com/results?search_query={encoded_query}")
        else:
            speak("Please specify what you want to search on YouTube.")
    
    elif "how are you" in cmd.lower():
        speak("I am Good, thank you for asking")
        
    elif "facebook" in cmd.lower():
        webbrowser.open("https://facebook.com")
        
    elif "linkedin" in cmd.lower():
        webbrowser.open("https://www.linkedin.com/in/abhishek14104")
        
    elif "instagram" in cmd.lower() or "insta" in cmd.lower():
        webbrowser.open("https://www.instagram.com/")
        
    elif "rels" in cmd.lower() or "Rels" in cmd.lower():
        webbrowser.open("https://www.instagram.com/reels/")
        
    elif "movie" in cmd.lower() or "movies" in cmd.lower() or "film" in cmd.lower():
        webbrowser.open("https://hdtoday.tv/")
        
    elif "news" in cmd.lower():
        r = requests.get(newsApi)
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])  
            for article in articles:
                print(article['title'])
                speak(article['title'])
    
    else:
        pass

if __name__ == "__main__":
    speak("Ram Ram sir, how can I help you?")
    
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening to you Sir....")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
           
            wake_up_word = r.recognize_google(audio)
            print(f"{wake_up_word}")  # Print statement for debug
            if "Ram" in wake_up_word or "ram" in wake_up_word:
                speak("Yes Sir. How can I assist you?")
                
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f"Command recognized: {command}")  # Print statement for debug
                    
                processCmd(command)
                
        except sr.UnknownValueError:
            print("Jarvis could not understand you Sir")
        except sr.RequestError as e:
            print(f"Jarvis error; {e}")
        except sr.WaitTimeoutError:
            print("Listening again..")
