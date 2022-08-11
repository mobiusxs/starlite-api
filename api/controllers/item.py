from starlite import Controller
from starlite import delete
from starlite import get
from starlite import post
from starlite import put

from api.models.item import Item
from api.models.item import ItemModel


class ItemController(Controller):
    path = '/item'
    tags = ['Item']

    @get(path='/', include_in_schema=True, summary='List all Items')
    async def list(self) -> list[Item]:
        """List all Items"""

        return ItemModel.all()

    @post(path='/', include_in_schema=True, summary='Create a new Item')
    async def create(self, data: Item) -> Item:
        """Create a new Item"""

        item = data.to_model_instance()
        return item.save()

    @get(path='/{item_id:int}', include_in_schema=True, summary='Retrieve an Item')
    async def get(self, item_id: int) -> Item:
        """Retrieve an Item"""

        return ItemModel.find(item_id)

    @delete(path='/{item_id:int}', include_in_schema=True, summary='Delete an Item')
    async def delete(self, item_id: int) -> None:
        """Delete an Item"""

        item = ItemModel.find(item_id)
        if item:
            item.delete()

    @put(path='/{item_id:int}', include_in_schema=True, summary='Update an Item')
    async def update(self, item_id: int, data: Item) -> Item:
        """Update an Item"""

        item = ItemModel.find(item_id)
        if item:
            return item.update(**data.dict())
