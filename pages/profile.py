import reflex as rx
from reflex.state import State


# Profile State
class ProfileState(State):
    user_name: str = "John Doe"  # Default user name
    reading_history: list = []  # List of books read/downloaded
    favorites: list = []  # List of favorite books
    contributions: list = []  # List of contributed books

    @staticmethod
    def fetch_profile_data():
        """Simulate fetching user profile data from a database."""
        ProfileState.reading_history = [
            {"title": "Book A", "author": "Author 1"},
            {"title": "Book B", "author": "Author 2"},
        ]
        ProfileState.favorites = [
            {"title": "Book C", "author": "Author 3"},
            {"title": "Book D", "author": "Author 4"},
        ]
        ProfileState.contributions = [
            {"title": "Book E", "author": "Author 5"},
            {"title": "Book F", "author": "Author 6"},
        ]

    @staticmethod
    def remove_favorite(book_title):
        """Remove a book from favorites."""
        ProfileState.favorites = [
            book for book in ProfileState.favorites if book["title"] != book_title
        ]
        print(f"Removed {book_title} from favorites.")

    @staticmethod
    def delete_contribution(book_title):
        """Delete a contributed book."""
        ProfileState.contributions = [
            book for book in ProfileState.contributions if book["title"] != book_title
        ]
        print(f"Deleted {book_title} from contributions.")


# Reusable Book List
def book_list(title, books, button_action=None, button_label=None):
    """Reusable component to display a list of books."""
    return rx.box(
        rx.vstack(
            rx.text(title, font_size="xl", font_weight="bold"),
            *[
                rx.hstack(
                    rx.text(f"{book['title']} by {book['author']}"),
                    rx.button(
                        button_label,
                        on_click=lambda: button_action(book["title"])
                        if button_action
                        else None,
                        bg="red",
                        color="white",
                        size="sm",
                    )
                    if button_action
                    else rx.spacer(),
                    justify="space-between",
                )
                for book in books
            ],
            spacing="1rem",
        ),
        padding="1rem",
        box_shadow="sm",
        border_radius="md",
        bg="white",
        width="100%",
    )


# Profile Page
def profile_page():
    # Fetch profile data
    ProfileState.fetch_profile_data()

    return rx.box(
        rx.vstack(
            rx.text(
                f"Welcome, {ProfileState.user_name}!",
                font_size="2xl",
                font_weight="bold",
            ),
            rx.text("Here's a summary of your activity:", font_size="md"),
            rx.divider(),
            book_list("Reading/Download History", ProfileState.reading_history),
            book_list("Favorites", ProfileState.favorites, ProfileState.remove_favorite, "Remove"),
            book_list(
                "Contributions", ProfileState.contributions, ProfileState.delete_contribution, "Delete"
            ),
            spacing="2rem",
        ),
        padding="2rem",
        width="100%",
        max_width="800px",
        margin="auto",
        bg="gray.50",
    )
