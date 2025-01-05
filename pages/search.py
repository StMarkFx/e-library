from reflex import pc
from reflex.state import State


# Search State
class SearchState(State):
    query: str = ""  # The search query
    search_results: list = []  # List of search results (books)

    @staticmethod
    def perform_search():
        """Simulate a search operation."""
        print(f"Performing search for: {SearchState.query}")
        # Simulate results based on query
        sample_books = [
            {"title": "Introduction to Python", "author": "Guido van Rossum"},
            {"title": "Advanced Data Science", "author": "John Smith"},
            {"title": "Machine Learning Basics", "author": "Andrew Ng"},
        ]
        # Filter books containing the query (case insensitive)
        SearchState.search_results = [
            book
            for book in sample_books
            if SearchState.query.lower() in book["title"].lower()
        ]

    @staticmethod
    def clear_search():
        """Clear search query and results."""
        SearchState.query = ""
        SearchState.search_results = []
        print("Search cleared.")


# Reusable Book Card
def book_card(book):
    """Reusable component for displaying a single book."""
    return pc.box(
        pc.vstack(
            pc.text(book["title"], font_weight="bold", font_size="lg"),
            pc.text(f"Author: {book['author']}", font_size="sm", color="gray.600"),
            pc.button("View Details", bg="blue.500", color="white", size="sm"),
        ),
        padding="1rem",
        box_shadow="sm",
        border_radius="md",
        bg="white",
        width="100%",
    )


# Search Page
def search_page():
    return pc.box(
        pc.vstack(
            pc.box(
                pc.hstack(
                    pc.input(
                        value=SearchState.query,
                        placeholder="Search for books...",
                        on_change=lambda query: setattr(SearchState, "query", query),
                        width="70%",
                    ),
                    pc.button(
                        "Search",
                        on_click=SearchState.perform_search,
                        bg="blue.500",
                        color="white",
                    ),
                    pc.button(
                        "Clear",
                        on_click=SearchState.clear_search,
                        bg="red.500",
                        color="white",
                    ),
                    justify="center",
                ),
                padding="1rem",
                bg="gray.50",
                width="100%",
                box_shadow="md",
            ),
            pc.divider(),
            pc.cond(
                SearchState.search_results,
                pc.grid(
                    *[
                        book_card(book)
                        for book in SearchState.search_results
                    ],
                    template_columns="repeat(auto-fit, minmax(200px, 1fr))",
                    gap="1rem",
                ),
                pc.text(
                    "No results found. Try searching for something else!",
                    font_size="lg",
                    color="gray.600",
                ),
            ),
            spacing="2rem",
        ),
        padding="2rem",
        max_width="800px",
        margin="auto",
    )
