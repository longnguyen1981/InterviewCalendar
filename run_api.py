from flask import Flask, make_response, request, jsonify
import json
from chemondis.interviewcalendar.src.mapping import map_calendar
from chemondis.interviewcalendar.database.crud import CrudOperations, DatabaseConnection

app = Flask(__name__)

my_crud = CrudOperations(DatabaseConnection('postgres', 'pass', 'testdb'))


@app.route('/health')
def health_check():
    """
    simple health-check
    """
    return make_response('OK',200)


@app.route('/addcalendar', methods=['POST'])
def add_data():
    if request.method == 'POST':
        input_data = json.loads(request.data.decode('utf-8'))
        list_add = my_crud.put_bulk(input_data['data'])
        return jsonify(list_add)


@app.route('/getcalendar/<name>', methods=['GET', 'POST'])
def get_data(name):
    if request.method == 'GET':
        query_string = {'name': name}
        list_out = my_crud.query_with_filter(**query_string)
        return jsonify(data=list_out)


@app.route('/updatecalendar/<id>', methods=['DELETE', 'PATCH'])
def update_data(id):
    if request.method == 'DELETE':
        success = my_crud.delete_data(id)
        return jsonify(success)

    if request.method == 'PATCH':
        input_data = json.loads(request.data.decode('utf-8'))
        update_data = my_crud.update_data(id, input_data['data'])
        return jsonify(update_data)


@app.route('/mapcalendar', methods=['POST'])
def map_data():
    if request.method == 'POST':
        input_data = json.loads(request.data.decode('utf-8'))
        avail = map_calendar(my_crud.query_by_listname(input_data['data']))
        return jsonify(data=avail)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)