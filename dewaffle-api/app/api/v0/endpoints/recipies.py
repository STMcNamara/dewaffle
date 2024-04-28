from app.schema import RecipeURL, Recipe, Ingredient, UnitsEnum
from fastapi import APIRouter

router = APIRouter()


@router.post("/get-from-url")
async def from_url(url: RecipeURL) -> Recipe:
    place_holder_recipe: Recipe = Recipe(
        name="placeholder_name",
        origin_url=url,
        ingredients=[
            Ingredient(name="Flour", quantity="2", units=UnitsEnum.GRAMS)
        ],
        steps=["1. Start", "N. Finish"],
    )
    return place_holder_recipe
