import os.path
import webbrowser
from datetime import datetime

import speech_recognition as sr
from googlesearch import search

from Features import Weather, Greeting, Calender
from Questions import WeatherQuestions, GreetingQuestions, CalenderQuestions


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    said = ""
    try:
        said = r.recognize_google(audio)

    except Exception as e:
        print(e)

    return said


cont = True

while cont:
    question = listen()

    if question.strip() == "":
        continue

    elif question.strip() == "stop" or question.strip() == "exit":
        cont = False

    elif WeatherQuestions.current_location_questions.__contains__(question) or \
            question.__contains__("weather") or \
            question.__contains__("climate"):

        if question.__contains__("at ") or question.__contains__("near"):
            split_question = question.split(" ")
            Weather.get_weather_at(split_question[len(split_question) - 1])
        else:
            Weather.get_weather()

    elif GreetingQuestions.questions.__contains__(question):
        Greeting.greet(question)

    elif CalenderQuestions.today_questions.__contains__(question):
        Calender.main("today")

    elif question.__contains__("take notes"):
        note = listen()
        file_name = "notes/" + str(datetime.now()).replace(":", "-") + "-note.txt"
        with open(file_name, "w") as f:
            f.write(note)

    elif question.__contains__("open ") and question.split(" ")[0] == "open":
        question_with_out_open = question.split("open ")
        get_url = search(question_with_out_open[0])[0]
        if question_with_out_open[0] == "browser":
            webbrowser.open("https://google.com")
        elif question_with_out_open[0] == "chrome" or question_with_out_open[0] == "google chrome":
            os.system("google-chrome")
        elif question_with_out_open[0] == "firefox":
            os.system("firefox")
        else:
            print(get_url)
            webbrowser.open(get_url)

    elif question.__contains__("search ") and question.split(" ")[0] == "search":
        question_with_out_search = question.split("search ")
        get_url = search(question_with_out_search[0])[0]
        print(get_url)
        webbrowser.open(get_url)

    else:
        get_url = search(question)[0]
        choice = input("I found something about this on Google do you want me to open it in browser : ")
        if choice.lower() == "yes":
            print(get_url)
            webbrowser.open(get_url)
