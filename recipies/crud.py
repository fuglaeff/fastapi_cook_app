import databases
from sqlalchemy import and_, func, insert, select

from recipies.models import (IngredientSQL, RecipeSQL, StepSQL,
                             recipe_ingredients)

database = databases.Database('sqlite:///fast_api_app.db')


async def read_recipe_by_id(recipe_id: int):
    ingredients_query = select(
        IngredientSQL.name,
        recipe_ingredients.c.count,
        recipe_ingredients.c.unit
    ).select_from(IngredientSQL).join(recipe_ingredients).where(
        recipe_ingredients.c.recipe_id == recipe_id)
    recipe_query = select(RecipeSQL, func.a(StepSQL.description)).where(and_(RecipeSQL.id == 1, RecipeSQL.steps)).group_by(RecipeSQL)
    steps_query = select(
        StepSQL.description, StepSQL.timing
    ).where(StepSQL.recipe_id == recipe_id)

    recipe = await database.fetch_one(recipe_query)
    steps = await database.fetch_all(steps_query)
    ingredients = await database.fetch_all(ingredients_query)
    steps_list = []
    for row in steps:
        steps_list.append(row._asdict())
    ingredients_list = []
    for row in ingredients:
        ingredients_list.append(row._asdict())
    return {**recipe._asdict(), 'steps': steps_list, 'ingredients': ingredients_list,}


async def create_recipe_db(**kwargs):
    insert_recipe = insert(RecipeSQL).values(**kwargs)
    return await database.execute(insert_recipe)


async def read_recipies(page: int, limit: int = 20):
    query = select(RecipeSQL).offset(page * limit).limit(limit)
    return await database.fetch_all(query)
