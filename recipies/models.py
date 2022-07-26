from datetime import timedelta
from enum import IntEnum
from typing import Optional, List

from pydantic import BaseModel, Field


class Rating(IntEnum):
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5


class Ingredient(BaseModel):
    pass


class CookingStep(BaseModel):
    name: str
    description: str
    timing: timedelta


class RecipeMain(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    cooking_time: timedelta = Field(title='Cooking time')
    cooking_level: Rating = Field(
        default=Rating.three, title='Recipe complexity', description='Choose the complexity of the recipe')
    ingredients: List[Ingredient]
    steps: Optional[List[CookingStep]] = Field(default=None, title='Steps of cooking')

