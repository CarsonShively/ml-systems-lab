from ml_systems_lab.config import STAGING
from fastapi import APIRouter, UploadFile, File

upload_folder_router = APIRouter()

@upload_folder_router.post("/upload_folder")
async def upload_folder(upload_folder: list[UploadFile] = File(...)):
    
    for file in upload_folder:
        path = STAGING / file.filename
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, "wb") as to_write:
            to_write.write(await file.read())
            