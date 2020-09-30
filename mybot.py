
import speech_recognition as sr
import pyttsx3
import wolframalpha
import wikipedia
import webbrowser
import numpy

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak('Hey, I am Jane')

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        ask = r.recognize_google(audio, language='en-us')
        print(f"You said : {ask}")
    except Exception:
        print("Say that again...")
        return ""
    
    return ask

if __name__ == "__main__":
    while True:
        query = command().lower()
        print(query)

        try:
            if 'max' in query:
                query = query.replace('max', '')
                client = wolframalpha.Client("5AVVKV-9HTE4ERPRW") # Paste Your API Key Here....!!!
                res = client.query(query)
                ans = next(res.results).text
                print(ans)
                speak(ans)
        
        except Exception:
            try:
                query = query.replace('max', '')
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak(results)

            except Exception:
                try:
                    query = query.replace('max', '')
                    webbrowser.open('https://google.com/?#q=' + query)

                except:
                    print("I found nothing , you are mind flayer try again.....")
                    speak("I found nothing , you are mind flayer try again.....")




