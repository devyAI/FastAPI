from fastapi import FastAPI
import json
 
app = FastAPI()

#create a helper function to load the data from json file
def load_data():
    with open("vaccine_records.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/")
def root():
    return {"message" : "VACCINE DOSE TRACKING API "}

@app.get("/about")
def about():
    return {"message": "This API helps track your vaccine doses"}

@app.get("/view")
def view():
    data = load_data()
    return data
