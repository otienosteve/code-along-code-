from datetime import datetime

from fastapi import FastAPI, HTTPException
from models import session, Student, Class, Payment, BioData
from pydantic import BaseModel

from typing import List

app = FastAPI()

class PaymentSchema(BaseModel):
    amount :float
    description: str
    date : datetime
    student_id: int
    class config:
        orm_mode= True

class BioDataSchema(BaseModel):
    aspiration : str
    religion: str
    nationality: str
    highschool: str
    student_id: int
    
    class config:
        orm_mode= True

class StudentSchema(BaseModel):
    id: int
    last_name: str
    first_name: str
    age: int
    home_town: str
    biodata: BioDataSchema
    
    class config:
        orm_mode= True

class ClassSchema(BaseModel):
    name : str


from typing import Optional

class StudentUpdateSchema(BaseModel):
    id: Optional[int] = None
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    age: Optional[int] = None
    home_town: Optional[str] = None

    class config:
        orm_mode= True




@app.get('/')
def index():
    return {'msg' : 'Welcome to fastapi'}


@app.get('/students', response_model=List[StudentSchema])
def get_all_students():
    #logic to query data from the database and return results to the user /client
    students = session.query(Student).all()
    return students

@app.get('/students/{id}', response_model=StudentSchema)
def get_one_student(id: int):
    #logic to query data for a single student from the database and return results to the user/ client
    student = session.query(Student).filter_by(id=id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student 

@app.post('/students')
def add_students(payload:StudentSchema):
    #logic for creating an instance from the payload and adding to the database 
    student = Student(**dict(payload))
    session.add(student)
    session.commit()
    return {"detail": "Student added SuccessfulLy"}
 
@app.put('/students/{id}')
def full_update_student(id:int, payload:StudentSchema):
    # logic to fully update student and persist changes in the database
    student = session.query(Student).filter_by(id=id).first()
    if not student:
        raise HTTPException(status_code=404,detail=f"No student with id {id} was found on our Database")
    for key,value in payload.dict(exclude_unset=True).items():
        setattr(student,key, value)
    session.commit()
    return {"detail":"student Updated Successfully"}  
  
@app.patch('/students/{id}',response_model=StudentSchema)
def partial_update_student(id:int, payload:StudentUpdateSchema):
    student = session.query(Student).filter_by(id=id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not Found")
    
    for key,value in payload.dict(exclude_unset=True).items():
        setattr(student, key, value)
    session.commit()

    return student

@app.delete('/students/{id}')
def delete_student(id: int):
    student = session.query(Student).filter_by(id=id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found ")
    session.delete(student)
    session.commit()
    return {"detail":f'Student with id {id} has been deleted successfully'}    

@app.get('/student_bio',response_model = List[BioDataSchema])
def student_bio():
    biodata = session.query(BioData).all()
    return biodata  

@app.get('/student_payment',response_model=List[PaymentSchema])
def student_payment():
    payments = session.query(Payment).all()
    return payments  

@app.get('/student_class',response_model=List[ClassSchema])
def student_class():
    classes = session.query(Class).all()
    return classes