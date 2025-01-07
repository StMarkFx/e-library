import reflex as rx
from dlcf_elibrary.models import Resource, UserResource
from dlcf_elibrary.state import State  # Assuming you have a State class


def BookCard(resource: Resource) -> rx.Component:
    """Displays a single resource (book) card."""

    # Fetch uploader's display name
    uploader = State.get_user_by_id(resource.uploader_id)
    uploader_name = uploader.display_name if uploader else "Unknown User"

    # Function to add resource to user's collection
    @rx.event(prevent_default=True)
    def add_to_collection():
        if State.user:
            with rx.session() as session:
                user_resource = UserResource(user_id=State.user.id, resource_id=resource.id)
                session.add(user_resource)
                session.commit()
            # Add feedback to the user (e.g., success message)

    return rx.card(
        rx.image(src=resource.file_url, width="100%", alt=resource.title),
        rx.vstack(
            rx.heading(resource.title, size="md"),
            rx.text(f"By: {resource.author}"),
            rx.text(f"Faculty: {resource.faculty}"),
            rx.text(f"Uploaded by: {uploader_name}"),  # Display uploader's name
            rx.hstack(
                rx.button("Read", on_click=lambda: rx.window_open(resource.file_url)), # Placeholder for PDF viewer
                rx.button("Download", on_click=lambda: rx.window_open(resource.file_url)), # Placeholder for download
                rx.button("Add to Collection", on_click=add_to_collection),
                rx.icon(type="thumbs-up"),  # Placeholder for thumbs up
                rx.icon(type="comment"),  # Placeholder for comments
                spacing="1em",
            ),
            rx.divider(),
            rx.text("Comments:"),  # Placeholder for comments section
            spacing="1em",
        ),
        padding="2em",
        border_radius="md",
        shadow="md",
    )
