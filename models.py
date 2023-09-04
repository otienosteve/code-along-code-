import datetime

from sqlalchemy import create_engine,Column, Integer, String,Float,ForeignKey,DateTime,Table,func
from sqlalchemy.orm import declarative_base,sessionmaker,relationship

Base = declarative_base()

# association table 
student_class = Table(
    'student_class',
    Base.metadata,
    Column('student_id', ForeignKey('student.id'), primary_key=True),
    Column('class_id', ForeignKey('class.id'), primary_key=True),
    extend_existing=True,
)

#student Model
class Student(Base):
    __tablename__ = 'student'
    id= Column(Integer,primary_key=True)
    first_name = Column(String(40), nullable=False)
    last_name = Column(String(40), nullable=False)
    age = Column(Integer, nullable=False)
    home_town = Column(Integer, nullable=False)

    # relationships
    biodata= relationship('BioData', backref='student',uselist=False)
    payment = relationship('Payment',backref='student')
    classes = relationship('Class', secondary=student_class, back_populates='students')

    def __repr__(self):
        return f'<Student: {self.first_name}>'
    
# Biodata model
class BioData(Base):
    __tablename__= 'biodata'
    id= Column(Integer,primary_key=True)
    aspiration = Column(String(40), nullable=False)
    religion = Column(String(40), nullable=False)
    nationality = Column(String(40), nullable=False)
    highschool = Column(String(40), nullable=False)
    student_id= Column(Integer,ForeignKey('student.id'))

    def __repr__(self):
        return f'<BioData: {self.aspiration}>'
    


# Payment Model
class Payment(Base):
    __tablename__= 'payment'
    id= Column(Integer,primary_key=True)
    amount = Column(Float,nullable=False)
    description = Column(String(50),nullable=False)
    date = Column(DateTime(), server_default=func.now())
    student_id = Column(Integer, ForeignKey('student.id'))

    def __repr__(self):
        return f'<Payment: {self.description}>'

#class Model
class Class(Base):
    __tablename__= 'class'
    id = Column(Integer,primary_key=True)
    name = Column(String(50), nullable=False)
    students = relationship('Student', secondary=student_class, back_populates='classes')

    def __repr__(self):
        return f'<Student: {self.name}>'


engine= create_engine('sqlite:///db.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()