from sqlalchemy import Integer, VARCHAR, Column
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)

    name = Column(VARCHAR)
    fromhour = Column(Integer)
    tohour = Column(Integer)
    day = Column(Integer)

