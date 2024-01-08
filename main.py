from googletrans import Translator

def translate_text(text, dest_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=dest_language)
    return translation.text

if __name__ == "__main__":
    input_text = input("Enter text to translate: ")
    destination_language = input("Enter destination language (e.g., 'en' for English): ")
    translated_text = translate_text(input_text, destination_language)
    with open('file.txt', 'w', encoding='utf-8') as file:
        file.write(translated_text)
