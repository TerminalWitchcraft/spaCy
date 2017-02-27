from __future__ import print_function
import codecs
import pathlib
from .symbols import POS, NOUN, VERB, ADJ, PUNCT

try:
    import ujson as json
except ImportError:
    import json


class Lemmatizer(object):
    """
    class for spacy lemmatizer
    """
    lang = 'de'
    @classmethod
    def load(cls, path, rules=None):
        index = {}
        # Assuming all the decompresssed files from
        # http://www.lexiconista.com/datasets/lemmatization/
        # exists in lemmatizers directory
        language_index_path = path / 'lemmatizers' / 'lemmatization-de.txt'
        if language_index_path.exists():
            with language_index_path.open() as file_:
                index = read_index(file_)
        else:
            index = {}
        return cls(index, None, None)

    def __init__(self, index, exceptions, rules):
        self.index = index
        self.exceptions = exceptions
        self.rules = rules

    def __call__(self, string, univ_pos, morphology=None):
        lemmas = lemmatize(string)

def lemmatize(string, index, exceptions, rules):
    string = string.lower()
    forms = []
    if string in index or not string.isalpha():
        forms.append(index[string])
    else:
        forms.append(string)
    return set(forms)

def read_index(fileobj):
    index = {}
    for line in fileobj:
        pieces = line.split(" ")
        # mappings of query -> base_form
        index[pieces[1]] = pieces[0]
    return index
