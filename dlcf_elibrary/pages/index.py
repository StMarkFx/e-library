import reflex as rx
from dlcf_elibrary.state import State
from dlcf_elibrary.components import BookCard


@rx.page("/")
def index():
    """Homepage of the e-library."""

    # Personalized greeting
    greeting = rx.heading(f"Hi, {State.user.display_name or 'Guest'}!", size="xl")

    # Recommendations (replace with actual logic to fetch recommendations)
    recommendations = rx.vstack(
        *[BookCard(resource) for resource in State.get_recommendations()], spacing="2em"
    )

    # Continue reading (replace with actual logic to fetch recent reads/downloads)
    continue_reading = rx.vstack(
        *[BookCard(resource) for resource in State.get_recent_reads()], spacing="2em"
    )

    return rx.center(
        rx.vstack(
            rx.heading(f"Hi, {State.user.display_name if State.user else 'Guest'}!", size="lg"),
            rx.heading("Recommendations", size="md"),
            rx.grid(
                children=[
                    State.get_recommendation_card(resource) for resource in State.get_recommendations()
                ],
                columns=[3, 3, 3],
                gap="1em",
            ),
            rx.heading("Recent Reads", size="md"),
            rx.grid(
                children=[
                    State.get_recent_reads_card(resource) for resource in State.get_recent_reads()
                ],
                columns=[3, 3, 3],
                gap="1em",
            ),
            rx.button("Contribute", on_click=lambda: rx.redirect("/upload_new")),
            spacing="2em",
        ),
        padding="4em",)