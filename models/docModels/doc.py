from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from models.objectId.objectId import PyObjectId

class DocumentModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    Titulo: str = Field(...)
    Autor: str = Field(...)
    Editorial: str = Field(...)
    Genero: str = Field(...)
    Edicion: str = Field(...)
    Icbn: str = Field(...)
    anoPublicacion: str = Field(...)

    class Config:
        json_encoders = { ObjectId: str }

class createDocumentModel(BaseModel):
    Titulo: str = Field(...)
    Autor: str = Field(...)
    Editorial: str = Field(...)
    Genero: str = Field(...)
    Edicion: str = Field(...)
    Icbn: str = Field(...)
    anoPublicacion: str = Field(...)

class UpdateDocumentModel(BaseModel):
    Titulo: Optional[str]
    Autor: Optional[str]
    Editorial: Optional[str]
    Genero: Optional[str]
    Edicion: Optional[str]
    Icbn: Optional[str]
    anoPublicacion: Optional[str]

    class Config:
        json_encoders = { ObjectId: str }