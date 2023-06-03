def count_words(text):
    word_count = {}
    words = text.split()

    for word in words:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1

    return word_count

text = input('Enter text to count words: ')
result = count_words(text)

print('Word count: ')
for word ,count in result.items():
    print(f'{word}:{count}')

