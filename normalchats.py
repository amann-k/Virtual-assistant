import speech_recognition as sr #for speech recognition
import pyttsx3 # text-to-speech
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer() #to recognize voice
engine = pyttsx3.init() # engine for virtual assistant to speak
voices = engine.getProperty("voices") #this will provide all voices text-to-speech can provide to variable voices
engine.setProperty('voice',voices[1].id)#setting up female voice of helen
def talk(text):
    engine.say(text)
    engine.runAndWait() # runs the above command and then waits for users voice command
def listen_command():
    try:
        with sr.Microphone() as source:  #to avoid any complications due to mic during recognition
                print("listening...")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)  #google api to convert speech to text
                command = command.lower()   # to check if helen is
                if 'helen':  #  mentioned in the first command
                    command = command.replace('helen','') #removes helen from command
                    print(command)
                else:
                    print("Sorry I didn't heard you")
    except:
        pass
    return command


def run_helen():
    command = listen_command()
    if 'play' in command:
        song = command.replace('play',' ') # removes play from command
        talk('playing' + song +'on youtube') # speaks the rest of command
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The time is' + time)
        print(time)
    elif 'date' in command:
        now = datetime.datetime.now()
        day = now.strftime('%A')
        date= str(now)[8:10]
        month = now.strftime('%B')
        year = str(now.year)
        result = f'{day},{date},{month},{year}'
        talk('Today is '+result)
        print(result)
    elif 'tell me about' in command:
        person = command.replace("tell me about",' ')
        info = wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'are you single' in command:
        print("Sorry, I'm in a relationship with wifi")
        talk("Sorry, I'm in a relationship with wifi")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    
    else:
        print("Please speak again. I didn't get it.")
        talk("Please speak again. I didn't get it.")


while True:
    run_helen()