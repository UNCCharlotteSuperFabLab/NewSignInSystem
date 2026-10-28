from fastapi import APIRouter

router = APIRouter()


@router.get("/station/scan/")
async def station_scan() -> dict:
    return {"message": "station scan page"}


@router.post("/station/close/")
async def close_space() -> dict:
    return {"message": "space closed"}


@router.post("/station/set_forgot/")
async def set_forgot() -> dict:
    return {"message": "forgot signout recorded"}


@router.get("/station/new-user/{niner_id}/")
async def new_user_form(niner_id: int) -> dict:
    return {"message": "new user form", "niner_id": niner_id}
