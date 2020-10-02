import nltk
from string import punctuation
import inflect
#from nltk.tag import pos_tag
import os
import csv
import sys

#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')

from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

from PyDictionary import PyDictionary
dictionary=PyDictionary()

plurals = inflect.engine()

dataset = sys.argv[1]

#file = open('rap-flat/zoom-lil-boosie-featuring-yung-joc','r')
word_count = dict()

for fn in os.listdir(dataset):
  print(fn)

  file = ""

  if (os.path.isdir(dataset + '/'  + fn)):
    continue
    
  file = open(dataset + '/' + fn,'r')

  for line in file:

    if '[' in line:
      continue

    for word in line.split():
    
    # lowercase
      word = word.lower()

    # remove stop words
      if word in stop:
          continue

    #tag = pos_tag(line.split)
    #print(tag)

    # remove leading and trailing punctuation
      word = word.strip(punctuation)    
    
      if (len(word) == 0):
        continue

      count = word_count.get(word)

      if (count > 0):
        count = count + 1
      else:
        count = 1

      word_count[word] = count
    
    
#    print word, plurals.singular_noun(word)
    
with open(dataset + '.csv', 'wb') as csvfile:
  csvwriter = csv.writer(csvfile, delimiter=' ',
                         quotechar='|', quoting=csv.QUOTE_MINIMAL)
  for key, value in sorted(word_count.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    csvwriter.writerow([key, value])

  #if(value > 1000):
    #print "%s: %s" % (key, value)
