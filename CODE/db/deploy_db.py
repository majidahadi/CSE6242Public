from google.cloud import datastore
import json
import sys
from threading import Thread

project_id = sys.argv[1]

def saver(i, datastore_client, words):
  datastore_client.put_multi(words)
  print str(i) + ', ',
  
datastore_client = datastore.Client(project=project_id)
kind = 'Word'

# delete the table
query = datastore_client.query(kind='Word')
#results = list(query.fetch())
keys = query.keys_only()
#for result in results:
#  print('deleting ' + result.key.name)

 # datastore_client.delete(result.key)
print 'Deleting' 
datastore_client.delete_multi(keys)
print 'Finished deleting.' 

with open('synonyms2.json') as f: 
  words = []
  i = 0
  for line in f:

    if line.strip() == '[':
      continue

    if line.strip() == ']':
      continue

    if len(line.strip()) == 0:
      continue


    #print(i)
    i = i + 1
    json_object = json.loads(line)
    word = json_object['word']
    word_key = datastore_client.key(kind, word)
    word_entity = datastore.Entity(key=word_key,exclude_from_indexes=['data'])
    word_entity['data'] = line
    words.append(word_entity)
    if (i % 100 == 0):
      t = Thread(target=saver, args=(i,datastore_client,words))
      t.start()
      words = []
      
    if (i % 10000 == 0):
      print ''

  if (len(words) > 0):
    print(str(len(words)) + ', '),
    t = Thread(target=saver, args=(i,datastore_client,words))
    t.start()
  print ('Finished - saved ' + str(i) + ' records.')
     
    #datastore_client.put(word_entity)
    #print line, 
#  print 'Saving' 
#  print 'Finished saving.' 

