#!/usr/bin/python

import cgi
import glob
import random
import sys
import simplejson as json

sys.path.append('./lib')


import wordlist 

from mako.template import Template
from mako.lookup import TemplateLookup

_lookup = TemplateLookup(directories = ['template',])


def _pick(l):
	return l[random.randrange(len(l))]

def sentence():
	hackwords = []
	item = _pick(wordlist.ITEM)

	if isinstance(item, tuple):
		plural = item[1]
		item = item[0]
	else:
		plural = False
	
	intro = _pick(wordlist.INTRO)

	for wlist in wordlist.SOCIOPOLITICAL, wordlist.PHYSICAL:
		hackwords.append(_pick(wlist))
	
	hackwords.append(item)
	
	resp = _pick(wordlist.RESPONSES)

	if plural:
		intro = "%s some" % intro
	else:
		if hackwords[0][0] in ('a', 'e', 'i', 'o', 'u'):
			intro = "%s an" % intro
		else:
			intro = "%s a" % intro
	return intro, hackwords, resp

def ajax():
	(intro, hackwords, resp) = sentence()

	phrase = intro + " " + " ".join(hackwords)	
	
	data = {
		'intro': intro,
		'hackvars': hackwords,
		'response': resp,
		'bg': getbg(),
		'phrase': phrase,
	}
	print "Content-type: text/json\n"

	print json.dumps(data)


def index():
	print "Content-type: text/html\n"
	print _lookup.get_template('index.html').render()

def getbg():
	choices = glob.glob('static/hackbg*')
	return _pick(choices)

def main():
	fs = cgi.FieldStorage()
	if 'ajax' in fs:
		ajax()
	else:
		index()


if __name__ == '__main__':
	main()
