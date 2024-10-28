from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Calculator API!"}

@app.get("/calculate")
async def calculate(op: str, x: float, y: float):
    if op == "add":
        return {"result": x + y}
    elif op == "subtract":
        return {"result": x - y}
    elif op == "multiply":
        return {"result": x * y}
    elif op == "divide":
        if y == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        return {"result": x / y}
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")


