#!/usr/bin/python3

import sys
from diffbot_mw import diffbot_mw, DiffbotMWException
from pprint import pprint


token = ''
url = '\
		http://blog.diffbot.com/diffbot_mws-new-product-api-teaches-robots-to-shop-online/'
fields = []
api = 'article'
result = ''

try:
	# now time to call diffbot_mw() to retrieve the results
	result = diffbot_mw(token, url, api, fields, version=2)
	# print the output JSON object in nice format
	pprint(result)

except DiffbotMWException as err:
	print (err)
	sys.exit()
