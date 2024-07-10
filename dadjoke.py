import requests

'''
https://github.com/neoporcupine/dadjoke
Use API provided by the champions at https://icanhazdadjoke.com to get a random DadJoke.
If things mess up for some reason then return empty string.
'''


def GetDadJoke():
	try:
		r = requests.get(
			'https://icanhazdadjoke.com', 
			headers={"Accept": "application/json", "User-Agent": "My Library (https://github.com/neoporcupine/dadjoke)"}
		)
		joke = r.json()['joke']
	except:
		joke = ""
	return joke


if __name__ == '__main__':
	print(GetDadJoke())
