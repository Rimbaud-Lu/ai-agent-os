from fastapi import FastAPI
from openclaw.scheduler.workflow_engine import run_workflow

app = FastAPI()

@app.get("/")
def root():
    return {"status":"AI Agent OS running"}

@app.post("/task")
def task(body: dict):
    return run_workflow(body["content"])
