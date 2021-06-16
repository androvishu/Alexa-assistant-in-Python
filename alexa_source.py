import datetime
import speech_recognition as sr
import pyttsx3
import pyjokes
import pywhatkit
import wikipedia
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
l = sr.Recognizer()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def weekday(number):
    if number == 0:
        return "Monday"
    elif number == 1:
        return "Tuesday"
    elif number == 2:
        return "Wednesday"
    elif number == 3:
        return "Thursday"
    elif number == 4:
        return "Friday"
    elif number == 5:
        return "Saturday"
    elif number == 6:
        return "Sunday and today is holiday let's enjoy your day sir"


def open_pc_programs(str):
    pass


def open_wed_page(str):
    string = str.replace("open ", "")
    webbrowser.open(f"http://{string}.com/")


def take_command():
    # command = input("enter here: ")
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = l.listen(source)
            command = l.recognize_google(voice)
            command = command.lower()

            ## just print the command in the terminal
            # print(command)

            if "alexa" in command:
                command = command.replace('alexa ', '')
                print(f"User say: {command}")

    except Exception as e:
        return "None"
    return command


def run_alexa():
    command = take_command()
    if 'how are you' in command:
        talk("every think is fine and what about you sir")
    elif 'your name' in command:
        talk("sir my name is alexa")
    elif 'i love you' in command:
        talk("i love you too. will you marry me sir")
    elif 'play' in command:
        song = command.replace('play', '')
        talk(f"playing... {song}")
        pywhatkit.playonyt(command)
    elif 'wikipedia' in command:
        wiki = command.replace('wikipedia', '')
        result = wikipedia.summary(wiki, sentences=2)
        print(result)
        talk(result)
    elif 'open' in command:

        open_wed_page(command)

    elif 'joke' in command:
        joke = pyjokes.get_joke(language='en', category='neutral')
        print(joke)
        talk(joke)
    elif 'time' in command:
        currect = datetime.datetime.now().strftime("%I:%M %p")
        print(currect)
        talk(f"time is {currect}")
    elif 'date' in command:
        d = datetime.datetime.now().date()
        print(f"Today date is {d}")
        talk(f"Today date is {d}")
    elif 'day' in command:
        d = int(datetime.datetime.now().weekday())
        day_name = weekday(d)
        print(f'{day_name} sir')
        talk(f'{day_name} sir')
    elif 'sleep' in command:
        talk("have a good day sir")


    else:
        pass


while True:
    run_alexa()
