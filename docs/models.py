from sqlalchemy import Column, Integer, String
from database import Base
import os

class Doc(Base):
    __tablename__ = 'g2w_local_docs'
    id = Column('doc_id', Integer, primary_key=True, autoincrement=True)
    name = Column('doc_name', String(100), nullable=False)
    path = Column('doc_path', String(255), nullable=False)
    slag = Column('doc_slag', String(50),  nullable=False, unique=True)

    def __init__(self, name=None, path=None, slag=None):
        self.name = name
        self.path = path
        self.slag = slag

    def __repr__(self):
        return '<Doc id=%r, name=%r, path=%r, slag=%r>' % (self.id, self.name, self.path, self.slag)
