"""
Описание моделей данных (DTO).
"""
from typing import Optional

from pydantic import BaseModel, Field


class LocalityDTO(BaseModel):
    """
    Модель для представления данных о местонахождении.

    .. code-block::

        LocalityDTO(
            city="Mariehamn",
            alpha2code="AX",
            locality="Mariehamn sub-region",
        )
    """

    city: Optional[str] = Field(
        None, title="Название города", min_length=2, max_length=50
    )
    alpha2code: Optional[str] = Field(
        None, title="ISO Alpha2-код страны", min_length=2, max_length=2
    )
    locality: Optional[str] = Field(
        None, title="Местонахождение", min_length=2, max_length=255
    )


class LocationDTO(BaseModel):
    """
    Модель для представления данных о локации.

    .. code-block::

        LocationDTO(
            latitude=58.0,
            longitude=56.22,
        )
    """

    latitude: Optional[float] = Field(None, title="Широта")
    longitude: Optional[float] = Field(None, title="Долгота")
