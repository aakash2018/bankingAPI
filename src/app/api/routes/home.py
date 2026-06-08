from fastapi import APIRouter
from src.app.core.logging import get_logger

logger = get_logger("home")

router = APIRouter(prefix="/home", tags=["home"])


@router.get("/")
def read_home():
    logger.info("Reading home page")
    logger.debug("Reading home page")
    logger.error("Reading home page")
    logger.warning("Reading home page")
    logger.critical("Reading home page")
    return {"message": "Welcome to FenTech Bank API!"}

