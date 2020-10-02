from flask import Flask, render_template, request, make_response
from flask_cors import CORS
import json

from google.appengine.ext import ndb
from google.appengine.api import memcache

app = Flask(__name__)
CORS(app)

@app.route('/get', methods=['GET'])
def handleGet():
    word = request.args.get("word")
    word_data = getWord(word)
    #word_data = json.dumps(word_data, indent=4)
    r = make_response(word_data)
    r.headers['Content-Type'] = 'application/json'
    return r

def getWord(query_text):

    word_string = memcache.get(query_text)

    if word_string is not None:
        return word_string

    word_string = "["
    if (not query_text):
      word = ''
    else: 
      word = loadWord(query_text)
    
    word_string = word_string + word

    if (len(word) > 0):
      word_obj = json.loads(word)
      word_string = getRelated('synonyms',word_obj,word_string)
      word_string = getRelated('antonyms',word_obj,word_string)
      word_string = getRelated('rhymes',word_obj,word_string)
    
    word_string = word_string + "]"
    memcache.add(query_text, word_string, 3600)

    return word_string

def getRelated(relationship, word_obj, word_string):
  related_words = word_obj[relationship]
  for related_word in related_words:
    related_word_text = loadWord(related_word)
    if (related_word_text):
      word_string = word_string + ",\n" + related_word_text
  return word_string      

@app.route('/get_all', methods=['GET'])
def handleGetAll():
    words = Word.query().fetch()
    word_string = "["
    remaining = len(words)
    for word in words:
      remaining = remaining - 1
      word_string = word_string + word.data
      if (remaining > 0):
        word_string = word_string + ",\n"
    return word_string + "]"

def loadWord(query_text):
    word_key = ndb.Key('Word', query_text)
    #word = word_key.get()
    word = word_key.get()
    #if not (word is None):
    #  word_text = word.data
    #else:
    if word:
      word_text = word.data
    else:
      word_text = ""

    return word_text

class Word(ndb.Model):
    data = ndb.StringProperty()
    
    @classmethod
    def query_word(cls, ancestor_key):
        return cls.query(ancestor=ancestor_key)

