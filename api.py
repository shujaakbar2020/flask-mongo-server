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
    
    obj = MongoAPI(data)
    response = obj.read()
    return Response(response=json.dumps(response), status=200, mimetype='application/json')


@app.route('/data', methods=['POST'])
def mongo_write():
    data = request.json
    if data is None or data=={} or 'Document' not in data:
        return Response(response=json.dumps({'status': 'Error please provide coonection info'}), status=400, mimetype='application/')

    obj = MongoAPI(data)
    response = obj.write(data)
    return Response(response=json.dumps(response), status=201, mimetype='application/json')


@app.route('/data', methods=['PUT'])
def mongo_update():
    data = request.json
    if data is None or data=={} or 'DataToBeUpdated' not in data:
        return Response(response=json.dumps({'status': 'Error please provide a valid connection info'}), status=400, mimetype='application/json')

    obj = MongoAPI(data)
    response = obj.update()
    return Response(response=json.dumps(response), status=202, mimetype='application/json')


@app.route('/data', methods=['DELETE'])
def mongo_delete():
    data = request.json
    if data is None or data=={} or 'Document' not in data:
        return Response(response=json.dumps({'status': 'Error please provide a valid connection'}), status=400, mimetype='application/json')
    obj = MongoAPI(data)
    response = obj.delete(data)
    return Response(response=json.dumps(response), status=204, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
