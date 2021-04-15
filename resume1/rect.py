from spacy.lang.en.stop_words import STOP_WORDS
stopwords = list(STOP_WORDS)


def evaluate(sample, liste):
    rank = {}
    for i in range(len(liste)):
            liste[i] = liste[i].lower()        
    for d in sample:
        docx = d.split()
        word_frc = {}
        word_key = {}
        for word in docx:
            for wrd in liste:
                if len(wrd.split()) > 1:
                    liste_2 = wrd.split()
                    liste_ = ' '.join([str(e) for e in liste_2])

                    if word in liste_2:
                        if word not in word_key.keys():
                            word_key[word] = 1
                        else:
                            word_key[word] += 1
                        if liste_ not in word_frc.keys():
                            word_frc[liste_] = 1 
                        else:
                            word_frc[liste_] = min([word_key[val] for val in word_key.keys()])

                else:
                    if word == wrd:
                        if wrd not in stopwords:
                            if word not in word_frc.keys():
                                word_frc[word] = 1
                            else:
                                word_frc[word] += 1

        rank[f'candidate_{sample.index(d)}'] = word_frc
        for skill in rank.keys():
            for i in liste:
                if i not in rank[skill].keys():
                    rank[skill][str(i)] = 0

    return rank