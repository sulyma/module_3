def single_root_words(root_word, *other_words):
    same_words = []
    root_word_up = root_word.upper()
    for i in range(len(other_words)):
        other_words_up = other_words[i].upper()
        if other_words_up.count(root_word_up):
            same_words.append(other_words[i])
        elif root_word_up.count(other_words_up):
            same_words.append(other_words[i])
    print(same_words)


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
