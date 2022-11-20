from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from models.objectId.objectId import PyObjectId

class CategoriaModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    genero: str = Field(...)
    idioma: str = Field(...)
    Subgenero: str = Field(...)

    class Config:
        json_encoders = { ObjectId: str }

class createCategoriaModel(BaseModel):    
    genero: str = Field(...)
    idioma: str = Field(...)
    Subgenero: str = Field(...)

class UpdateCategoriaModel(BaseModel):
    genero: Optional[str]
    idioma: Optional[str]
    Subgenero: Optional[str]

    class Config:
        json_encoders = { ObjectId: str }