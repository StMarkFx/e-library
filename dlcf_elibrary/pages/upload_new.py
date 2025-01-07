import reflex as rx
from dlcf_elibrary.state import State
from dlcf_elibrary.components import UploadForm


@rx.page(route="/upload_new")
def upload_new() -> rx.Component:
    """Renders the upload new resource page."""
    if not State.user:
        return rx.redirect("/login")  # Redirect if not logged in

    return rx.center(
        rx.vstack(
            rx.heading("Upload New Resource", size="lg"),
            UploadForm(),  # Use the UploadForm component
            spacing="2em",
        ),
        padding="4em",)