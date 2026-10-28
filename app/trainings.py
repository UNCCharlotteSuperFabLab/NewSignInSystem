from fastapi import APIRouter

router = APIRouter()


@router.get("/training/create/")
async def create_training() -> dict:
    return {"message": "training create route"}
