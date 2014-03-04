Diffbot

Handles Diffbot APIs fetching and returns JSON object of the result 
in case of success or raise 'DiffbotException' withe error code and message.     
This library makes a GET HTTP request to the Diffbot web API ex: "http://api.diffbot.com/v2/articles"

Example code:


from diffbot import diffbot, DiffbotException

json_obj = diffbot(token, url, api, fields, version)

	token	: free developer token can be get from here 'https://www.diffbot.com/plans/trial'
	url		: the target web page to be analyzed
	api     : type of API -> 'article', 'image', 'product', 'frontpage', 'classifier'
	fields  : the desired output fields that will be returned in the result
	version : the API version, curently '2'

	json_obj: JSON object


Example implementation in 'client.py' base don Python 3, 
just supply your own developer token to the 'token' variable.