from fastapi import FastAPI, Path, HTTPException, Query # path is used for explanability 
import json
 
app = FastAPI()

#create a helper function to load the data from json file
def load_data():
    with open("vaccine_records.json", "r") as f:
        data = json.load(f)
        #print(data.keys())
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


# to locate a specific record - use path parameter.
@app.get("/record/{record_id}")
def view_record(record_id : str = Path(..., description="ID of the record in DB", example = 1)):
    data = load_data()
    if record_id in data:
        return data[record_id]
    return HTTPException(status_code=404, detail="record not found")

@app.get("/sort")
def sort_records(sort_by: str = Query(..., description = "sort on the basis of age or dose"), order: str = Query('asc', description = 'sort in asc or desc order' )):
    valid = ['age', 'dose']
    if sort_by not in valid:
        return HTTPException(status_code = 400, detail = f"invalid field. Select from {valid} ")
    if order not in ['asc', 'desc']:
        return HTTPException(status_code = 400, detail = "invalid order. Say asc/desc")
    
    data = load_data()
    sort_order  = True if order=='desc' else False
    sorted_data = sorted(data.values(), key = lambda x : x.get(sort_by, 0), reverse = sort_order)
    return sorted_data

@app.get("/paginated")
def get_paginated_records(skip: int = 0, limit: int=4):
    data = load_data()
    data_list = list(data.values())
    return data_list[skip : skip + limit]





    

