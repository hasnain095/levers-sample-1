from fastapi import APIRouter

from app.api.api_v1.endpoints import bills

api_router = APIRouter()
api_router.include_router(bills.router, prefix="/bills", tags=["bills"])
