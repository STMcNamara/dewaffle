import pytest

from app.api.v0.endpoints.recipies import from_url
from app.schema import RecipeURL

pytest_plugins = "pytest_asyncio"


@pytest.mark.asyncio
async def test_from_url_valid_response():
    """
    This is a trivial example test, illustrates
    a test that calls an asynchronous method.
    """
    # arrange
    good_url = RecipeURL(url="https://www.abc.co.uk")

    # act
    response = await from_url(good_url)

    # assert
    assert response.name is not None
