# This is a sample Python script.

# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import warnings
from sqlalchemy.exc import SAWarning
warnings.filterwarnings("ignore", category=SAWarning)

# Create chatbot instance
# chatbot = ChatBot("RhinoBot")
#
#  Create and train using corpus trainer
# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train("chatterbot.corpus.french")  # You can use other languages too
#
# Get a response
# response = chatbot.get_response("Au revoir!")
# print(response)

chatbot = ChatBot("SwahiliBot")

# Create a trainer and train with the custom Swahili corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("./swahili/tanesco.yml")  # Path to your Tanesco Huduma kwa wateja! corpus

# Interactive terminal chat loop
print("Karibu! Tanesco huduma kwa wateja (andika 'exit' kuondoka).")
while True:
    try:
        user_input = input("Habari: ")

        if user_input.lower() in ["exit", "ondoka", "quit"]:
            print("Chatbot: Kwa heri! Tanesco tunayaangaza maisha yako.")
            break

        response = chatbot.get_response(user_input)
        print("Chatbot:", response)

    except (KeyboardInterrupt, EOFError):
        print("\nChatbot: Kwa heri!")
        break