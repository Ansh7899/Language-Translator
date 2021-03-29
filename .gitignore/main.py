from translate import Translator
lang1 = input("Enter the language of text:")
lang2 = input("Enter the language ou want to convert the text in:")
translator = Translator(from_lang=lang1,to_lang=lang2)
stringInput = input("Enter the text you want to translate:")
translation = translator.translate(stringInput)
print(translation)