import os
import uuid
import mimetypes
from datetime import datetime
from reflex import pc

# Constants
UPLOAD_DIR = "uploads"
ALLOWED_FILE_TYPES = ["application/pdf", "application/epub", "application/mobi"]  # Add other file types as needed

# Ensure the upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

def generate_unique_filename(filename):
    """Generate a unique filename using UUID to avoid name conflicts."""
    file_extension = os.path.splitext(filename)[1]
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    return unique_filename

def validate_file_type(file):
    """Validate the uploaded file type."""
    mime_type, _ = mimetypes.guess_type(file["filename"])
    if mime_type not in ALLOWED_FILE_TYPES:
        raise ValueError("Unsupported file type. Please upload a PDF, EPUB, or MOBI file.")
    return mime_type

def save_uploaded_file(file):
    """Save the uploaded file to the server."""
    unique_filename = generate_unique_filename(file["filename"])
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    with open(file_path, "wb") as f:
        f.write(file["content"])

    return unique_filename

def generate_download_url(filename):
    """Generate a download URL for the uploaded file."""
    return f"/{UPLOAD_DIR}/{filename}"

def save_book_to_db(title, author, faculty, department, description, download_url):
    """Save the book's metadata to the database (stub function for illustration)."""
    # Replace with actual database logic
    print(f"Saving book: {title}, {author}, {faculty}, {department}, {description}, {download_url}")

def format_datetime(dt):
    """Format datetime objects into a human-readable string."""
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def create_message_component(message, message_type="info"):
    """Create a message component for UI notifications."""
    if message_type == "error":
        color = "red"
    elif message_type == "success":
        color = "green"
    else:
        color = "blue"

    return pc.alert(message, status=color)
