def check(x: str, file: str):
    words = x.split()
    words_count = {}

    for word in words:
        word = word.lower()
        if word in words_count.keys():
            words_count[word] += 1
        else:
            words_count[word] = 1

    with open(file, 'w') as f:
        for word, count in sorted(words_count.items(), key=lambda t: t[0]):
            f.write(f'{word} {count}\n')
