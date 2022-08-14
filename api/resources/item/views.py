from starlite import Controller, delete, get, post, put

from . import models
from . import schemas


class ItemController(Controller):
    path = '/item'
    tags = ['Item']

    @get(path='/', summary='List all Items')
    async def list_all(self) -> list[schemas.Item]:
        """List all Items"""
        return models.Item.all()

    @post(path='/', summary='Create a new Item')
    async def create(self, data: schemas.Item) -> schemas.Item:
        """Create a new Item"""
        item = models.Item(**data.dict())
        return item.save()

    @get(path='/{item_id:int}', summary='Retrieve an Item')
    async def read(self, item_id: int) -> schemas.Item:
        """Retrieve an Item"""
        return models.Item.find(item_id)

    @put(path='/{item_id:int}', summary='Update an Item')
    async def update(self, item_id: int, data: schemas.Item) -> schemas.Item:
        """Update an Item"""
        item = models.Item.find(item_id)
        if item:
            return item.update(**data.dict())

    @delete(path='/{item_id:int}', summary='Delete an Item')
    async def delete(self, item_id: int) -> None:
        """Delete an Item"""
        item = models.Item.find(item_id)
        if item:
            item.delete()
