from sqlalchemy import and_

from .connect import DatabaseConnection
from .schema import Data


class CrudOperations:
    """
    offers basic crud-operations for Data-Table

    Raises:
        AttributeError: when you attempt to access an attribute that does not exist
        IntegrityError: when you try to do something that would violate
                        the constraints configured on a Column or Table

    """

    def __init__(self, db_connection: DatabaseConnection):
        """
        Args:
            db_connection: database connection
        """
        self.db_connection = db_connection

    def put_data(self, data: dict) -> dict:
        """
        import data to database
        Returns:
            id of stored data
            data as a dictionary with schema format
        """
        f = Data(**data)
        self.db_connection.session.add(f)
        self.db_connection.session.commit()
        return dict(id=f.id, data=data)

    def put_bulk(self, bulk_data: list):
        """
        insert a bulk of objects
        Args:
            bulk_data: list of data with a form of data in schema
        Returns:
            list of data with schema format
        """
        self.db_connection.session.bulk_save_objects(bulk_data)
        self.db_connection.session.commit()
        return bulk_data

    def get_data(self, id: int):
        """
        return data with certain id from database
        Returns:
            data as dict
        """
        out = {}
        getdata = self.db_connection.session.query(Data).filter(Data.id == id).all()
        for item in getdata:
            out.update(item.__dict__)
        return out

    def query_with_filter(self, **kwargs):
        """
        query data with specific filters
        Args:
            **kwargs: given query dict
                Ex. {'name': 'carl'}
        Returns:
            data as dict
        """
        query_filter = (getattr(Data, key) == value for key, value in kwargs.items())
        print(query_filter)

        data = self.db_connection.session.query(Data).filter(and_(query_filter)).all()

        return [item.__dict__ for item in data]

    def update_data(self, id: int, data: dict):
        """
        update data with certain id
        Args:
            id: row id
            data: as dict
        Returns:
            data up to date
        """
        update_data = dict(id=id)
        update_data.update(data)
        self.db_connection.session.bulk_update_mappings(Data, [update_data])
        self.db_connection.session.commit()
        return update_data

    def delete_data(self, id: int):
        """
        delete data with certain id from database
        Args:
            id: id need to be deleted
        Returns:
            1 if success, 0 if not
        """
        f = self.db_connection.session.query(Data).filter(Data.id == id).delete()
        self.db_connection.session.commit()
        return f
