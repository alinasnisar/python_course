def popular_words(text, words):
    lowered_text = text.lower()
    lower_words = [word.lower() for word in words]

    counted_words = {}
    for word in lower_words:
        counted_words[word] = 0

    for word in lowered_text.split():
        if word in counted_words:
            counted_words[word] += 1

    return counted_words


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')
