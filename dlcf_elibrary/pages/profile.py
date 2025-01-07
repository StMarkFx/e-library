import reflex as rx
from dlcf_elibrary.state import State


@rx.page(route="/profile")
def profile():
    """User profile page."""

    return rx.vstack(
        rx.heading(f"Profile: {State.user.display_name}", size="xl"),
        rx.vstack(
            rx.avatar(src=State.user.avatar_url, size="lg"),
            rx.text(f"Display Name: {State.user.display_name}"),
            rx.text(f"Email: {State.user.email}"),
            rx.text(f"Faculty: {State.user.faculty}"),
            rx.text(f"Department: {State.user.department}"),
            rx.text(f"Level: {State.user.level}"),
            rx.button("Edit Profile", on_click=lambda: rx.redirect("/profile_setup")),  # Placeholder route
            rx.button("View Contributions", on_click=lambda: rx.redirect("/my_uploads")),  # Placeholder route
            spacing="1em",
        ),
        padding="2em",
    )
