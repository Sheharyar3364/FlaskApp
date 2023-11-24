from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

texts =['First Page', 'Second Page', 'Third Page']

@app.route('/first')
def first():
    return texts[0]

@app.route('/second')
def second():
    return texts[1]

@app.route('/third')
def third():
    return texts[2]

if __name__ == '__main__':
    app.run(debug=True)