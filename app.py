from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'], endpoint='index_page')
def index():
    if request.method == 'POST':
        query = request.form['query']
        response = requests.get(f'https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch={query}&utf8=1&formatversion=2')

        if response.status_code == 200 and 'query' in response.json():
            results = response.json()['query']['search']
            return render_template('index.html', results=results, query=query)
        else:
            return render_template('index.html', error="Error retrieving data from the API")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
