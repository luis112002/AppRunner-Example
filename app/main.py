from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import random
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Montar carpeta static para servir archivos CSS
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    labels = [f"Item {i}" for i in range(1, 6)]
    data = [random.randint(10, 100) for _ in labels]
    return templates.TemplateResponse("index.html", {
        "request": request,
        "labels": labels,
        "data": data
    })
