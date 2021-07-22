from flask import Flask, render_template, jsonify, request, session

from dao import Database

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():

    return render_template("index.html")

@app.route('/show', methods=['GET'])
def usercheck():
    print("app")
    return Database.selectdb()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    # app.run(debug=True, host='127.0.0.1', port=5000)