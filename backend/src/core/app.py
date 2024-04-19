from backend.api_loader import *

def makeapp() -> FastAPI:
    """
    The function to launch FastApi application

    Returns:
        FastAPI: The launched FastAPI instance.
    """
    app = FastAPI(debug=True)

    app.add_middleware(
        CORSMiddleware, allow_credentials = True,
        allow_origins = [
            "http://localhost:4200"
        ],
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )

    return app

app = makeapp()
