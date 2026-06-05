import uvicorn
from fastapi import FastAPI
# from .api.main import api_router
# from .core.config import settings
from api.main import api_router   
from core.config import settings 

app = FastAPI(
    title=settings.PROJECT_NAME or "Banking API",
    description=settings.PROJECT_DESCRIPTION or "Banking FastAPI Project",
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)