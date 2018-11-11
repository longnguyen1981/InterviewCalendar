from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from urllib.parse import urlparse

from .schema import Base


class DatabaseConnection:
    """
    create and connect to db using sqalchemy orm
    """

    def __init__(self, username, password, dbname, dbtype='postgres', host='localhost', port=5432):
        """
        connect to database
        Args:
            username: username
            password: password for this username
            dbname:  database name
            dbtype: drivername (Ex. postgres)
            host: host (Ex. localhost)
            port: port (Ex. 5432 for localhost)
        """
        db_path = URL(drivername=dbtype,
                      username=username,
                      password=password,
                      host=host,
                      port=port,
                      database=dbname)
        self.engine = create_engine(db_path)
        Base.metadata.create_all(bind=self.engine)
        session = sessionmaker()
        session.configure(bind=self.engine)
        self.session = session()

    def __delete__(self, instance):
        """
        auto close the db when the instance is not used
        """
        self.session.close()

    @classmethod
    def init_from_url(cls, url):
        """
        initialize database from url type
        """
        init_kwargs = cls._validate_init_kwargs(url)
        return cls(**init_kwargs)

    @staticmethod
    def _validate_init_kwargs(url: str) -> dict:
        """
        validates url and returns keyword arguments used for __init__
        Args:
            url: in a form: dbtype://username:password@localhost:5432/dbname
                 if url without dbtype, username:password@localhost:5432/dbname,
                    then dbtype is postgres as a default
        Returns:
            dict with keys: username, password, dbname, dbtype, host, port)
        """
        if '://' not in str(url):
            url = 'postgres://' + url
        p = urlparse(url)
        return dict(username=p.username,
                    password=p.password,
                    dbname=p.path.split('/')[1],
                    dbtype=p.scheme,
                    host=p.hostname,
                    port=p.port
                    )
