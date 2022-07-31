from typing import List

import databases
from fastapi import APIRouter

from recipies.crud import create_recipe_db, read_recipe_by_id, read_recipies
from recipies.schemas import Recipe, RecipeDetail, RecipeMain

router = APIRouter()

database = databases.Database('sqlite:///fast_api_app.db')


@router.on_event("startup")
async def startup():
    await database.connect()


@router.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@router.get('/recipies', tags=['recipe'], response_model=List[RecipeMain])
async def show_recipies(page: int = 0, limit: int = 20):
    return await read_recipies(page, limit)


@router.post('/recipies', tags=['recipe'])
async def create_recipe(recipe: Recipe):
    data = recipe.dict()
    return await create_recipe_db(**data)


@router.get('/recipies/{id}', tags=['recipe'], response_model=RecipeDetail)
async def take_recipe(id: int):
    return await read_recipe_by_id(id)
