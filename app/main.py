from fastapi import Body, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from bson import ObjectId
from typing import List
from models.docModels.doc import DocumentModel, UpdateDocumentModel, createDocumentModel
# from models.catModels.categoria import CategoriaModel, UpdateCategoriaModel, createCategoriaModel
# from models.invModels.inventario import InventarioModel, UpdateInventarioModel, createInventarioModel
from components.db.conn import db
from components.api.api import app

#Ruta principal
@app.get("/", response_description="API saying hello")
async def read_root():
    return {"Hello": "World"}

#Ruta para obtener todos los documentos
@app.get("/document", response_description="All documents here", response_model=List[DocumentModel])
async def get_documents():
    return list(db["Documento"].find())

#Ruta para obtener un documento por su id
@app.get("/document/{id}", response_description="Single document here", response_model=DocumentModel)
async def get_document_by_id(id: str):
    if( doc := db["Documento"].find_one({ "_id": ObjectId(id) })) is not None:
        return doc
    raise HTTPException(status_code=404, detail=f"Document with id {id} not found")

#Ruta para crear un documento
@app.post("/document/new", response_description="New document added", response_model=DocumentModel)
async def create_document(document: createDocumentModel = Body(...)):
    db["Documento"].insert_one(dict(document))
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder(document))

#Ruta para actualizar un documento
@app.put("/document/{id}", response_description="Document updated", response_model=DocumentModel)
async def update_document(id: str, doc: UpdateDocumentModel = Body(...)):
    doc = {k: v for k, v in doc.dict().items() if v is not None}

    if len(doc) >= 1:
        update_result = db["Documento"].update_one({ "_id": ObjectId(id) }, {"$set": doc})

        if update_result.modified_count == 1:
            if( updated_doc := db["Documento"].find_one({ "_id": ObjectId(id) }) ) is not None:
                return updated_doc

    if( existin_doc := db["Documento"].find_one({ "_id": ObjectId(id) }) ) is not None:
        return existin_doc

    raise HTTPException(status_code=404, detail=f"Document {id} not found")

#Ruta para eliminar un documento
@app.delete("/document/{id}", response_description="Document deleted")
async def delete_document(id: str):
    delete_result = db["Documento"].delete_one({ "_id": ObjectId(id) })

    if delete_result.deleted_count == 1:
        return {"message": f"Document with id {id} deleted successfully"}

    raise HTTPException(status_code=404, detail=f"Document {id} not found")