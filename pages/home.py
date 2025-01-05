# Combines Home, Search, Profile, and Upload

import reflex as rx

def UploadPage():
    return rx.center(
        rx.form(
            rx.vstack(
                rx.input(placeholder="Book Title", required=True, id="title"),
                rx.input(placeholder="Author Name", required=True, id="author"),
                rx.select(
                    ["Engineering", "Science", "Arts"],
                    placeholder="Select Faculty",
                    required=True,
                    id="faculty",
                ),
                rx.select(
                    ["Computer Science", "Mathematics", "History"],
                    placeholder="Select Department",
                    required=True,
                    id="department",
                ),
                rx.textarea(placeholder="Book Description", required=True, id="description"),
                rx.file_input(accept="application/pdf", required=True, id="file"),
                rx.button("Upload", type="submit"),
            ),
            on_submit=handle_upload,
        )
    )

def handle_upload(data):
    # Send the form data to the backend
    print("Uploading book:", data)
    rx.call_api("upload_book", data=data)
