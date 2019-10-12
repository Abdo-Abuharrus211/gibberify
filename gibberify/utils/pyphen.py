# Copyright 2019-2019 the gibberify authors. See copying.md for legal info.

"""
Pyphen-based utilities used in other modules
"""

import pyphen
from collections import OrderedDict


def super_hyphenator():
    """
    :return: a list of pyphen.Pyphen instances for a fixed list of languages
    """
    langs = ["en", "it", "de", "fr", "ru", "es", "nl", "ca", "el", "et", "is", "lt", "nb", "pt", "sk"]
    return [pyphen.Pyphen(lang=hyph_lang) for hyph_lang in langs]


def syllabize(word):
    """
    takes a word and reduces it to fundamental syllables using a list of
    pyphen hyphenators from several different languages

    :param word: a single word
    :return: a set of syllables
    """
    word = word.lower()

    # first get rid of apostrophes and such by splitting the word in sub-words
    syl = word.split('\'')

    # hyphenize using a bunch of languages. This ensures we cut down syllables to the most fundamental ones
    # TODO: using pyphen.LANGUAGES is kinda overkill, for now reverting back to using a fixed list
    hyph_list = super_hyphenator()
    for hyph in hyph_list:
        # do some list comprehension black magic to split up everything nicely
        syl = [s for w in syl for s in hyph.inserted(w).strip().split('-')]

    # nice trick to maintain order
    syllables = list(OrderedDict.fromkeys(syl))

    return syllables
