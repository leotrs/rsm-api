from tempfile import NamedTemporaryFile
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

import rsm

app = FastAPI()


# origins = [
#     "http://localhost:8000",
#     "http://localhost:8001",
#     "http://localhost:8002",
#     "http://localhost:8003",
#     "http://localhost:3000",
#     "http://localhost:3001",
#     "http://localhost:3002",
#     "http://localhost:3003",
# ]


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


OUTPUT = ""


class Body(BaseModel):
    src: str


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}


@app.put("/make")
def make(body: Body):
    output = rsm.render(body.src, True)
    global OUTPUT
    OUTPUT = output

    return {"src": body.src, "output": output}


@app.get("/view", response_class=HTMLResponse)
def view():
    return OUTPUT


@app.get("/debug")
def debug():
    return OUTPUT


# app.mount("/static", StaticFiles(directory="../../rsm-core/rsm/static"), name="static")
