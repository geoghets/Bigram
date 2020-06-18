# START MY TIMER
import time
start = time.time()

def bigram(string_):
    import re
    string_ = re.split("\W+|\n+",string_)                          #String becomes list of words with no punctuation
    dict1 = {}                                                     #This is the bigrams dictionary

    for i in range(len(string_)-1):                                 #Go through each word
        j = string_[i]                                                  # j is the current word.
        j = j.lower()                                                   # j is made lowercase
        k = string_[i+1]                                                # k is the word following j
        k = k.lower()                                                   # k is made lowercase

        if j not in dict1:                                          # if j is not  yet a dictionary key:
            dict1[j] = [k]                                              # add it and make it's value a list with item
        else:  # if j is in dict1[j]                                # if j is a dictionary value already
            if k not in dict1[j]:                                       # if k is not yet in the sub-list
                dict1[j]+=[k]                                           # add k
    return dict1                                                    # Return the dictionary

def sentence_makr(seed,length,bigr_dict):

    import random
    j = seed
    output_string = str(j)
    for i in range(length-1):
        k = bigr_dict[j][random.randint(0,len(bigr_dict[j])-1)]
        output_string+= ' ' + k
        j=k

    return output_string

title1 = input("Provide a text file to ingest:")
#title1 = "Ivanhoe.txt"
text1 = open(title1, "r", encoding="utf8").read()
a = bigram(text1)
#
# seed_word = None
# while seed_word not in a:
#     seed_word = input("What seed word would you like to begin with?: ")
#     seed_word = seed_word.lower()
#     if seed_word not in a:
#         print("Sorry, '{}' is not an available seed term".format(seed_word))

#length = input("How long of a sentence would you like to generate?:")

a = sentence_makr(seed="made",length=int(6),bigr_dict=a)
print(a)



# STOP MY TIMER
elapsed_time = time.time() - start # in seconds
print(elapsed_time)

