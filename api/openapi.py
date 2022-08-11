from starlite import OpenAPIController
from starlite import OpenAPIConfig


class OpenAPIRootController(OpenAPIController):
    path = '/'


openapi_config = OpenAPIConfig(
    openapi_controller=OpenAPIRootController,
    create_examples=False,
    use_handler_docstrings=True,
    title='API Title',
    version='0.0.1',
    contact=dict(name='Contact Name', url='http://www.contact_url.com', email='contact@email.com'),
    description='API Description',
    license=dict(name='MIT', identifier='MIT', url='https://opensource.org/licenses/MIT'),
    summary='API Summary',
    servers=[{'url': '/'}]
)
