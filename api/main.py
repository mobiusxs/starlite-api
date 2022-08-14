from starlite import Starlite
from starlite.plugins.sql_alchemy import SQLAlchemyPlugin

from .openapi import openapi_config
from .resources.item.views import ItemController

app = Starlite(
    openapi_config=openapi_config,
    plugins=[SQLAlchemyPlugin()],
    route_handlers=[
        ItemController
    ],
)
