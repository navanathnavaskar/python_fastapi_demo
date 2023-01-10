from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello Friends"}

@app.get("/items/{item_id}")
async def get_item(item_id:int):
    return {"Item ID" : item_id}