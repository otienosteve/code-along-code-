from fastapi import FastAPI, HTTPException
from models import session, Student
from pydantic import BaseModel

from typing import List

app = FastAPI()

class StudentSchema(BaseModel):
    id: int
    last_name: str
    first_name: str
    age: int
    home_town: str

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