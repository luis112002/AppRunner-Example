from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import random

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    labels = [f"Item {i}" for i in range(1, 6)]
    data = [random.randint(10, 100) for _ in labels]
    return templates.TemplateResponse("index.html", {
        "request": request,
        "labels": labels,
        "data": data
    })
