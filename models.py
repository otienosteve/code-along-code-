from sqlalchemy import create_engine,Column, Integer, String,Float,ForeignKey,DATETIME
from sqlalchemy.orm import declarative_base,sessionmaker,relationship,backref

Base = declarative_base()
import datetime 

class Student(Base):
    __tablename__ = 'student'
    id= Column(Integer,primary_key=True)
    first_name = Column(String(40), nullable=False)
    last_name = Column(String(40), nullable=False)
    age = Column(Integer, nullable=False)
    home_town = Column(Integer, nullable=False)

    biodata= relationship('BioData', backref='student')
    payment = relationship('Payment',backref='student')

    def __repr__(self):
        return f'<Student: {self.first_name}>'
    
class BioData(Base):
    __tablename__= 'biodata'
    aspiration = Column(String(40), nullable=False)
    religion = Column(String(40), nullable=False)
    nationality = Column(String(40), nullable=False)
    highschool = Column(String(40), nullable=False)
    student_id= Column(Integer,ForeignKey('student.id'))

class Payment(Base):
    __tablename__= 'payment'
    id= Column(Integer,primary_key=True)
    amount = Column(Float,nullable=False)
    description = Column(String(50),nullable=False)
    date = Column(DATETIME,default=datetime.now())
    student_id = Column(Integer, ForeignKey('student.id'))

class Class(Base):
    __tablename__= 'class'
    id = Column(Integer,primary_key=True)
    name = Column(String(50), nullable=False)






engine= create_engine('sqlite:///db.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()