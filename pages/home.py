# Combines Home, Search, Profile, and Upload

import reflex as pc

def UploadPage():
    return pc.center(
        pc.form(
            pc.vstack(
                pc.input(placeholder="Book Title", required=True, id="title"),
                pc.input(placeholder="Author Name", required=True, id="author"),
                pc.select(
                    ["Engineering", "Science", "Arts"],
                    placeholder="Select Faculty",
                    required=True,
                    id="faculty",
                ),
                pc.select(
                    ["Computer Science", "Mathematics", "History"],
                    placeholder="Select Department",
                    required=True,
                    id="department",
                ),
                pc.textarea(placeholder="Book Description", required=True, id="description"),
                pc.file_input(accept="application/pdf", required=True, id="file"),
                pc.button("Upload", type="submit"),
            ),
            on_submit=handle_upload,
        )
    )

def handle_upload(data):
    # Send the form data to the backend
    print("Uploading book:", data)
    pc.call_api("upload_book", data=data)
