from sqlalchemy import Column
from sqlalchemy import String
from starlite import DTOFactory
from starlite.plugins.sql_alchemy import SQLAlchemyPlugin

from api.database import Base

dto_factory = DTOFactory(plugins=[SQLAlchemyPlugin()])


class ItemModel(Base):
    __tablename__ = 'item'

    name = Column(String)


Item = dto_factory("Item", ItemModel, exclude=['id', 'modified'])
