import requests
import json

__version__ = 1.0
__author__ = 'Islam Bahnasy'
__email__ = 'islam@cybertechlab.com'
__url__  = 'http://cybertechlab.com'



class DiffbotMWException(Exception):
	''' DiffbotMW Exception class 
	
	Code 401: Invalid Token
	Code 500: Invalid API or wrong URL

	'''
	def __init__(self, errCode, errMsg):
		self.errCode = errCode
		self.errMsg = errMsg
	    
	def __str__(self):
		return ("<DiffbotMWException: %s %s>" % (self.errCode, self.errMsg))


def diffbot_mw(token, url, api, fields, version):
	''' Sends HTTP GET request to the DiffbotMW API and returns 

	JSON object of the result in case of success or 
	raise 'DiffbotMWException' withe error code and message

	token:   developer token for authentication
	url:     target web page
	api:     type of API like 'article', 'image'
	fields:	 specify desired output fields or '*' to return all fields
	version: API version

	example: 
	from diffbot_mw import diffbot_mw
	json_obj = diffbot_mw('...', 'http://...', 'article', 
				fields=['*'], version=2)

	'''

	payload = { 'token': token, 'url': url, 'fields': fields }
	response = requests.get("http://api.diffbot.com/v" + str(version) + "/" +
							str(api), params=payload)
	json_obj = response.json()

	if response.status_code != 200:
		raise DiffbotMWException(str(json_obj['errorCode']), \
								str(json_obj['error']))

	return json_obj
