from fastapi import FastAPI  # type: ignore
from pydantic import BaseModel  


app = FastAPI()

## Output model for the index route
class Index(BaseModel):
    health: str
    status: str
    

@app.get("/", response_model=Index)
def index():
    return Index(health="healthy", status="running")