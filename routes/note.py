from fastapi import APIRouter
from fastapi import Request, Form
from fastapi.responses import   HTMLResponse
from typing import Annotated
from config.db import conn
from fastapi.templating import Jinja2Templates


note = APIRouter() 
templates= Jinja2Templates(directory="templates")



@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs=conn.Fastapi.notes.find({})
    newDocs=[]

    for doc in docs:

        newDocs.append({
            "id":doc["_id"],
            "title":doc["title"],
            "desc":doc["desc"],



        })
    
    return templates.TemplateResponse("index.html", {"request": request, "notes": newDocs})

@note.post("/notes/")
async def login(title: Annotated[str, Form()], desc: Annotated[str, Form()]):
    note=conn.Fastapi.notes.insert_one({"title":title,"desc":desc})
    return {"Message":"Note added successfully",
        "title": title,
            "description": desc}

