from enum import StrEnum
from typing import List, Optional

from pydantic import AnyHttpUrl, BaseModel


class UnitsEnum(StrEnum):
    GRAMS = "g"
    KILOGRAMS = "kg"
    MILLILITRES = "ml"


class Ingredient(BaseModel):
    name: str
    quantity: float
    units: UnitsEnum


class RecipeURL(BaseModel):
    url: AnyHttpUrl


class Recipe(BaseModel):
    name: str
    origin_url: Optional[RecipeURL]
    ingredients: List[Ingredient]
    steps: List[str]
