
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query
def screenshot():
    img = pyautogui.screenshot()
    img_path = os.path.expanduser(r"C:\Users\devar\OneDrive\Desktop\Jarvis-Desktop-Voice-Assistant-main\Jarvis-Desktop-Voice-Assistant-main\Images\li.png")
    img.save(img_path)
    
def play_music():
    song_dir = os.path.expanduser(r"C:\Users\devar\OneDrive\Desktop\Jarvis-Desktop-Voice-Assistant-main\Jarvis-Desktop-Voice-Assistant-main\Music")
    songs = [os.path.join(song_dir, song) for song in os.listdir(song_dir) if song.endswith(".mp3")]
    if songs:
        print(songs)
        song_to_play = random.choice(songs)
        os.startfile(song_to_play)
    else:
        speak("No music files found in the Music directory.")

if __name__ == "__main__":
    while True:
        query = takecommand().lower()
        if "time" in query:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time}")
            print(f"The time is {time}")
            break

        elif "date" in query:
            date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"The date is {date}")
            print(f"The date is {date}")
            break

        elif "who are you" in query:
            speak("I'm JARVIS created by Mr. Kishan and I'm a desktop voice assistant.")
            print("I'm JARVIS created by Mr. Kishan and I'm a desktop voice assistant.")
            break

        elif "how are you" in query:
            speak("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")
            break

        elif "fine" in query or "good" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")
            break

        elif "wikipedia" in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except wikipedia.exceptions.WikipediaException:
                speak("Can't find this page sir, please ask something else")
                break

        elif "open youtube" in query:
            wb.open("youtube.com") 
            break

        elif "open google" in query:
            wb.open("google.com") 
            break
   
        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")
            break

        elif "play music" in query:
            play_music()
            break


        elif "open chrome" in query:
            wb.open("chrome.exe")  # Open Chrome
            break

        elif "search on chrome" in query:
            try:
                speak("What should I search?")
                search_query = takecommand().lower()
                wb.open("https://www.google.com/search?q=" + search_query)
                print("Searching for:", search_query)

            except Exception as e:
                speak("Can't search at the moment, please try again later.")
                print("Can't search at the moment, please try again later.")
                break

            
        
        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
            break

        elif "do you remember anything" in query:
            remember = open("Jarvis-Desktop-Voice-Assistant-main/Jarvis/data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))
            break

        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")
            break

        elif "stop" in query:
            speak("Stopping the program.")
            print("Stopping the program.")
            break


