from translate import Translator


def uz_en(text, src='uz', dest='en'):
    translator = Translator(from_lang=src, to_lang=dest)
    translated = translator.translate(text)
    return translated


def en_uz(text, src='en', dest='uz'):
    translator = Translator(from_lang=src, to_lang=dest)
    translated = translator.translate(text)
    return translated
