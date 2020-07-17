input_sentence = input("Input sentence: ")

splited_words = input_sentence.split(' ')

words = [word[:10] for word in splited_words if word != '']

for idx, word in enumerate(words):
    print('{idx}. {word}'.format(idx=idx + 1,
                                 word=word))
