from datetime import timedelta

from fastapi import APIRouter

from .schemas import RecipeMain

router = APIRouter()

fake_recipies = {
    1: {
        'id': 1,
        'name': 'Sandwich',
        'description': 'Fast and tasty breakfast',
        'cooking_time': timedelta(minutes=5),
        'ingredients': [
            {
                'name': 'Bread'
            },
            {
                'name': 'Cheese'
            },
            {
                'name': 'Ham'
            },
            {
                'name': 'Cucumber'
            },
            {
                'name': 'Tomato'
            },
        ],
        'steps': None,
        },
}


@router.get('/recipies/{id}', tags=['recipe'], response_model=RecipeMain)
def take_recipe(id: int):
    return fake_recipies[id]
