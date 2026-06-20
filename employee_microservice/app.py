from fastapi import FastAPI  # type: ignore
from pydantic import BaseModel 
from fastapi.responses import HTMLResponse  # type: ignore 


app = FastAPI()

## Output model for the index route
class Index(BaseModel):
    health: str
    status: str
    

@app.get("/", response_model=Index)
async def index():
    return Index(health="healthy", status="running")




## To return an HTML response, we can use the HTMLResponse class from FastAPI.
@app.get('/home', response_class=HTMLResponse)
def html_page():
    return """
    <html>
        <head><title>My Page</title></head>
        <body>
            <h1>Hello from FastAPI!</h1>
            <p>This is a plain HTML response.</p>
        </body>
    </html>
    """
