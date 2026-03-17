from ml_systems_lab.config import STAGING
from fastapi import APIRouter, UploadFile, File

upload_file_router = APIRouter()

@upload_file_router.post("/upload_file")
async def upload_file(upload_file: UploadFile = File(...)):
    path = STAGING / upload_file.filename
    
    path.parent.mkdir(parents=True)
    
    with open(path, "wb") as file:
        file.write(await upload_file.read())