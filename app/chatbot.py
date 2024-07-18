from chatterbot import ChatBot
from langdetect import detect
from googletrans import Translator

# Initialize ChatterBot
english_bot = ChatBot("English Bot")

# Translation function
def translate_to_english(text):
    translator = Translator()
    translated = translator.translate(text, src='auto', dest='en')
    return translated.text

# Language detection function
def detect_language(text):
    try:
        return detect(text)
    except:
        return 'unknown'
