# -*- coding: utf-8 -*-

import time    
import re

def read_file(filename):
    lines = []
    with open(filename, 'r') as read:
        for line in read:
            lines.append(line.strip().lower())
    return lines

def spell_check(to_check):
    word_list = read_file('words.txt')
    return to_check.lower() in word_list


book = read_file('war_and_peace.txt')
start = time.time()
mispelled_words = 0
total_words = 0
for sentence in book:
    for word in sentence.split():
        #print "{} : {}".format(word, spell_check(word))
        total_words +=1
        word = re.sub("[^a-z]", "", word.lower())
        print word
        if not spell_check(word):
            mispelled_words += 1
            
print "Total Words : {}, Mispelled Words: {}".format(total_words, mispelled_words)
print "Time Taken: ", (time.time() - start)