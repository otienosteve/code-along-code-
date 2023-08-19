from fastapi import FastAPI
from models import session, Student

app = FastAPI()

@app.get('/')
def index():
    return {'msg' : 'Welcome to fastapi'}


@app.get('/students')
def get_all_students():
    #logic to query data from the database and return results to the user /client
    students = session.query(Student).all()
    return students

@app.get('/students/{id}')
def get_one_student(id: int):
    #logic to query data for a single student from the database and return results to the user/ client
    return {'msg':f'student {id}'} 