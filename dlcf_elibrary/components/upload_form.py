import reflex as rx
from dlcf_elibrary.models import Resource
from dlcf_elibrary.state import State  # Assuming you have a State class


def UploadForm() -> rx.Component:
    """A form for uploading new resources."""

    @rx.event(prevent_default=True)
    def handle_submit(
        title: str,
        author: str,
        description: str,
        faculty: str,
        department: str,
        level: str,
        file: rx.UploadFile,
    ):
        """Handles form submission."""
        if not file:
            # Handle file upload error
            return

        try:
            file_url = upload_file_to_cloud_storage(file)  # Your cloud storage upload function
            with rx.session() as session:
                new_resource = Resource(
                    title=title,
                    author=author,
                    description=description,
                    faculty=faculty,
                    department=department,
                    level=level,
                    file_url=file_url,
                    uploader_id=State.user.id,  # Get ID from logged-in user
                )
                session.add(new_resource)
                session.commit()
            # Add success feedback to the user
        except Exception as e:
            # Handle exceptions during upload and database insertion
            print(f"Error uploading file: {e}")
            # Add error feedback to the user


    return rx.form(
        rx.vstack(
            rx.text_input(
                placeholder="Title",
                name="title",
                type="text",
                required=True,
            ),
            rx.text_input(
                placeholder="Author",
                name="author",
                type="text",
                required=True,
            ),
            rx.text_area(
                placeholder="Description",
                name="description",
                required=True,
            ),
            rx.select(
                name="faculty",
                options=State.faculties,  # Assuming State.faculties is populated
                placeholder="Faculty",
                required=True,
            ),
            rx.select(
                name="department",
                options=["Department 1", "Department 2"],  # Placeholder options
                placeholder="Department",
                required=True,
            ),
            rx.select(
                name="level",
                options=["Level 1", "Level 2"],  # Placeholder options
                placeholder="Level",
                required=True,
            ),
            rx.file_upload(name="file", required=True),
            rx.button("Upload", type="submit", on_click=handle_submit),
            spacing="1em",
        ),
        on_submit=handle_submit,  # This is also needed for form submission
    )


def upload_file_to_cloud_storage(file: rx.UploadFile) -> str:
    """Uploads a file to cloud storage and returns the URL.  REPLACE THIS."""
    # Replace this with your actual cloud storage upload logic (e.g., using AWS S3, Google Cloud Storage)
    # This is a placeholder; you'll need to implement the actual upload logic here.
    # Example using a mock URL:
    return f"https://example.com/uploads/{file.filename}"
