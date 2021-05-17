import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speech_recognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser  # pip install webbrowser
import subprocess  # pip install subprocess

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)

            command = command.lower()


    except:
        pass
    return command


def run_computer():
    command = listen_command()
    print(command)
    if 'computer' in command:
        command = command.replace('computer', '')

        if 'what time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
            print(command)
        elif 'what is' in command:
            talk('Searching...')
            command = command.replace("what is", "")
            results = wikipedia.summary(command, sentences=2)
            print(results)
            talk("According to wikipedia" + results)
        elif 'open google' in command:
            talk("Opening google")
            subprocess.Popen('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
        elif 'search google' in command:
            command = command.replace('computer', ' ')
            command = command.replace('search', ' ')
            command = command.replace('google', ' ')
            webbrowser.open("https://google.com/search?q=%s" % command)
        elif 'open youtube' in command:
            webbrowser.open("https://youtube.com")
        elif 'search youtube' in command:
            command = command.replace('computer ', ' ')
            command = command.replace('search ', ' ')
            command = command.replace('youtube ', ' ')
            webbrowser.open("https://youtube.com/results?search_query=" + command)
        else:
            talk("Please repeat the command")
            print("Please repeat the command")
    else:
        return



while True:
    run_computer()