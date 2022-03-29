import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser as wb


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'chandigarh university' in command:
        person = command.replace('chandigarh University', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, Do it yourself')
    elif 'are you single' in command:
        talk('I am in a relationship with  ayushwifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'speed' in command:
        import Speedtest        
    elif 'set alarm' in command:
        import alarmclock  
    elif 'news' in command:
        import News
          
    elif 'weather' in command:
        import Weather 
    elif 'market' in command:
        import Stocks    
    elif 'developers' in command: 
        talk('Sahil,Ravi,Ayush,Devendra')
    elif 'vaccine' in command:
            import vaccine 
    elif "covid" in command:
            talk("Opening covidstats")
            wb.open(' https://covid19tracker-af4d0.web.app/')
    elif "project" in command:
            talk("Project Details")
            wb.open('https://plump-economy.000webhostapp.com/ ')
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
