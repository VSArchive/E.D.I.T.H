from Features.Speak import speak


def greet(question):
    if question.split(" ").__contains__("how") or question.split(" ").__contains__("how's"):
        print("I am fine, how are you doing")
        speak("I am fine, how are you doing")

    elif question.split(" ").__contains__("what's"):
        print("Nothing much, how are you doing")
        speak("Nothing much, how are you doing")

    else:
        print("Hello")
        speak("Hello")
