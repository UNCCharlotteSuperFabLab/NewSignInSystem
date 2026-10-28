from fastapi import APIRouter

router = APIRouter()


@router.get("/users/")
async def users_index() -> dict:
    return {"message": "users index"}


@router.post("/users/{user_id}/update_canvas_id")
async def update_canvas_id(user_id: int) -> dict:
    return {"message": "canvas id update queued", "user_id": user_id}
