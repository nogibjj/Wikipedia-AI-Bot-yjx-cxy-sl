from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'], endpoint='index_page')
def index():
    if request.method == 'POST':
        query = request.form['query']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        category = request.form['category']
        location = request.form['location']
        language = request.form['language']

        api_url = f'https://en.wikipedia.org/w/api.php?action=query&list=search&format=json&srsearch={query}&utf8=1&formatversion=2'

        if start_date and end_date:
            api_url += f'&srprop=timestamp&srlimit=500&srwhat=text&srinfo=totalhits&srstart={start_date}&srend={end_date}'

        # Add more filters here according to the Wikipedia API documentation

        response = requests.get(api_url)

        if response.status_code == 200 and 'query' in response.json():
            results = response.json()['query']['search']
            return render_template('index.html', results=results, query=query)
        else:
            return render_template('index.html', error="Error retrieving data from the API")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
