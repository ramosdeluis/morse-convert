import translator


def main():
    mt = translator.MorseTranslator()
    text_to_translate = mt.normal_text()
    mt.simple_translate(text_to_translate)
    mt.create_morse_file()


if __name__ == '__main__':
    main()
