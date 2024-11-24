
class WordsFinder:

    def __init__(self, *files):

        self.file_names = files

    def get_all_words(self):

        all_words = {}

        for i in self.file_names:

            with open(i, 'r', encoding='utf-8') as file:
                reading = file.read().lower()
                simvols = ',.=!?;:-'
                reading = reading.translate(str.maketrans(simvols, ' ' * len(simvols)))
                all_words[i] = reading.split()


        return all_words

    def find(self, word):

        slovar = {}

        for key, value in self.get_all_words().items():
            if word.lower() in value:
                slovar[key] = value.index(word.lower()) + 1

            return slovar


    def count(self, word):

        slovar_2 = {}

        for key, value in self.get_all_words().items():
            if word.lower() in value:
                slovar_2[key] = value.count(word.lower())

            return slovar_2

finder2 = WordsFinder('file1.txt', 'file2.txt', 'file3.txt')

print(finder2.get_all_words()) # Все слова

print(finder2.find('TEXT')) # 3 слово по счёту

print(finder2.count('teXT')) # 4 слова teXT в тексте всего

