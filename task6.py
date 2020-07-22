def int_func(text):
    words = [word.capitalize() for word in text.split()]
    return " ".join(words)


test_word = 'abcdef'

print(int_func(test_word))

test_words = 'aaa bbb ccc ddd eee fff'

print(int_func(test_words))
