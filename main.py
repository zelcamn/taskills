from flask import Flask, request
import requests

app = Flask(__name__)
GlobaldataArd = ''
GlobaldataSoft = ''

@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


@app.route('/DataArduino/', methods=['POST', 'GET'])
def DataArduino():
    if request.method == 'POST':
        global GlobaldataSoft
        data = GlobaldataSoft
        return data
    elif request.method == 'GET':
        global Globaldata
        data = GlobaldataArd
        print(request.form['data'])
        return "success"


def dataSoft():
    return req


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
