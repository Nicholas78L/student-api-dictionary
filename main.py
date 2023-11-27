from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/api/v1/<word>')
def dictionary(word):
    result_dictionary = {'definition': word.upper(), 'word': word}
    return result_dictionary


if __name__ == '__main__':
    app.run(debug=True, port=5002)
