import random

# input: string, output: bigram dictionary
def bigram(string_):
    # 'Alpha And Apostrophes'  The only acceptable characters in a word
    # Characters will be considered either 'AAA' or 'non-AAA'
    aaa = "abcdefghijklmnopqrstuvwxyz\'"

    # This is the dictionary that will be filled out with bigrams
    dict_={}
    # j is a key, k is a value
    j = ''
    k = ''
    # Go through the code, character by character
    for i in range(len(string_)):
        # if the char is a 'AAA' char, add it to word 'k'
        if string_[i].lower() in aaa:
            k+=string_[i].lower()
        # if the char is non-AAA, and the preceding char is non-AAA,
        # that means there is an instance of several non-AAA chars between words
        # in this case, continue looping until you find an AAA char
        elif string_[i].lower() not in aaa and string_[i-1].lower() not in aaa:
            continue
        # if the char is non-AAA, and the preceding char is AAA
        # you have just finished a word.  congratulations
        # this word, 'k', will now be placed in the dictionary of bigrams
        else:
            if j not in dict_:
                dict_[j] = [k]
            else:  # if j is in dict1[j]
                if k not in dict_[j]:
                    dict_[j]+=[k]
            # to finish, the word 'k' will become word 'j'.
            # k will be deleted
            j = k
            k = ''
    # This removes the first item in the dictionary, where the key is an empty string
    dict_.pop('')

    return dict_

# inputs: seed_word, length of sentence, bigram dictionary | outputs: nonsense sentence
def sentence_makr(seed, length, bigr_dict):
    j = seed
    output_string = str(j)
    for i in range(int(length)-1):
        k = bigr_dict[j][random.randint(0, len(bigr_dict[j])-1)]
        output_string += ' ' + k
        j=k
    return output_string

# Now the dictionary maker is defined and the sentence maker is defined
# The following steps get user inputs

# 1) Program asks you what text file you want and then produces a bigram dictionary
title_ = input("Provide a text file to ingest:")

text_ = open(title_, "r", encoding="utf8").read()
a = bigram(text_)

# 2) Program asks you what seed word you want
# if your word isn't a dictionary key then it asks you again
seed_word = None
while seed_word not in a:
    seed_word = input("What seed word would you like to begin with?: ")
    seed_word = seed_word.lower()
    if seed_word not in a:
        print("Sorry, '{}' is not an available seed term".format(seed_word))

# 3) Program asks length of desired sentence
length = input("How long of a sentence would you like to generate?:")

print(sentence_makr(seed=seed_word,length=length,bigr_dict=a))



