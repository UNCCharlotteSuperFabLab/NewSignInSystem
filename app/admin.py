from fastapi import APIRouter

router = APIRouter()


@router.get("/admin/")
async def admin_page() -> dict:
    return {"message": "admin"}


@router.get("/accounts/login/")
async def login_page() -> dict:
    return {"message": "login"}
