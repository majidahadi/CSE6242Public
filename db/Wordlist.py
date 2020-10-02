from __future__ import division
import nltk
import json
import pronouncing
from nltk.corpus import wordnet as wn


# for ss in wn.synsets('small'):
#     # print(ss)
#     for sim in ss.similar_tos():
#         print('    {}'.format(sim))


# for ss in wn.synsets('small'):
#    	print(ss.lemma_names())


entries = nltk.corpus.cmudict.entries()

def rhyme(inp, level):
     # entries = nltk.corpus.cmudict.entries()
     syllables = [(word, syl) for word, syl in entries if word == inp]
     rhymes = []
     for (word, syllable) in syllables:
             rhymes += [word for word, pron in entries if pron[-level:] == syllable[-level:]]
     return rhymes

fp = open("synonyms.json", "w")
fp.write("[\n")
fp.close()

with open("wordnetWords.txt", "r") as fh:
	word_list = fh.read().split("\n")
	# word_list = [line.strip("\n") for line in word_list]

print word_list


count = 0
for input_word in word_list: 
	if count < 200000:
		# input_word = "car"
		syn_dict = {}
		syn_list = []
		ant_list = []
		pos_list = []
		def_list = []
		syn_dict ["word"] = input_word
		for i,j in enumerate(wn.synsets(input_word)):
		  print "Meaning",i, "NLTK ID:", j.name()
		  print "Definition:",j.definition()
		  print "Synonyms:", ", ".join(j.lemma_names())
		  syn_list += j.lemma_names()
		  for k in j.lemmas():
			  if k.antonyms():
			  	ant_list.append(k.antonyms()[0].name())
		  pos_list += j.pos()
		  def_list.append(j.definition())
		  # pos_list.append(wn.getpos(j))
		  print syn_list
		  while input_word in syn_list:
		  	syn_list.remove(input_word)

		syn_dict ["synonyms"] = list(set(syn_list))
		syn_dict ["rhymes"] = list(set(pronouncing.rhymes(input_word)))# + rhyme(input_word, 1)))
		syn_dict ["antonyms"] = list(set(ant_list))
		syn_dict ["definitions"] = list(set(def_list))
		syn_dict ["pos"] = list(pos_list)

		print syn_dict

		with open('synonyms.json', 'a') as fp:
		    json.dump(syn_dict, fp)
		    fp.write("\n")
	count += 1

fp = open("synonyms.json", "a")
fp.write("\n]")
fp.close()



def rhymes(inp, level):
     entries = nltk.corpus.cmudict.entries()
     syllables = [(word, syl) for word, syl in entries if word == inp]
     rhymes = []
     for (word, syllable) in syllables:
             rhymes += [word for word, pron in entries if pron[-level:] == syllable[-level:]]
     return set(rhymes)

# word = raw_input()
# level = input()
# print rhyme(word, level)


# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# fp = open("inpsyn.txt")
# data = fp.read()

# #to tokenize input text into sentences

# print '\n-----\n'.join(tokenizer.tokenize(data))# splits text into sentences

# #to tokenize the tokenized sentences into words

# tokens = nltk.wordpunct_tokenize(data)
# text = nltk.Text(tokens)
# words = [w.lower() for w in text]  
# print words     #to print the tokens

# for a in words:
#     print a

# syns = wn.synsets(a)
# print "synsets:", syns

# for s in syns:
#     for l in s.lemmas:
#         print l.name
#     print s.definition
#     print s.examples