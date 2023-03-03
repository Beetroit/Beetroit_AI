from chatterbot import  ChatBot
from chatterbot.trainers import ListTrainer
import logging
import time
from speek import speak
import pdfdrive


logging.basicConfig(level=logging.ERROR)
#keep_alive()
chatbot = ChatBot(
    "Beetroit",preprocessors = ["chatterbot.preprocessors.clean_whitespace","chatterbot.preprocessors.convert_to_ascii"],
    logic_adapters=[{"import_path":"JokeLogic.JokeLogic"}
    ,"chatterbot.logic.BestMatch",
    {"import_path":"WolframResponder.WolframResponder"},
    {'import_path':"shorten.Shorten"},
    {'import_path':'QrCoder.QR'},
    "chatterbot.logic.UnitConversion",
    "chatterbot.logic.SpecificResponseAdapter",
    'chatterbot.logic.MathematicalEvaluation',
    "chatterbot.logic.TimeLogicAdapter"],read_only=True
)

trainer = ListTrainer(chatbot)
conversation = [
    "what do i call you",
    "Beetroit works fine",
    'what is your name',
    'Beetroit',
    'what is your name',
    'Call me Beetroit',
    "what are you called",
    'You can refer to me as Beetroit',
    'is your name Beetroit',
    'Yes, it is.',
    'Is your name John',
    'No, my name is Beetroit',
    'Is your name Peter',
    'No, my name is Beetroit',
    'Is your name Mathew',
    'No, my name is Beetroit',
    'Is your name Paul',
    'No, my name is Beetroit',
    'Is your name Sandra',
    'No, my name is Beetroit'

]
#trainer.train(conversation)
exit_conditions = (":q", "quit", "exit")
help_list=["cmd","help"]
def cmd_list():
    #TODO add more commands and API's
    intro=["Hello, I'm Beetroit, your friendly bot","Here's a list of my commands"]
    for i in intro:
        print(i)
        speak(i)
    time.sleep(0.3)
    print()
    help_list=["ask followed by a prompt for answers to specific questions","joke,tell me a joke or a variation of it for tech jokes",'shorten followed by a url(s) to shorten em',"qr followed by any text to generate a qr code of said text",'cmd or help for this help message']
    for i in help_list:
        print(f"Type {i}")
        speak(f'Type {i}')



while True:
    query = input("Me:  ")
    if query in exit_conditions:
        conf=input("You're leaving me? ")
        if "ye" in conf.lower():
            end="Ok,Bye"
            print(end)
            speak(end)
            exit();quit()
        else:
            continue
    elif query in help_list:
        cmd_list()
    elif '_pdf' in query:
        query=query.replace('_pdf','')
        print(query)
        pdfdrive.main(query)
    else:
        resp=chatbot.get_response(query)
        print(f"Beetroit> {resp}")
        speak(resp)
        print()
