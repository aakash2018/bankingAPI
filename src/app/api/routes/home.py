from fastapi import APIRouter


router = APIRouter(prefix="/home", tags=["home"])

@router.get("/")
def read_home():
    return {"message": "Welcome to FenTech Bank API!"}

