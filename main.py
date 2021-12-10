from flask import Flask, request
import requests

app = Flask(__name__)
GlobaldataArd = ''
GlobaldataSoft = ''


@app.route('/', methods=['POST', 'GET'])
@app.route('/index')
def index():
    print(request.method)
    return "Привет, Яндекс!"


@app.route('/dataArduino/', methods=['POST', 'GET'])
def DataArduino():
    if request.method == 'GET':
        global GlobaldataSoft
        data = GlobaldataSoft
        return data
    elif request.method == 'POST':
        global GlobaldataArd
        GlobaldataArd = request.get_data()
        print(request.get_data())
        return "success"


@app.route('/dataSoft', methods=['POST', 'GET'])
def dataSoft():
    print(request.method)
    if request.method == 'GET':
        global GlobaldataSoft
        data = GlobaldataArd
        # return "test"
        return data
    elif request.method == 'POST':
        global GlobaldataSoft
        GlobaldataSoft = request.get_data()
        print(request.get_data())
        return "success"


@app.route('/login', methods=['GET', 'POST'])
def login():
    print(request.method)
    if request.method == 'POST':
        print("post")
    else:
        print("get")


if __name__ == '__main__':
    app.run(port=8080, host='192.168.88.248')
