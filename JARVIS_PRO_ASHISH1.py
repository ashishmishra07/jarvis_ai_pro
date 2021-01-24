import pyttsx3
#import gtts
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os,time
engine = pyttsx3.init('sapi5') #windows gives an inbuit API which can be used to take voices
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Mister X sir, How may I help you")
def takeCommand():
    # it takes microphone input from the user and returns string output

    # Initialize the recognizer
    r = sr.Recognizer()


    with sr.Microphone() as source:
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source)
        print("Please say something...")
        time.sleep(1)
        print("listening...")
        # listens for the user's input
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio)
            print("you said: " + query)

            # error occurs when google could not understand what was said

        except sr.UnknownValueError:
            print("Sorry could not recognize your voice")

        except sr.RequestError as e:
            print("Could not recognize your request")
            return "None"
        return query
    #r = sr.Recognizer()
    #with sr.Microphone() as source:
       # print("Listening...")
        #r.pause_threshold = 1
       # audio = r.listen(source)
        #try:
         #   print("Recognizing...")
          #  query = r.recognize_google(audio, Language='en-in')
          #  print(f"User said: {query}\n")

        #except Exception as e:
            #print(e)
            #print("Please say that again...")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()  #the query/text will be converted into lower case and we can easily match it
        if "wikipedia" in query: #Logic for executing tasks based on query
            print("Searching wikipedia...")
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences= 2)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "college website" in query:
            webbrowser.open("sbsstc.com")

        elif "music" in query:
            music_dir = 'E:\\favorite songs' # double \\ is to escape characters
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))









