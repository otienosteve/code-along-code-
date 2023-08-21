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