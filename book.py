#!/usr/bin/env python3

""" analysis of book alice to practice text processing
"""
__author__ = 'Miroslav Ivan'
__version__ = '0.1'

import requests

BOOK_ONLINE = 'http://openbookproject.net/thinkcs/python/english2e/resources/ch10/alice_in_wonderland.txt'

book = requests.get(BOOK_ONLINE)

word_list = {}
for line in book.text.split('\n'):
    for word in line.split(' '):
        word_list.get(word) =

