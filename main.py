def sort_sentence(sentence):
    sentence_local = sentence.lower()
    list_sentence_local = sentence_local.split(" ")
    for i in range(len(list_sentence_local)-1):
        k = i
        while len(list_sentence_local[k]) > len(list_sentence_local[k+1]):
            if k >= 0:
                list_one = list_sentence_local[k]
                list_two = list_sentence_local[k+1]           
                list_sentence_local[k: k+2] = [list_one, list_two]
                k -= 1
            if k < 0:
                break
    list_sentence_local = " ".join(list_sentence_local).capitalize()
    return list_sentence_local
