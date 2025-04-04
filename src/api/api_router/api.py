import falcon
import falcon.asgi

from src.api.endpoints import hello  # Import your endpoint resources
from src.api.middleware import auth  # Import your middleware (if any)

api_router = falcon.asgi.App(
    middleware=[
        # Add global middleware here (e.g., authentication)
        # auth.AuthMiddleware()
    ]
)

# Create instances of your resource classes
hello_resource = hello.HelloResource()

# Add routes to the router
api_router.add_route("/hello/{user_id}", hello_resource)  # Corrected line
