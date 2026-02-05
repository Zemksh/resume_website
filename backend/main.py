from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/items/")
async def create_item():
    return {"created succesfully"}

@app.get("/items/{item_id}")
async def get_items():
    return {"returned succesfully"}

@app.put("/items/{item_id}")
async def update_item(item_id: int):
    return {"updated succesfully"}  

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"deleted succesfully"}