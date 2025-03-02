from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API FastAPI rodando!"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "description": f"Item {item_id}"}
