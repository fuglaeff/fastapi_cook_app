from sqlalchemy import (Column, Enum, Float, ForeignKey, Integer, Interval,
                        String, Table)
from sqlalchemy.orm import relationship

from schemas import Rating

from ..db import Base, engine

recipe_ingredients = Table(
    'recipe_ingredients',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('recipe_id', Integer, ForeignKey('recipies.id')),
    Column('ingredient_id', Integer, ForeignKey('ingredients.id')),
    Column('count', Float),
    Column('unit', String(25))
)


class RecipeSQL(Base):
    __tablename__ = 'recipies'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(300))
    cooking_time = Column(Interval)
    prepariring_time = Column(Interval)
    recipe_level = Column(Enum(Rating))
    steps = relationship('StepSQL')
    ingredients = relationship('IngredientSQL', secondary=recipe_ingredients)


class StepSQL(Base):
    __tablename__ = 'steps'

    id = Column(Integer, primary_key=True)
    description = Column(String(300))
    timing = Column(Interval)
    recipe_id = Column(Integer, ForeignKey('recipies.id'))


class IngredientSQL(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))


Base.metadata.create_all(engine)
