from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import Date

from base import Base


class Pipe(Base):
    __tablename__ = "pipes"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    length = Column(Float)
    weight = Column(Float)
    add_date = Column(Date)
    delete_date = Column(Date)