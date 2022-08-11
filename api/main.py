from starlite import Starlite
from starlite.plugins.sql_alchemy import SQLAlchemyPlugin

from .controllers import route_handlers
from .openapi import openapi_config

app = Starlite(route_handlers=route_handlers, openapi_config=openapi_config, plugins=[SQLAlchemyPlugin()])
