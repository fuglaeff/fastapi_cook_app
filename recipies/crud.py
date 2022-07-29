import asyncio

import databases
from sqlalchemy import select, func

from recipies.models import IngredientSQL, RecipeSQL, StepSQL, recipe_ingredients

database = databases.Database('sqlite:///fast_api_app.db')


async def read_recipe_by_id(recipe_id: int):
    ingredients_query = select(
        IngredientSQL.name,
        recipe_ingredients.c.count,
        recipe_ingredients.c.unit
    ).select_from(IngredientSQL).join(recipe_ingredients).where(
        recipe_ingredients.c.recipe_id == recipe_id)
    recipe_query = select(RecipeSQL).where(RecipeSQL.id == recipe_id)
    steps_query = select(
        StepSQL.description, StepSQL.timing
    ).where(StepSQL.recipe_id == recipe_id)
    return await database.fetch_one(recipe_query)
