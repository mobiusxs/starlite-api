from sqlalchemy import Column, String

from api.database import Base


class Item(Base):
    name = Column(String)
