import re
import time
from datetime import datetime, date
import calendar
import pyttsx3
import serial
import speech_recognition as sr

engine = pyttsx3.init()

port = 'COM6'   #Identify Computer port
baud = '9600'   #Signal Rate

ser = serial.Serial(port, baud)


def speak(audio):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    # rate = engine.getProperty("rate")
    engine.setProperty("rate", 170)
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print('Listening')
            r.pause_threshold = 1
            audio = r.listen(source)
            print('Recognizing')

            command = r.recognize_google(audio, language='en-in')
            print(command)
    except Exception as ex:
        print(ex)
        return 'none'
    return command


def greeting():
    speak("Yes Sir")
    # speak("Hello Sir i am your personal assistant")


if __name__ == '__main__':
    flag = 0
    while True:
        command = takecommand().lower()

        # if 'available' in command:
        if re.search('terminator', command):
            flag = 1
            greeting()

        elif 'bedroom light on' in command or 'bedroom lights on' in command and flag == 1:
            speak("bedroom light turned on")
            ser.write(b'a')

        elif 'bedroom light off' in command or 'bedroom lights off' in command and flag == 1:
            speak("bedroom light turned off")
            ser.write(b'A')

        elif 'living room light on' in command or 'living room lights on' in command and flag == 1:
            speak("living room light turned on")
            ser.write(b'b')

        elif 'living room light off' in command or 'living room lights off' in command and flag == 1:
            speak("living room light turned off")
            ser.write(b'B')

        elif 'study room light on' in command or 'study room lights on' in command and flag == 1:
            speak("study room light turned on")
            ser.write(b'c')

        elif 'study room light off' in command or 'study room lights off' in command and flag == 1:
            speak("study room light turned off")
            ser.write(b'C')

        elif 'storage room light on' in command or 'storage room lights on' in command and flag == 1:
            speak("storage room light turned on")
            ser.write(b'd')

        elif 'storage room light off' in command or 'storage room lights off' in command and flag == 1:
            speak("storage room light turned off")
            ser.write(b'D')

        elif 'turn on lights' in command or 'turn on light' in command and flag == 1:
            speak("lights turned on")
            ser.write(b'a')
            ser.write(b'b')
            ser.write(b'c')
            ser.write(b'd')

        elif 'turn off lights' in command or 'turn off light' in command and flag == 1:
            speak("lights turned off")
            ser.write(b'A')
            ser.write(b'B')
            ser.write(b'C')
            ser.write(b'D')

        elif 'time' in command and flag == 1:
            t = time.localtime()
            current_time = time.strftime("%I:%M %p", t)
            speak(current_time)

        elif 'day' in command and flag == 1:
            curr_date = date.today()
            speak(calendar.day_name[curr_date.weekday()])

        elif 'date' in command and flag == 1:
            date = datetime.now()
            today = date.today()
            d2 = today.strftime("%B %d, %Y")
            speak(d2)

        elif 'terminate' in command and flag == 1:
            speak("Take Care")
            quit()