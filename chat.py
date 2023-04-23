import wikipedia
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/message', methods=['POST'])
def reply():
    msg = request.get_json()['message']
    try:
        # Try to get a summary from Wikipedia
        summary = wikipedia.summary(msg)
        return jsonify({'response': summary})
    except:
        # If the query is not recognized, return an error message
        return jsonify({'response': "I'm sorry, I don't know what you mean."})

if __name__ == '__main__':
    app.run(debug=True)
