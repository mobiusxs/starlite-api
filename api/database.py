from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy_mixins import AllFeaturesMixin

from api.settings import settings

engine = create_engine(settings.database_url, echo=False)
session = scoped_session(sessionmaker(bind=engine, autocommit=True))
metadata = MetaData()


class BaseModel(AllFeaturesMixin):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, autoincrement=True)
    modified = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


BaseModel.set_session(session)
Base = declarative_base(metadata=metadata, cls=BaseModel)
