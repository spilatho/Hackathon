from fastapi import FastAPI
import getLeaveDetails

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my API!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@app.get("/leaveDetails")
def read_leaveResources():
    return getLeaveDetails.getLeaveData()
