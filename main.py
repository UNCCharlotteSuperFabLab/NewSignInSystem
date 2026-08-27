from fastapi import fastapi, APIRouter
from .app import admin, profile, station, stats, trainings, visits

#Should be where the root file is called and should point to all required pages
app = FastAPI()
print("does this work")
