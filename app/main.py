from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI(title = "Gestión documental", description = "API para la gestión documental de la empresa", version = "1.0.0")

Documents = [
    {
        "id": 1,
        "name": "Document 1",
        "description": "This is the first document"
    },
    {
        "id": 2,
        "name": "Document 2",
        "description": "This is the second document"
    },
    {
        "id": 3,
        "name": "Document 3",
        "description": "This is the third document"
    },
    {
        "id": 4,
        "name": "Document 4",
        "description": "This is the fourth document"
    },
]

Users = [
    {
        "id": 1,
        "name": "User 1",
        "description": "This is the first user"
    },
    {
        "id": 2,
        "name": "User 2",
        "description": "This is the second user"
    },
    {
        "id": 3,
        "name": "User 3",
        "description": "This is the third user"
    },
    {
        "id": 4,
        "name": "User 4",
        "description": "This is the fourth user"
    }
]

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/user/")
async def getUsers(skip: int = 0, limit: int = 10):
    return Users[skip: skip + limit]

@app.get("/user/{user_id}")
async def getUser(user_id: int):
    for user in Users:
        if user["id"] == user_id:
            return user
    return {"Data": "Not Found"}

@app.get("/document")
async def get_documents(skip: int = 0, limit: int = 10):
    return Documents[skip: skip + limit]

@app.get("/document/{document_id}")
async def get_document_by_id(document_id: int):
    for document in Documents:
        if document["id"] == document_id:
            return document
    return {"Error": "Document not found"}

@app.post("/document/new")
async def create_document(document: dict):
    Documents.append(document)
    return document

@app.put("/document/{document_id}")
async def update_document(document_id: int, documentEdit: dict):
    for index, document in enumerate(Documents):
        if document["id"] == document_id:
            Documents[index] = documentEdit
            return document
    return {"Error": "Document not found"}

@app.delete("/document/{document_id}")
async def delete_document(document_id: int):
    for index, document in enumerate(Documents):
        if document["id"] == document_id:
            Documents.pop(index)
            return {"Success": "Document deleted"}
    return {"Error": "Document not found"}