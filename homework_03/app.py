from fastapi import FastAPI

app=FastAPI()

@app.get("/ping/")
def pingapp():
    return {"message": "pong"}
