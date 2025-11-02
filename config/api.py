from ninja import NinjaAPI, Schema

from scalar_django_ninja import ScalarViewer


api = NinjaAPI(
    title="Pages API",
    version="1.0.0",
    docs=ScalarViewer(title="Pages API Reference"),
)


class HelloResponse(Schema):
    message: str


@api.get("/hello", response=HelloResponse)
def hello(request):
    """Demo endpoint showing Django Ninja integration."""
    return HelloResponse(message="Hello from Django Ninja!")
