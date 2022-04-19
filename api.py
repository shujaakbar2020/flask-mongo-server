from flask import Flask, request, json, Response
from crud import MongoAPI


app = Flask(__name__)


@app.route('/')
def base():
    return Response(response=json.dumps({'status': 'UP'}), status=200, mimetype='application/json')


@app.route('/data', methods=['GET'])
def mongo_read():
    data = request.json
    if data is None or data=={}:
        return Response(response=json.dumps({'status': 'Error please provide connection info'}), status=400, mimetype='application/json')

    return Response(response=json.dumps(data), status=200, mimetype='application/json')


@app.route('/data', methods=['POST'])
def mongo_write():
    data = request.json
    if data is None or data=={} or 'Document' not in data:
        return Response(response=json.dumps({'status': 'Error please provide coonection info'}), status=400, mimetype='application/')

    return Response(response=json.dumps(data), status=201, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
