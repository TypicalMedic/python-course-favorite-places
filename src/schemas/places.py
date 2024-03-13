from typing import Optional

from pydantic import BaseModel, Field

from models import Place
from schemas.base import ListResponse


class PlaceUpdate(BaseModel):
    """
    Схема данных для обновления любимого места.
    """

    latitude: Optional[float] = None
    longitude: Optional[float] = None
    description: Optional[str] = Field(None, min_length=3, max_length=255)


class PlaceLocation(BaseModel):
    """
    Схема данных для текущей локации.
    """

    latitude: Optional[float] = None
    longitude: Optional[float] = None


class PlaceResponse(BaseModel):
    """
    Схема для представления данных о списке любимых мест.
    """

    data: Place


class PlacesListResponse(ListResponse):
    """
    Схема для представления данных о списке любимых мест.
    """

    data: list[Place]
