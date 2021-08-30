import enchant
#from enchant import *
endict = Dict("en_US")
data = raw_input("Enter String : ")
words = []
inc_words = []
swords = {}
for word in data.split(" "):
    if word not in words:
        words.append(word)
        if not endict.check(word):
            inc_words.append(word)
            swords.setdefault(word, endict.suggest(word))
        

#print words
#print inc_words        
#print swords


print enchant.list_dicts()
#print enchant.list_languages()
#print enchant.dict_exists("hi_US")
