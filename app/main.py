import pymongo # solo para la conexion a la base de datos
from pydantic import BaseModel, Field # para crear modelos para cada entidad (usuario / documento) y sus campos
from fastapi import FastAPI # para crear la API
from bson import ObjectId # para convertir el id de mongo a string o viceversa
from typing import Optional, List # para usar en el metodo put o update de la API y poder actualizar solo algunos campos además de usar List para devolver una lista de documentos o usuarios

app = FastAPI(title = "Gestión documental", description = "API para la gestión documental de la empresa", version = "1.0.0") # creamos la API
client = pymongo.MongoClient() #Link de base de datos dentro de los parentesis del metodo MongoClient de pymongo
db = client.databaseName # reemplazar databaseName por el nombre de la base de datos en mongo

class PyObjectId(ObjectId):
    # PyObjectId es una clase que hereda de ObjectId de bson para poder convertir el id de mongo a string y viceversa
    # es indispensable para poder usar el id de mongo como string en la API
    # debe ir en cada api que se vaya a crear con mongo
    #Cada @classmethod es un metodo indispensable y obligatorio de usar de la forma como se expresa en el codigo
    # Status: OBLIGATORIA
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid object id')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')    

class DocumentoModel(BaseModel):
    # modelo para crear un documento
    # Status: OBLIGATORIA
    # se debe generar de la siguiente forma:
    # class NombreModel(BaseModel):
    #     campo1: tipoCampo1 = Field(...) # Field es para agregar una descripcion al campo
    #     campo2: tipoCampo2 = Field(...)

    #     class Config:
    #         # Config es para agregar una descripcion al modelo
    #         # la descripcion es opcional

    #         title = "Nombre del modelo"
    #         description = "Descripcion del modelo"
    #         version = "1.0.0"

    #         # json_encoders es obligatorio para poder usar el id de mongo como string en la API
    #         json_encoders = {ObjectId: str} # para convertir el id de mongo a string

    #         # schema_extra es para agregar un ejemplo de como debe ser el modelo
    #         # es opcional
    #         schema_extra = {
    #             "example": {
    #                 "campo1": "valorCampo1",
    #                 "campo2": "valorCampo2"
    #             }
    #         }

    # el campo id es opcional ya que mongo lo genera automaticamente
    # en caso de usar el campo id, debe ser de tipo PyObjectId

    # ejemplo de un modelo:

    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    nombre: str = Field(...)
    descripcion: str = Field(...)

    class Config:
        json_encoders = { ObjectId: str }

class UpdateDocumentoModel(BaseModel):
    # modelo para actualizar un documento
    # Status: OBLIGATORIA
    # se debe generar de la siguiente forma:
    # class NombreModel(BaseModel):
    #     campo1: Optional[tipoCampo1] = Field(...) # Field es para agregar una descripcion al campo
    #     campo2: Optional[tipoCampo2] = Field(...) # Optional es para que el campo sea opcional

    #     class Config:
    #         # Config es para agregar una descripcion al modelo
    #         # la descripcion es opcional

    #         title = "Nombre del modelo"
    #         description = "Descripcion del modelo"
    #         version = "1.0.0"
    
    #         # json_encoders es obligatorio para poder usar el id de mongo como string en la API
    #         json_encoders = {ObjectId: str} # para convertir el id de mongo a string

    #         # schema_extra es para agregar un ejemplo de como debe ser el modelo
    #         # es opcional
    #         schema_extra = {
    #             "example": {
    #                 "campo1": "valorCampo1",
    #                 "campo2": "valorCampo2"
    #             }
    #         }

    # el campo id no es necesario ya que no se debe actualizar

    # ejemplo de un modelo para actualizar:
    nombre: Optional[str]
    descripcion: Optional[str]

    class Config:
        json_encoders = { ObjectId: str }

class UserModel(BaseModel):
    # repetir la misma sintaxis de documento model pero para usuarios o distintas entidades
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    Nombre: str = Field(...)
    Apellidos: str = Field(...)
    Edad: int = Field(...)
    Curso: str = Field(...)

    class Config:
        json_encoders = { ObjectId: str }

class UpdateUserModel(BaseModel):    
    # repetir la misma sintaxis de update documento model pero para usuarios o distintas entidades
    Nombre: Optional[str]
    Apellidos: Optional[str]
    Edad: Optional[int]
    Curso: Optional[str]

    class Config:
        json_encoders = { ObjectId: str }

# Rutas de la API
# Ruta principal:
@app.get("/", response_description="API saying hello") # response description permite agregar una descripcion a la respuesta de la API en swagger
async def read_root():
    return {"Hello": "World"}

# Ruta para listar todos los usuarios
@app.get("/user/", response_model=List[UserModel]) # response model permite agregar un modelo a la respuesta de la API en swagger, OBLIGATORIO
async def getUsers():
    return list(db["Tripulantes"].find()) # db es la base de datos, "Tripulantes" es la coleccion, find() es para buscar todos los documentos de la coleccion y list() es para convertir el resultado de find() a una lista

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