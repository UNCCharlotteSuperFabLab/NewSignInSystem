from fastapi import FastAPI

from app import admin, profile, station, stats, trainings, visits

app = FastAPI(title="Super Fab Lab Sign-In System")

app.include_router(admin.router)
app.include_router(profile.router)
app.include_router(station.router)
app.include_router(stats.router)
app.include_router(trainings.router)
app.include_router(visits.router)


@app.get("/")
async def root() -> dict:
    return {"message": "Super Fab Lab Sign-In System"}
