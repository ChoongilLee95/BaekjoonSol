from curses import keyname
import sys

num_words  = int(sys.stdin.readline().strip())

dict_words = dict()

for i in range(num_words):
    new_word = sys.stdin.readline().strip()
    leng = len(new_word)
    if leng in dict_words:
        if new_word not in dict_words[leng]:
            dict_words[leng].append(new_word)
    else:
        dict_words[leng] = [new_word]

for i in sorted(dict_words.keys()):
    for j in sorted(dict_words[i]):
        print(j)

