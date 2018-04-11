import chardet
import json


def open_file(name_file):
    """Объеденил определение кодировки и чтнение файла в один open"""
    with open(name_file, 'rb') as file:
        data = file.read()
        result = chardet.detect(data)
        print(result['encoding'])
        data_json = json.loads(data.decode(encoding=result['encoding']))
        data_news = data_json['rss']['channel']['items']

        list_news = list()
        for description in data_news:
            list_news.append(description['title'])
            list_news.append(description['description'])

        list_char_more_6 = list()
        for str_news in list_news:
            list_string_file = str_news.lower().split(' ')
            list_char_more_6 = [char for char in list_string_file if len(char) > 6]

        return list_char_more_6


def top_10_popular(list_char_more_6):
    """ Принимаем список слов длинее 6 символов, проходим по списку и составляем словарь {слово: повторения}
    сортируем словарь"""

    list_word = list()
    freq = {}

    for word in list_char_more_6:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1

    sorted_count_pair = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    sorted_count_pair = sorted_count_pair[:10]  # С помощью среза выбираем ТОП 10

    for word, count in sorted_count_pair:
        if word not in list_word:
            list_word.append(word)

    return list_word


def print_word(word, name_file):
    print('Топ 10 самых часто встречающихся в новостях {} слов длиннее 6 символов:'.format(name_file))
    for i in word:
        print(i)


def main():
    list_file = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']

    for name_file in list_file:
        list_char_more_6 = open_file(name_file)
        list_word = top_10_popular(list_char_more_6)
        print_word(list_word, name_file)


main()

