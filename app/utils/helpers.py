import os

def save_uploaded_file(upload_file, destination: str):
    os.makedirs(os.path.dirname(destination), exist_ok=True)

    with open(destination, "wb") as buffer:
        buffer.write(upload_file.file.read())
