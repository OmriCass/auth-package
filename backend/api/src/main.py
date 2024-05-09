from fastapi import FastAPI

app = FastAPI()

user = []


@app.post('/register')
def register():
    return {}

@app.post('/login')
def login():
    return {}

@app.get('/unprotected')
def unprotected():
    return{"not" : "working"}

@app.get('/protected')
def protected():
    return 