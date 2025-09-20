from flask import Flask



app=Flask(__name__)


@app.route('/')
def home():
    return "Hello World..!"


@app.route('/api')
def api():
    return "Hello From Api...!"



if __name__=='__main__':
    app.run(debug=True)
