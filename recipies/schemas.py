from datetime import timedelta
from enum import IntEnum
from typing import List, Optional

from pydantic import BaseModel, Field


class Rating(IntEnum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5


class Ingredient(BaseModel):
    name: str
    count: float
    unit: str


class CookingStep(BaseModel):
    name: str
    description: str
    timing: timedelta


class RecipeMain(BaseModel):
    id: int
    name: str = Field(
        title='Recipe name',
        description='Give name for your recipe',
        max_length=50
    )
    description: Optional[str] = Field(
        default=None,
        title='Description of your recipe',
        description='Write mini text about your recipe',
        max_length=300
    )
    cooking_time: timedelta = Field(title='Cooking time')
    prepariring_time: timedelta = Field(title='Prepare time for cook')
    cooking_level: Rating = Field(
        default=Rating.three,
        title='Recipe complexity',
        description='Choose the complexity of the recipe'
    )
    ingredients: List[Ingredient]
    steps: Optional[List[CookingStep]] = Field(
        default=None, title='Steps of cooking')
