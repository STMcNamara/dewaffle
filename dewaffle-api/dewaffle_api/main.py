import uvicorn
from fastapi import FastAPI

from dewaffle_api.schema import Recipe, RecipeURL, Ingredient, UnitsEnum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello world - welcome to Dewaffle"}


@app.post("/recipe-from-url")
async def from_url(
        url: RecipeURL
) -> Recipe:
    place_holder_recipe: Recipe = Recipe(
        name='placeholder_name',
        origin_url=url,
        ingredients=[Ingredient(
            name="Flour",
            quantity="2",
            units=UnitsEnum.GRAMS
        )],
        steps=["1. Start", "N. Finish"]
    )
    return place_holder_recipe


def start():
    """Launch from root folder"""
    uvicorn.run("dewaffle_api.main:app")
