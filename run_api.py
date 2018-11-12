from flask import Flask, make_response, request, jsonify
import json
from company.interviewcalendar.src.mapping import map_calendar, validate_time
from company.interviewcalendar.database.crud import CrudOperations, DatabaseConnection
from setting import args

app = Flask(__name__)

db_connection = DatabaseConnection(args.username, args.password, args.dbname, args.dbtype, args.host, args.port)

my_crud = CrudOperations(db_connection)


@app.route('/health')
def health_check():
    """
    simple health-check
    """
    return make_response('OK',200)


@app.route('/add', methods=['POST'])
def add_data():
    if request.method == 'POST':
        input_data = json.loads(request.data.decode('utf-8'))
        validate = validate_time(input_data['data'])
        if validate['code'] == 200:
            list_add = my_crud.put_bulk(validate['response'])
            validate['response'] = jsonify(list_add)
        return make_response(validate['response'], validate['code'])


@app.route('/get/<name>', methods=['GET', 'POST'])
def get_data(name):
    if request.method == 'GET':
        query_string = {'name': name}
        list_data = my_crud.query_with_filter(**query_string)
        return jsonify(data=list_data)


@app.route('/update/<id>', methods=['DELETE', 'PATCH'])
def update_data(id):
    if request.method == 'DELETE':
        success = my_crud.delete_data(id)
        if success == 1:
            return make_response('Successfully deleted', 200)
        else:
            return make_response('Could not delete', 403)

    if request.method == 'PATCH':
        input_data = json.loads(request.data.decode('utf-8'))
        validate = validate_time(input_data['data'])
        if validate['code'] == 200:
            update_data = my_crud.update_data(id, input_data['data'])
            validate['response'] = jsonify(update_data)
        return make_response(validate['response'], validate['code'])


@app.route('/map', methods=['POST'])
def map_data():
    if request.method == 'POST':
        input_data = json.loads(request.data.decode('utf-8'))
        avail = map_calendar(my_crud.query_by_listname(input_data['names']))
        return jsonify(result=avail)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)