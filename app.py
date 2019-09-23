from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<query>', methods=['GET'])
def getQuery(query):
	response = requests.get('https://pokeapi.co/api/v2/pokemon-species/%s' % query)
	content = json.loads(response.content)
	try:
		value = int(query)
		return 'the pokemon with id %s is %s' % (query, content['name']) 
	except ValueError:
		return '%s has id %s' % (query, content['id'])


if __name__ == '__main__':
    app.run()
