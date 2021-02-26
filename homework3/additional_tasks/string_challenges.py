# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
print(word.count('а'))

# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???


def countvowel(word):
    cnt = 0
    vowel_list = set("АаЕеЁёИиЙйОоУуЫыЭэЮюЯя")
    for letter in word:
        if letter in vowel_list:
            cnt += 1
    print(cnt)


countvowel(word)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
print(len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
for word in sentence.split():
    print(word[0])

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
# ???
word_len = 0
word_list = sentence.split()
word_quantity = len(word_list)
for word in word_list:
    word_len += len(word)
word_mean = word_len / word_quantity
print(word_mean)
