import json

# This program requires watson-developer-cloud Python SDK installed
# pip install --upgrade watson-developer-cloud
from watson_developer_cloud import LanguageTranslatorV2


def get_data():
    input_value = input("Informe o texto para ser traduzido: ")
    validade_input_value(input_value)

    target_lang = input("Informe o código ISO da linguagem a ser traduzida (es, en, pt, ru, etc.: ")
    validade_input_value(target_lang)
    translate_text(input_value, target_lang)


def validade_input_value(input_value):
    if len(input_value.strip()) == 0:
        print("Invalid value")
        exit(1)


def identify_language(language_translator, source_text):
    """
    Identify the language's text using Watson Language detection APIs
    :param language_translator: Watson Language Translator instance
    :param source_text: Text to be identify
    :return: ISO code
    """
    lang = 'en'
    try:
        result = language_translator.identify(source_text)

        for x in (result["languages"]):
            lang = x["language"]
            break
    except:
        print("Ocorreu um erro na identificação da linguagem origem")

    return lang


def translate_text(source_text, target_lang):
    """
    Translate the source text to target language by Watson's APIs
    :param source_text: Text to be translated
    :param target_lang: Language to be translate
    :return: Text translated
    """
    try:
        language_translator = LanguageTranslatorV2(username='<username>',
                                                   password='<password>')

        source_lang = identify_language(language_translator, source_text)
        print("Linguagem detectada: ", source_lang)

        translation = language_translator.translate(text=source_text, source=source_lang, target=target_lang)
        print(json.dumps(translation, indent=2, ensure_ascii=False))
    except:
        print("Ooops, ocorreu um erro :/")

if __name__ == "__main__":
    get_data()
