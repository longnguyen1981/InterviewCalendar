from chemondis.interviewcalendar.database.crud import CrudOperations
from chemondis.interviewcalendar.database.crud import DatabaseConnection

def get_data_from_name(name):
    my_crud = CrudOperations(DatabaseConnection('postgres', 'pass', 'testdb'))
    query_string = {'name': name}
    return my_crud.query_with_filter(**query_string)

