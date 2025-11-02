from django.conf import settings
from ninja import NinjaAPI, Schema

from scalar_django_ninja import ScalarViewer


API_SERVER_URL = getattr(settings, "API_SERVER_URL", ".")

servers = (
    [{"url": ".", "description": "Resolve against the current host"}]
    if API_SERVER_URL == "."
    else [{"url": API_SERVER_URL}]
)


api = NinjaAPI(
    title="Pages API",
    version="1.0.0",
    docs=ScalarViewer(title="Pages API Reference"),
    servers=servers,
)


class HelloResponse(Schema):
    message: str


@api.get("/hello", response=HelloResponse)
def hello(request):
    """Demo endpoint showing Django Ninja integration."""
    return HelloResponse(message="Hello from Django Ninja!")
