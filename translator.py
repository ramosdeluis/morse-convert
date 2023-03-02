import pandas as pd


class MorseTranslator:

    def __init__(self):
        self.df_morse = None
        self.get_morse_data()
        self.text_to_translate = ''
        self.result = ''

    def get_morse_data(self) -> None:
        morse_data = pd.read_csv('morse_data.csv', sep=';')
        self.df_morse = pd.DataFrame(morse_data)
        self.df_morse.set_index('digit', inplace=True)

    def simple_translate(self, a_frase):
        for car in a_frase.upper():
            if car == ' ':
                self.result += '   '
            else:
                try:
                    result = self.df_morse.loc[car, 'morse']
                    self.result += f'{result}  '
                except KeyError:
                    if car == '\n':
                        self.result += f''
                    else:
                        print(f"There is no '{car}' in morse.")
                        if car == 'Á':
                            result = self.df_morse.loc['A', 'morse']
                            self.result += f'{result}  '
                            print('Changed to A')
                        if car == 'Í':
                            result = self.df_morse.loc['I', 'morse']
                            self.result += f'{result}  '
                            print('Changed to I')
                        if car == 'Ú':
                            result = self.df_morse.loc['U', 'morse']
                            self.result += f'{result}  '
                            print('Changed to U')
                        if car == 'Ã':
                            result = self.df_morse.loc['A', 'morse']
                            self.result += f'{result}  '
                            print('Changed to A')
                        if car == 'Ê':
                            result = self.df_morse.loc['E', 'morse']
                            self.result += f'{result}  '
                            print('Changed to E')

    def get_result(self):
        return self.result

    def normal_text(self):
        try:
            with open('text_to_translate.txt'):
                pass
        except FileNotFoundError:
            print('File not found. A new file to put your text was created.')
            with open('text_to_translate.txt', 'a'):
                pass
        finally:
            with open('text_to_translate.txt') as file:
                for line in file:
                    self.text_to_translate += line
            return self.text_to_translate

    def create_morse_file(self):
        try:
            with open('morse_text.txt'):
                pass
        except FileNotFoundError:
            print('Morse file was not found. A new file to put your text created.')
            with open('morse_text.txt', 'a'):
                pass
        finally:
            with open('morse_text.txt', 'w') as file:
                file.write(self.result)


if __name__ == '__main__':
    mt = MorseTranslator()
    text_to_translate = mt.normal_text()
    mt.simple_translate(text_to_translate)
    mt.create_morse_file()
