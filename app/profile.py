from fastapi import APIRouter

router = APIRouter()


@router.get("/me/profile")
async def profile_page() -> dict:
    return {"message": "profile", "user": "current_user"}


@router.get("/staff/user_list")
async def staff_user_list() -> dict:
    return {"message": "user list", "users": []}
