from fastapi import Body, status, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from bson import ObjectId
from typing import List
from models.docModels.doc import DocumentModel, UpdateDocumentModel, createDocumentModel
from models.catModels.categoria import CategoriaModel, UpdateCategoriaModel, createCategoriaModel
from models.invModels.inventario import InventarioModel, UpdateInventarioModel, createInventarioModel
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

#Ruta para obtener todas las categorias
@app.get("/categoria", response_description="All categories here", response_model=List[CategoriaModel])
async def get_categorias():
    return list(db["Categoria"].find())

#Ruta para obtener una categoria por su id
@app.get("/categoria/{id}", response_description="Single category here", response_model=CategoriaModel)
async def get_categoria_by_id(id: str):
    if( cat := db["Categoria"].find_one({ "_id": ObjectId(id) })) is not None:
        return cat
    raise HTTPException(status_code=404, detail=f"Category with id {id} not found")

#Ruta para crear una categoria
@app.post("/categoria/new", response_description="New category added", response_model=CategoriaModel)
async def create_categoria(categoria: createCategoriaModel = Body(...)):
    db["Categoria"].insert_one(dict(categoria))
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder(categoria))

#Ruta para actualizar una categoria
@app.put("/categoria/{id}", response_description="Category updated", response_model=CategoriaModel)
async def update_categoria(id: str, cat: UpdateCategoriaModel = Body(...)):
    cat = {k: v for k, v in cat.dict().items() if v is not None}

    if len(cat) >= 1:
        update_result = db["Categoria"].update_one({ "_id": ObjectId(id) }, {"$set": cat})

        if update_result.modified_count == 1:
            if( updated_cat := db["Categoria"].find_one({ "_id": ObjectId(id) }) ) is not None:
                return updated_cat

    if( existin_cat := db["Categoria"].find_one({ "_id": ObjectId(id) }) ) is not None:
        return existin_cat

    raise HTTPException(status_code=404, detail=f"Category {id} not found")

#Ruta para eliminar una categoria
@app.delete("/categoria/{id}", response_description="Category deleted")
async def delete_categoria(id: str):
    delete_result = db["Categoria"].delete_one({ "_id": ObjectId(id) })

    if delete_result.deleted_count == 1:
        return {"message": f"Category with id {id} deleted successfully"}

    raise HTTPException(status_code=404, detail=f"Category {id} not found")

#Ruta para obtener todos los inventarios
@app.get("/inventario", response_description="All inventories here", response_model=List[InventarioModel])
async def get_inventarios():
    return list(db["Inventario"].find())

#Ruta para obtener un inventario por su id
@app.get("/inventario/{id}", response_description="Single inventory here", response_model=InventarioModel)
async def get_inventario_by_id(id: str):
    if( inv := db["Inventario"].find_one({ "_id": ObjectId(id) })) is not None:
        return inv
    raise HTTPException(status_code=404, detail=f"Inventory with id {id} not found")

#Ruta para crear un inventario
@app.post("/inventario/new", response_description="New inventory added", response_model=InventarioModel)
async def create_inventario(inventario: createInventarioModel = Body(...)):
    db["Inventario"].insert_one(dict(inventario))
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder(inventario))

#Ruta para actualizar un inventario
@app.put("/inventario/{id}", response_description="Inventory updated", response_model=InventarioModel)
async def update_inventario(id: str, inv: UpdateInventarioModel = Body(...)):
    inv = {k: v for k, v in inv.dict().items() if v is not None}

    if len(inv) >= 1:
        update_result = db["Inventario"].update_one({ "_id": ObjectId(id) }, {"$set": inv})

        if update_result.modified_count == 1:
            if( updated_inv := db["Inventario"].find_one({ "_id": ObjectId(id) }) ) is not None:
                return updated_inv

    if( existin_inv := db["Inventario"].find_one({ "_id": ObjectId(id) }) ) is not None:
        return existin_inv

    raise HTTPException(status_code=404, detail=f"Inventory {id} not found")

#Ruta para eliminar un inventario
@app.delete("/inventario/{id}", response_description="Inventory deleted")
async def delete_inventario(id: str):
    delete_result = db["Inventario"].delete_one({ "_id": ObjectId(id) })

    if delete_result.deleted_count == 1:
        return {"message": f"Inventory with id {id} deleted successfully"}

    raise HTTPException(status_code=404, detail=f"Inventory {id} not found")
    