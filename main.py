from flask import Flask, request
import requests
import serial


ser = serial.Serial('COM4', 9600)
app = Flask(__name__)
GlobaldataArd = ''
GlobaldataSoft = ''


@app.route('/', methods=['POST', 'GET'])
@app.route('/index')
def index():
    print(request.method)
    return "Привет"


@app.route('/dataArduino/', methods=['POST', 'GET'])
def DataArduino():
    if request.method == 'GET':
        global GlobaldataSoft
        data = GlobaldataSoft
        print(GlobaldataSoft)
        return data
    elif request.method == 'POST':
        global GlobaldataArd
        GlobaldataArd = request.args
        print(request.args)
        return request.args


@app.route('/dataSoft', methods=['POST', 'GET'])
def dataSoft():
    print(request.method)
    if request.method == 'GET':
        global GlobaldataSoft
        data = str(ser.readline()[2:-5].decode('UTF-8'))
        print(data)
        return data
    elif request.method == 'POST':
        global GlobaldataSoft
        GlobaldataSoft = request.get_data()
        print(request.get_data())
        return "success"


if __name__ == '__main__':
    app.run(port=8080, host='192.168.88.248')
