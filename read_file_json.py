def detect_encording(name_file):
    import chardet
    with open(name_file, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        print("\nКодировка в {}: {}".format(name_file, result['encoding']))

        return result['encoding']


def read_file(name_file, encoding_file):
    import json

    with open(name_file, encoding=encoding_file) as file:
        list_char_more_6 = list()
        data = json.load(file)
        data_string = data['rss']['channel']['items'][1]["description"]
        list_data_string = data_string.lower().split(' ')
        list_char_more_6 = [i for i in list_data_string if len(i) > 6]

        return list_char_more_6


def top_10_popular(list_char_more_6):
    list_word = list()
    list_word_unique = list()
    list_word = [[list_char_more_6.count(i), i] for i in list_char_more_6]

    for i in list_word:
        if i not in list_word_unique:
            list_word_unique.append(i)  # Убираем повторяющие элементы из списка

    list_word_unique.sort(reverse=True)  # Сортрируем, первыми занч. будут с наиб. числом повторений [повторн:слово]
    list_word_top_10 = list_word_unique[:10]  # С помощью среза выбираем ТОП 10
    list_word = list()

    for i in list_word_top_10:
        for i_i in i:
            if i[1] not in list_word:
                list_word.append(i[1])

    return list_word


def print_word(word, name_file):
    print('Топ 10 самых часто встречающихся в новостях {} слов длиннее 6 символов:'.format(name_file))
    for i in word:
        print(i)


def main():
    list_file = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']

    for name_file in list_file:
        encoding_file = detect_encording(name_file)
        list_char_more_6 = read_file(name_file, encoding_file)
        list_word = top_10_popular(list_char_more_6)
        print_word(list_word, name_file)


main()

