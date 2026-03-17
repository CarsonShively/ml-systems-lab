from fastapi import FastAPI
from ml_systems_lab.routes.upload_file import upload_file_router
from ml_systems_lab.routes.upload_folder import upload_folder_router

api = FastAPI()

api.include_router(upload_file_router)
api.include_router(upload_folder_router)