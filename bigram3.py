import random



class MarkovChainMaker:
    def __init__(self,string_):
        self.string_ = string_

    def bigram(self):
        string_ = open(self.string_, "r", encoding="utf8").read()

        aaa = "abcdefghijklmnopqrstuvwxyz\'"
        dict_ = {}
        j = ''
        k = ''
        for i in range(len(string_)):
            # if the char is a 'AAA' char, add it to word 'k'
            if string_[i].lower() in aaa:
                k += string_[i].lower()
            elif string_[i].lower() not in aaa and string_[i - 1].lower() not in aaa:
                continue
            else:
                if j not in dict_:
                    dict_[j] = [k]
                else:  # if j is in dict1[j]
                    if k not in dict_[j]:
                        dict_[j] += [k]
                j = k
                k = ''
        dict_.pop('')
        return dict_

    def chain(self,seed, length):
        j = seed
        bigr_dict = self.bigram()
        output_string = str(j)
        for i in range(int(length)-1):
            k = bigr_dict[j][random.randint(0, len(bigr_dict[j])-1)]
            output_string += ' ' + k
            j=k
        return output_string


chainer = MarkovChainMaker("Ivanhoe.txt")
print(chainer.chain("seed", 7))
#=> "seed output seven random words words words"
print(chainer.chain("other", 5))
#=> "other five random words words"

chainer2 = MarkovChainMaker("Hard Times.txt")
print(chainer2.chain("different", 3))
# #=> "different three random"





