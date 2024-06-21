import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLib
import urllib.parse
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsApi = "https://newsapi.org/v2/top-headlines?country=us&apiKey=a855e1f4c89c47408ef85a31712eee5c"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processCmd(cmd):
    print(cmd)
    
    # Plays the songs present in the mnusicLib file
    if cmd.lower().startswith("play"):
        song = cmd.lower().split(" ", 1)[1]
        songLink = musicLib.music[song]
        if songLink:
            webbrowser.open(songLink)
        else:
            speak("I couldn't find the song in the music library.")
            
    # Spotify search karne ke liye
    elif "search spotify for" in cmd.lower():
        search_query = cmd.lower().split("search spotify for", 1)[1].strip()
        if search_query:
            webbrowser.open(f"https://open.spotify.com/search/{search_query}")
        else:
            speak("Please specify what you want to search on Spotify.")
    
    # Google search karne ke liye
    elif "google" in cmd.lower():
        search_query = cmd.lower().split("google", 1)[1].strip()
        if search_query:
            # Encode the search query for use in URL
            encoded_query = urllib.parse.quote(search_query)
            webbrowser.open(f"https://www.google.com/search?q={encoded_query}")
        else:
            speak("Please specify what you want to search on Spotify.")
        
    # YouTueb serach karte h
    elif "search youtube for" in cmd.lower():
        # Extract the search query after "youtube"
        search_query = cmd.lower().split("search youtube for", 1)[1].strip()
        if search_query:
            encoded_query = urllib.parse.quote(search_query)
            webbrowser.open(f"https://www.youtube.com/results?search_query={encoded_query}")
        else:
            speak("Please specify what you want to search on YouTube.")
    
    elif "youtube for" in cmd.lower():
        # Extract the search query after "youtube"
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
        webbrowser.open("www.linkedin.com/in/abhishek14104")
        
    elif "instagram" in cmd.lower() or "insta" in cmd.lower():
        webbrowser.open("https://www.instagram.com/")
        
    elif "rels" in cmd.lower() or "Rels" in cmd.lower():
        webbrowser.open("https://www.instagram.com/reels/")
        
    elif "movie" in cmd.lower() or "movies" in cmd.lower() or "film" in cmd.lower():
        webbrowser.open("https://hdtoday.tv/")
        
    elif "news" in cmd.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=a855e1f4c89c47408ef85a31712eee5c")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])  
            for article in articles:
                print(article['title'])
                speak(article['title'])
    
    else:
        # Agar OPEN API ko integrate karna ho to yahi karna h
        pass
    
    
    
if __name__ == "__main__":
    speak("Ram Ram sir, how can I help you?")
    
    # while true se hamesha run karega code
    while True:
        r = sr.Recognizer()
            
        # recognises your command with the use of google
        try:
            with sr.Microphone() as source:
            # Microphone is used as source of input in the below lines
                print("Listning to you Sir....")
                audio = r.listen(source, timeout=2 , phrase_time_limit=1 )
           
            wake_up_word = r.recognize_google(audio)
            print(wake_up_word)
            if "Jarvis" in wake_up_word or "jarvis" in wake_up_word:
                speak("Yes Sir. How can I assist you?")
                
                with sr.Microphone() as source:
                    print("Jarvis Acive...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                processCmd(command)
                
        except sr.UnknownValueError:
            print("Jarvis could not understand you Sir")
        except sr.RequestError as e:
            print("Jarvis error; {0}".format(e))
        except sr.WaitTimeoutError:
            print("Listining again..")