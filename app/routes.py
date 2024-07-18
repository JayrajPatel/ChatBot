from flask import Blueprint, jsonify, request
from app.chatbot import english_bot, translate_to_english, detect_language

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/chat', methods=['POST'])
def chat():
    incoming_message = request.json.get('message')
    
    # Detect language of incoming message
    detected_lang = detect_language(incoming_message)
    print(f"Detected language: {detected_lang}")
    
    # Translate to English if not already in English
    if detected_lang != 'en':
        translated_message = translate_to_english(incoming_message)
        print(f"Translated text ({detected_lang} -> en): {translated_message}")
    else:
        translated_message = incoming_message
    
    # Get response from ChatterBot
    english_response = english_bot.get_response(translated_message)
    
    return jsonify({'message': str(english_response)})
