def sort(text,dict_words = [],dict_translate = []): #

    text = text.replace('\n',' ')
    text = text.replace('.',' ')
    text = text.replace(',',' ')
    raw_data = text.split(' ')

    dict = {}
    for i in range(0,len(dict_words)):
        dict[dict_words[i].lower()] = dict_translate[i]

    allwords = [] # все слова с повторами

    for string in raw_data:
        for char in string:
            if not char.isalpha():
                string = string.replace(char,'')

        string = string.lower()
        if string == '' or not string in dict_words:
            continue

        allwords.append(string)

    allwords.sort()

    pref_word = allwords[0]
    count = 0
    words = {} # словарь = слово: колл-во слов


    for word in allwords:
        if pref_word != word:
            words[pref_word] = [dict[pref_word],count]
            count = 1
            pref_word = word
        else:
            count +=1

    words[pref_word] = [dict[pref_word], count]


    return words,len(allwords)


def statistic(conts_list = [], allwordscount = int()):

    percent = 0
    current_allwords_count = 0
    current_words_count = 0
    stat = {}

    for count in conts_list:
        current_allwords_count+=count
        current_words_count+=1
        new_percent = int(current_words_count  * 100 / allwordscount)
        if percent != new_percent and new_percent % 5 == 0 and new_percent >= 50:
            percent = new_percent
            stat[current_words_count] = percent


    return conts_list

