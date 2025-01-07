import reflex as rx
from dlcf_elibrary.state import State
from dlcf_elibrary.components import BookCard  # Assuming you have this component


@rx.page(route="/my_collections")
def my_collections():
    """Page to display the user's saved resources."""

    # Fetch user's saved resources (replace with your actual logic)
    user_resources = State.get_user_resources()  # Function to fetch from DB

    return rx.center(
        rx.vstack(
            rx.heading("My Collections", size="lg"),
            rx.search_bar(placeholder="Search your collection...", on_change=State.set_search_query),
            rx.grid(
                children=[
                    State.get_collection_card(resource) for resource in State.get_user_resources()
                ],
                columns=[3, 3, 3],
                gap="1em",
            ),
            spacing="2em",
        ),
        padding="4em",
    )
