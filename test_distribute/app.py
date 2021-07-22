from flask import Flask, render_template, jsonify, request, session

from dao import Database

app = Flask(__name__)

@app.route('/', methods=['GET'])
def usercheck():

    data = (id,)
    print(data)
    return Database.selectdb()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)