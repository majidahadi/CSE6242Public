rock_dict = dict()

with open('genres/rock.csv') as rock: 
  i = 0
  for line in rock:
    #print(line)
    words = line.split()
    key = words[0]
    value = words[1]
    rock_dict[key] = value
    i = i + 1
    #if (i >= 10):
      #break
  #print(rock_dict)

rap_dict = dict()

with open('genres/rap.csv') as rap:
  i = 0
  for line in rap:
    #print(line)
    words = line.split()
    key = words[0]
    value = words[1]
    rap_dict[key] = value
    i = i + 1
    #if (i >= 10):
      #break
  #print(rap_dict)

country_dict = dict()

with open('genres/country.csv') as country:
  i = 0
  for line in country:
    #print(line)
    words = line.split()
    key = words[0]
    value = words[1]
    country_dict[key] = value
    i = i + 1
    #if (i >= 10):
     # break
  #print(country_dict)

import json

out_file = open('synonyms2.json', 'w')

with open('synonyms.json') as f: 
  words = []
  i = 0
  for line in f:

    if line.strip() == '[':
      out_file.write('[\n')
      continue

    if line.strip() == ']':
      out_file.write(']\n')
      continue

    if len(line.strip()) == 0:
      continue

    #print(i)
    i = i + 1
    json_object = json.loads(line)
    word = json_object['word']

    genres = []
    if rock_dict.get(word) > 500:
	genres.append('rock')
    if rap_dict.get(word) > 500:
        genres.append('hip-hop') 
    if country_dict.get(word) > 500:
        genres.append('country') 

    json_object['genres'] = genres

    out_file.write(json.dumps(json_object) + '\n')
    #print(json_object)

    #if (i >= 10):
      #break
