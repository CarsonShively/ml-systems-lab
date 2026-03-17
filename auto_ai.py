from ml_systems_lab.config import API_BASE
import streamlit as st
from requests import post

def auto_ai():
    st.title("Auto AI")
    
    # upload file
    upload_file = st.file_uploader(
        "Upload file",
        accept_multiple_files=False
    )
    
    if upload_file and st.button("Upload file"):
        file = [
            ("upload_file", (upload_file.name, upload_file.getvalue(), upload_file.type))
        ]
        
        upload_file_response = post(
            f"{API_BASE}/upload_file",
            files=file
        )
    
    # upload folder
    upload_folder = st.file_uploader(
        "Upload folder",
        accept_multiple_files="directory"
    )

    if upload_folder and st.button("Upload folder"):
        files = []
        for file in upload_folder:
            files.append(("upload_folder", (file.name, file.getvalue(), file.type)))
            
        upload_folder_response = post(
            f"{API_BASE}/upload_folder",
            files=files
        )
        
auto_ai()