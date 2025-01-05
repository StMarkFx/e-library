from reflex import pc
from reflex.state import State


# Upload State
class UploadState(State):
    book_title: str = ""
    book_author: str = ""
    book_faculty: str = ""
    book_department: str = ""
    book_file: str = ""  # Will store the file path or name after upload
    upload_status: str = ""  # To show upload success or failure messages

    @staticmethod
    def upload_book():
        """Handle the book upload process."""
        if (
            UploadState.book_title
            and UploadState.book_author
            and UploadState.book_faculty
            and UploadState.book_department
            and UploadState.book_file
        ):
            # Simulate a successful upload (would be replaced by actual upload logic)
            print("Uploading book:", UploadState.book_title)
            UploadState.upload_status = "Book uploaded successfully!"
            # Reset form fields
            UploadState.book_title = ""
            UploadState.book_author = ""
            UploadState.book_faculty = ""
            UploadState.book_department = ""
            UploadState.book_file = ""
        else:
            UploadState.upload_status = "Please fill in all the fields."

    @staticmethod
    def handle_file_upload(file):
        """Simulate handling file upload."""
        # In production, this would save the file to a server or cloud storage.
        UploadState.book_file = file["name"]
        print("Uploaded file:", UploadState.book_file)


# Upload Form
def upload_form():
    return pc.vstack(
        pc.text("Upload a Book", font_size="2xl", font_weight="bold", margin_bottom="1rem"),
        pc.form(
            pc.vstack(
                pc.input(
                    placeholder="Book Title",
                    value=UploadState.book_title,
                    on_change=lambda title: setattr(UploadState, "book_title", title),
                ),
                pc.input(
                    placeholder="Author Name",
                    value=UploadState.book_author,
                    on_change=lambda author: setattr(UploadState, "book_author", author),
                ),
                pc.select(
                    options=["Science", "Arts", "Engineering", "Medicine"],
                    placeholder="Select Faculty",
                    value=UploadState.book_faculty,
                    on_change=lambda faculty: setattr(UploadState, "book_faculty", faculty),
                ),
                pc.select(
                    options=["Computer Science", "Civil Engineering", "English Literature", "Pharmacology"],
                    placeholder="Select Department",
                    value=UploadState.book_department,
                    on_change=lambda dept: setattr(UploadState, "book_department", dept),
                ),
                pc.file_upload(
                    on_upload=UploadState.handle_file_upload,
                    accept=".pdf,.docx,.epub",
                    multiple=False,
                ),
                pc.button(
                    "Upload Book",
                    on_click=UploadState.upload_book,
                    bg="blue.500",
                    color="white",
                    width="100%",
                ),
                pc.cond(
                    UploadState.upload_status,
                    pc.text(
                        UploadState.upload_status,
                        color="green.500" if "successfully" in UploadState.upload_status else "red.500",
                        font_size="sm",
                    ),
                ),
            ),
            spacing="1rem",
            padding="2rem",
            bg="gray.50",
            border_radius="md",
            box_shadow="lg",
        ),
        width="100%",
        max_width="600px",
        margin="auto",
    )


# Upload Page
def upload_page():
    return pc.box(
        upload_form(),
        padding="2rem",
        bg="gray.100",
        min_height="100vh",
    )
