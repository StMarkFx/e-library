# Reflex app entry point

import os
from reflex import Reflex, State

# File storage directory (ensure this exists on the server)
UPLOAD_DIR = "uploads"

class BookUploadState(State):
    message = ""

    def upload_book(self, data):
        # Extract details from the form
        title = data["title"]
        author = data["author"]
        faculty = data["faculty"]
        department = data["department"]
        description = data["description"]
        file = data["file"]  # File object from the user

        # Ensure upload directory exists
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        # Save the uploaded file
        file_path = os.path.join(UPLOAD_DIR, file["filename"])
        with open(file_path, "wb") as f:
            f.write(file["content"])

        # Generate a download URL (adjust for production)
        download_url = f"/{UPLOAD_DIR}/{file['filename']}"

        # Save book details to the database (pseudo-code)
        save_to_database(
            title=title,
            author=author,
            faculty=faculty,
            department=department,
            description=description,
            download_url=download_url,
        )

        # Update state message
        self.message = "Book uploaded successfully!"

# Pseudo-function to save to the database
def save_to_database(**kwargs):
    print("Saved book to database:", kwargs)

app = Reflex(state=BookUploadState)
