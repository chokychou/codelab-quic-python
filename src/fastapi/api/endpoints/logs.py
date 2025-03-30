from fastapi import APIRouter
from src.fastapi.schemas import logs

router = APIRouter()


@router.get("/", tags=["logs"], response_model=logs.LogsResponse)
async def root():
    return {"message": "logs root endpoint"}
