# This is a sample Python script.

# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

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

# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot.response_selection import get_first_response
# from dotenv import load_dotenv
# from openai import OpenAI
# import os
# import openai
# import warnings
# from sqlalchemy.exc import SAWarning
#
# # Suppress SQLAlchemy warnings
# warnings.filterwarnings("ignore", category=SAWarning)
#
# # Load environment variables
# load_dotenv()
#
# # Initialize OpenAI client
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#
# # Initialize ChatterBot with better settings
# chatbot = ChatBot(
#     "TanescoBot",
#     storage_adapter='chatterbot.storage.SQLStorageAdapter',
#     logic_adapters=[
#         {
#             'import_path': 'chatterbot.logic.BestMatch',
#             'default_response': 'Samahani, sijaelewa swali lako. Unaweza kulisema kwa njia nyingine?',
#             'maximum_similarity_threshold': 0.65
#         }
#     ],
#     response_selection_method=get_first_response
# )
#
# # Train the bot with custom Swahili corpus
# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train("./swahili/tanesco.yml")
#
# print("Karibu! Tanesco huduma kwa wateja (andika 'exit' kuondoka).")
#
#
# # Custom logic for known inputs
# def get_custom_response(user_input):
#     user_input = user_input.lower().strip()
#
#     # Handle specific known patterns
#     if "eneo langu ni" in user_input:
#         area = user_input.split("eneo langu ni")[-1].strip()
#         return f"Ahsante kwa taarifa! Tumepokea malalamiko kutoka {area}, timu yetu iko kazini kuboresha huduma."
#
#     # Get response from ChatterBot
#     response = chatbot.get_response(user_input)
#
#     return response
#
#
# # Fallback to ChatGPT with Swahili context
# def get_chatgpt_response(prompt):
#     try:
#         system_message = """
#         Wewe ni msaidizi wa TANESCO unaojibu maswali kwa Kiswahili kuhusu:
#         - Matatizo ya umeme
#         - Malipo ya bili
#         - Uunganishaji wa umeme mpya
#         - Huduma kwa wateja
#         Jibu kwa ufupi na kwa lugha rahisi ya Kiswahili.
#         Kama hujui jibu, sema 'Samahani, siwezi kukusaidia kwa hili. Tafadhali piga 0748 123 456.'
#         """
#
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",  # Using 3.5 for cost efficiency
#             messages=[
#                 {"role": "system", "content": system_message},
#                 {"role": "user", "content": prompt}
#             ],
#             temperature=0.3  # Keep responses more focused
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         print(f"Error accessing ChatGPT: {e}")
#         return "Samahani, kuna tatizo la kiufundi. Tafadhali jaribu tena baadaye."
#
#     # Checking for the connection
#
#     # try:
#     #     test_response = client.chat.completions.create(
#     #         model="gpt-3.5-turbo",
#     #         messages=[{"role": "user", "content": "Sema 'Hello' kwa Kiswahili"}],
#     #         max_tokens=10
#     #     )
#     #     print("\nOpenAI Test Result:", test_response.choices[0].message.content)
#     #     print("✅ OpenAI is working correctly!")
#     # except Exception as e:
#     #     print("\n❌ OpenAI Connection Failed:", str(e))
#
#
#
# # Improved confidence evaluation
# def should_use_chatgpt(response):
#     try:
#         # Check if response is the default (low confidence)
#         if str(response) == chatbot.default_response:
#             return True
#
#         # Check confidence if available
#         if hasattr(response, 'confidence'):
#             return response.confidence < 0.6
#
#         return False
#     except:
#         return False
#
#
# # Chat loop
# while True:
#     try:
#         user_input = input("Habari: ")
#
#         if user_input.lower() in ["exit", "ondoka", "quit","hapana","bye"]:
#             print("Chatbot: Kwa heri! Tanesco tunayaangaza maisha yako.")
#             break
#
#         # First try custom responses
#         response = get_custom_response(user_input)
#
#         # Then check if we should use ChatGPT
#         if should_use_chatgpt(response):
#             print("Chatbot: (Ninatafuta jibu sahihi zaidi...)")
#             gpt_reply = get_chatgpt_response(user_input)
#             print("Chatbot:", gpt_reply)
#         else:
#             print("Chatbot:", response)
#
#     except (KeyboardInterrupt, EOFError):
#         print("\nChatbot: Kwa heri!")
#         break
#     except Exception as e:
#         print(f"Chatbot: Samahani, kuna tatizo la kiufundi: {str(e)}")


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_first_response
from dotenv import load_dotenv
from openai import OpenAI  # DeepSeek uses OpenAI-compatible API
import os
import warnings
from sqlalchemy.exc import SAWarning

# Suppress SQLAlchemy warnings
warnings.filterwarnings("ignore", category=SAWarning)

# Load environment variables
load_dotenv()

# Initialize DeepSeek client (using OpenAI-compatible format)
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),  # Add DEEPSEEK_API_KEY to .env
    base_url="https://integrate.api.nvidia.com/v1"  # DeepSeek API endpoint
)

# Initialize ChatterBot
chatbot = ChatBot(
    "TanescoBot",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Samahani, sijaelewa swali lako. Unaweza kulisema kwa njia nyingine?',
            'maximum_similarity_threshold': 0.65
        }
    ],
    response_selection_method=get_first_response
)

# Train the bot
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("./swahili/tanesco.yml")

print("Karibu! Tanesco huduma kwa wateja (andika 'exit' kuondoka).")


# --- DeepSeek Test Function ---
# def test_deepseek_connection():
#     try:
#         test_response = client.chat.completions.create(
#             model="deepseek-ai/deepseek-r1",
#             messages=[{"role": "user", "content": "Sema 'Hello' kwa Kiswahili"}],
#             max_tokens=10
#         )
#         # print("\nDeepSeek Test Result:", test_response.choices[0].message.content)
#         # print("✅ DeepSeek is working correctly!")
#         return True
#     except Exception as e:
#         print("\n❌ DeepSeek Connection Failed:", str(e))
#         return False
#
#
# # Run connection test
# if not test_deepseek_connection():
#     exit("Please check your DeepSeek API key and connection.")


# Custom response logic (unchanged)
def get_custom_response(user_input):
    user_input = user_input.lower().strip()
    if "eneo langu ni" in user_input:
        area = user_input.split("eneo langu ni")[-1].strip()
        return f"Ahsante kwa taarifa! Tumepokea malalamiko kutoka {area}, timu yetu iko kazini kuboresha huduma."
    return chatbot.get_response(user_input)


# Modified for DeepSeek
def get_deepseek_response(prompt):
    try:
        system_message = """
        Wewe ni msaidizi wa TANESCO unaojibu maswali kwa Kiswahili kuhusu:
        - Matatizo ya umeme
        - Malipo ya bili
        - Uunganishaji wa umeme mpya
        - Huduma kwa wateja
        Jibu kwa ufupi na kwa lugha rahisi ya Kiswahili.
        Kama hujui jibu, sema 'Samahani, siwezi kukusaidia kwa hili. Tafadhali piga 0748 123 456.'
        """
        response = client.chat.completions.create(
            model="deepseek-ai/deepseek-r1",  # DeepSeek model
            messages=[
                {"role": "system", "content": "Huduma kwa wateja"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            top_p = 0.7,
            max_tokens = 4096,
            stream = True
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"DeepSeek Error: {e}")
        return "Samahani, kuna tatizo la kiufundi. Tafadhali jaribu tena baadaye."


# Confidence check (unchanged)
def should_use_deepseek(response):
    try:
        if str(response) == chatbot.default_response:
            return True
        if hasattr(response, 'confidence'):
            return response.confidence < 0.6
        return False
    except:
        return False


# Main chat loop (modified for DeepSeek)
while True:
    try:
        user_input = input("Habari: ")
        if user_input.lower() in ["exit", "ondoka", "quit", "hapana", "bye"]:
            print("Chatbot: Kwa heri! Tanesco tunayaangaza maisha yako.")
            break

        response = get_custom_response(user_input)

        if should_use_deepseek(response):
            print("Chatbot: (Ninatafuta jibu sahihi zaidi...)")
            ai_reply = get_deepseek_response(user_input)
            print("Chatbot:", ai_reply)
        else:
            print("Chatbot:", response)

    except (KeyboardInterrupt, EOFError):
        print("\nChatbot: Kwa heri!")
        break
    except Exception as e:
        print(f"Chatbot: Samahani, kuna tatizo: {str(e)}")
