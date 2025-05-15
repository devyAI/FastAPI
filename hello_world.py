from fastapi import FastAPI

#creating a simple endpoint
app = FastAPI()

#define route for endpoint
@app.get("/")
def hello():
    return {"message" : "hello devyani"}

@app.get("/info")
def intro():
    return {"message" : "i am trying to learn fastAPI"}