
def sort(text,dict_words = [],dict_translate = []):

    text = text.replace('\n',' ')
    text = text.replace('.',' ')
    text = text.replace(',',' ')
    raw_data = text.split(' ')

    dict = {}
    for i in range(0,len(dict_words)):
        dict[dict_words[i].lower()] = dict_translate[i]

    allwords = [] # все слова с повторами

    for string in raw_data:
        upper = 0
        for char in string:
            if char.isupper():
                upper +=1
            if not char.isalpha():
                string = string.replace(char,'')

        if len(string) > 15 or len(string) < 2 or not string in dict_words:
            continue
        if upper > 1 or string == '':
            continue

        allwords.append(string.lower())

    allwords.sort()


    pref_word = allwords[0]
    count = 0
    biggest_count = 0
    data = {} # словарь = слово: колл-во слов


    for word in allwords:
        if pref_word != word:
            data[pref_word] = count

            count = 1
            pref_word = word
        else:
            count +=1
            if count > biggest_count:
                biggest_count = count
    data[pref_word] = count

    count = 0
    allwordscount = 0
    pref_percent = 0
    words = {}
    statistic = {}

    for wordcount in range(biggest_count,0,-1):
        for j in data:
            if data[j] == wordcount:
                allwordscount += wordcount
                percent = int(allwordscount  * 100/ len(allwords))
                count += 1
                words[j] = [dict[j],wordcount]
                if percent >= 50 and percent != pref_percent and percent % 5 == 0:
                    statistic[count] = percent
                    pref_percent = percent
#                    print(count ,'(',wordcount,')','=', percent , '%')

    return words,statistic,biggest_count
