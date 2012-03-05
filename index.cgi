#!/usr/bin/python

import random
import sys


import wordlist 

from mako.template import Template


def _pick(l):
	return l[random.randrange(len(l))]

def sentence():
	phrase = []
	plural = False

	item = _pick(wordlist.ITEM)

	if isinstance(item, tuple):
		plural = item[1]
		item = item[0]
	
	phrase.append(_pick(wordlist.INTRO))

	if plural:
		phrase.append(_pick(wordlist.BRIDGE))
	else:
		phrase.append('a')
	
	for wlist in wordlist.SOCIOPOLITICAL, wordlist.PHYSICAL, wordlist.ITEM:
		phrase.append(_pick(wlist))
	
	resp = _pick(wordlist.RESPONSES)

	return " ".join(phrase), resp




print "Content-type: text-html\n\n"

print sentence()[0]
