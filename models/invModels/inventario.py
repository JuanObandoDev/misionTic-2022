from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from models.objectId.objectId import PyObjectId

class InventarioModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    Icbn: str = Field(...)
    cantidad: str = Field(...)
    Editorial: str = Field(...)
    ubicacion: str = Field(...)

    class Config:
        json_encoders = { ObjectId: str }

class createInventarioModel(BaseModel):
    Icbn: str = Field(...)
    cantidad: str = Field(...)
    Editorial: str = Field(...)
    ubicacion: str = Field(...)

class UpdateInventarioModel(BaseModel):
    Icbn: Optional[str]
    cantidad: Optional[str]
    Editorial: Optional[str]
    ubicacion: Optional[str]

    class Config:
        json_encoders = { ObjectId: str }