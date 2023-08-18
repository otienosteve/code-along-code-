from sqlalchemy import create_engine,Column, Integer, String
from sqlalchemy.orm import declarative_base,sessionmaker

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'
    id= Column(Integer,primary_key=True)
    first_name = Column(String(40), nullable=False)
    last_name = Column(String(40), nullable=False)
    age = Column(Integer, nullable=False)
    home_town = Column(Integer, nullable=False)

    def __repr__(self):
        return f'<Student: {self.first_name}>'


engine= create_engine('sqlite:///db.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()