from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'msg' : 'Welcome to fastapi'}