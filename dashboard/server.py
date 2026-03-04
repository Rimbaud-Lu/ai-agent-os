from fastapi import FastAPI

app = FastAPI()

@app.get("/metrics")
def metrics():

    return {"status":"running"}
