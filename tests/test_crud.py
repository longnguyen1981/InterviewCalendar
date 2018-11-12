from unittest import TestCase
import testing.postgresql

from chemondis.interviewcalendar.database.crud import DatabaseConnection
from chemondis.interviewcalendar.database.crud  import Data
from chemondis.interviewcalendar.database.crud  import CrudOperations


Postgresql = testing.postgresql.PostgresqlFactory(cache_initialized_db=True)


class TestCrud(TestCase):
    def setUp(self):
        self.postgresql = Postgresql()
        self.db_connection = DatabaseConnection.init_from_url(self.postgresql.url())
        self.crud = CrudOperations(self.db_connection)
        self.data = [{'name': 'name1', 'fromhour': 8, 'tohour': 14, 'day': 4}, {'name': 'name2', 'fromhour': 9, 'tohour': 12, 'day': 4}]

    def test_put_data(self):
        putdata = self.crud.put_data(self.data[0])
        self.assertEqual(putdata['data']['name'], self.data[0]['name'])
        self.assertIsInstance(putdata['id'], int)

    def test_put_bulk(self):
        out = self.crud.put_bulk(self.data)
        for item in out:
            self.assertEqual(item['day'], 4)

    def test_get_data(self):
        self.crud.put_data(self.data[0])
        getdata = self.crud.get_data(id=1)
        self.assertEqual(getdata['id'], 1)
        self.assertEqual(getdata['name'], 'name1')
        self.assertEqual(getdata['fromhour'], 8)
        self.assertEqual(getdata['tohour'], 14)

    def test_query_with_filter(self):
        self.crud.put_bulk(self.data)
        query = {'name': 'name3'}
        out = self.crud.query_with_filter(**query)
        self.assertEqual(len(out), 0)
        query = {'name': 'name1'}
        out = self.crud.query_with_filter(**query)
        for item in out:
            self.assertEqual(item['day'], 4)

    def test_query_by_listname(self):
        self.crud.put_bulk(self.data)
        out = self.crud.query_by_listname(['name1', 'name2'])
        self.assertEqual(len(out), 2)
        for item in out:
            self.assertEqual(item['day'], 4)

    def test_update_data(self):
        self.crud.put_bulk(self.data)
        updatedata = {'name': 'name3', 'fromhour': 8, 'tohour': 14, 'day': 4}
        out = self.crud.update_data(id=1, data=updatedata)
        self.assertEqual(out['id'], 1)
        query = self.db_connection.session.query(Data).filter(Data.id == 1).all()
        self.assertEqual(query[0].__dict__['id'], 1)
        self.assertEqual(query[0].__dict__['name'], updatedata['name'])

    def test_delete_data(self):
        self.crud.put_bulk(self.data)
        out = self.crud.delete_data(2)
        self.assertEqual(out, 1)
        query = self.db_connection.session.query(Data). \
            filter(Data.id == 2).all()
        self.assertEqual(len(query), 0)

    def tearDown(self):
        self.db_connection.session.close()
        self.postgresql.stop()

    def tearDownModule(self):
        Postgresql.clear_cache()




