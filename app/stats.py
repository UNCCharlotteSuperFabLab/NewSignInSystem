from fastapi import APIRouter

router = APIRouter()


@router.get("/stats")
async def stats_page() -> dict:
    return {"message": "stats"}


@router.get("/users-per-day-chart/")
async def users_per_day_chart() -> dict:
    return {
        "labels": ["Mon", "Tue"],
        "values": [10, 12],
        "avg_lengths": [0.5, 0.75],
        "total_time": [5, 7],
        "avg_visits_per_user": [1.0, 1.2],
    }
