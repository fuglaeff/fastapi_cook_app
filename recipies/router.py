from datetime import timedelta
import databases

from fastapi import APIRouter

from recipies.crud import read_recipe_by_id

from recipies.schemas import RecipeMain

router = APIRouter()

database = databases.Database('sqlite:///fast_api_app.db')


@router.on_event("startup")
async def startup():
    await database.connect()


@router.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@router.get('/recipies/{id}', tags=['recipe'], response_model=RecipeMain)
async def take_recipe(id: int):
    return await read_recipe_by_id(id)
