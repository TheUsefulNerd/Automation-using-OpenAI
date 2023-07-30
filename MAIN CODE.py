import os
import openai
from config import api_key
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import random

reply = ""
def chat(query):
    global reply
    print(reply)
    openai.api_key = api_key
    reply += f"Advait: {query}\n Atlas: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=reply,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response["choices"][0]["text"])
    reply += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


    with open(f"INTAKE/{''.join(prompt.split('magic')[1:])}.txt", "w") as f:
        f.write(text)





def give(prompt):
    openai.api_key = api_key
    text = f"OpenAI response for Prompt: {prompt}\n****************\n\n"


    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if  not os.path.exists("INTAKE"):
        os.mkdir("INTAKE")

    with open(f"INTAKE/{''.join(prompt.split('magic')[1:])}.txt", "w") as f:
        f.write(text)




def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 1000
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print (f"User: {query}")
            return query
        except Exception as e:
            return "Some Error Occured. Sorry ."


if __name__ == '__main__':
    say("Hello, I am Atlas")
    while True:
        print("Listening...")
        query= takecommand()
        sites = [["Youtube","https://www.youtube.com"],["chat","https://www.openai.com"], ["Linkedin", "https://www.linkedin.com"],  ["git", "https://www.github.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}, Sir")
                webbrowser.open(site[1])

            elif " the time" in query:
                Time= datetime.datetime.now().strftime("%H:%M:%S")
                say(f"Sir, Time is {Time}")

            elif "magic".lower() in query.lower():
                give(prompt=query)
                break

            elif"Hi Atlas".lower() in query.lower():
                chat(query)

                while True:
                    print("Listening...")
                    query = takecommand()
                    chat(query)
                    if "bye" in query.lower() :
                        say("Goodbye, have a great day!")
                        exit()







