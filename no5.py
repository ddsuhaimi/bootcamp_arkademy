def split_word(word, keywords):
    check_idx = 0
    for i in range(len(keywords)):
        if word.find(keywords[i]) == check_idx:
            print(keywords[i], end=' ')
            check_idx += len(keywords[i])

            for j in range(len(keywords)):
                if word.find(keywords[j]) == check_idx:
                    print(keywords[j], end=' ')
                    check_idx += len(keywords[j])
            print()
        check_idx = 0


keywords = ['pro', 'gram', 'merit', 'program', 'it', 'programmer']

split_word('programmerit', keywords)
# pro gram merit
# program merit
# programmer it
