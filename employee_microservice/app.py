from typing import List
from fastapi import FastAPI  # type: ignore
from fastapi.exceptions import HTTPException  # type: ignore
from fastapi.responses import HTMLResponse  # type: ignore 
from models.models import Employee, Index

app = FastAPI()


employees_db: List[Employee] = [] 

@app.get("/", response_model=Index)
async def index():
    return Index(health="healthy", status="running new")




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


@app.get("/employees", response_model=List[Employee])
async def get_employees():
    # Placeholder implementation - replace with actual employee data retrieval
    return employees_db


@app.get("/employees/{employee_id}", response_model=Employee)
async def get_employee(employee_id: int):
    # Placeholder implementation - replace with actual employee data retrieval
    for employee in employees_db:
        if employee.id == employee_id:
            return employee
    raise HTTPException(status_code=404, detail="Employee not found")


@app.post("/add_employee", response_model=Employee)
async def add_employee(employee: Employee):
    employees_db.append(employee)
    return employee
       

@app.put("/update_employee/{employee_id}", response_model=Employee)
async def update_employee(employee_id: int, employee: Employee):
    for index, emp in enumerate(employees_db):
        if emp.id == employee_id:
            employees_db[index] = employee
            return employee
    raise HTTPException(status_code=404, detail=f"Employee {employee_id} not found")

@app.delete("/delete_employee/{employee_id}", response_model=Employee)
async def delete_employee(employee_id: int):
    for index, emp in enumerate(employees_db):
        if emp.id == employee_id:
            return employees_db.pop(index)
    raise HTTPException(status_code=404, detail=f"Employee {employee_id} not found")    