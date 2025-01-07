import reflex as rx
from dlcf_elibrary.state import State
from dlcf_elibrary.components import BookCard  # Assuming you have this component


@rx.page(route="/explore")
def explore():
    """Explore page for browsing resources."""

    # Search functionality (add more sophisticated search later)
    search_query = rx.input(
        placeholder="Search by title, author, faculty, department, or level...",
        on_change=lambda change: State.set_search_query(change.value),  # Update state
    )

    # Filtering (add more filters as needed)
    faculty_filter = rx.select(
        placeholder="Filter by Faculty",
        options=State.faculties,  # Fetch faculties from database or state
        on_change=lambda change: State.set_faculty_filter(change.value),
    )

    filtered_resources = State.resources  # Start with all resources

    # Apply filters (add more filter logic as needed)
    if State.search_query:
        filtered_resources = [
            resource
            for resource in filtered_resources
            if State.search_query.lower()
            in resource.title.lower() + resource.author.lower() + resource.faculty.lower() + resource.department.lower() + resource.level.lower()
        ]
    if State.faculty_filter:
        filtered_resources = [
            resource for resource in filtered_resources if resource.faculty == State.faculty_filter
        ]

    return rx.vstack(
        rx.hstack(search_query, faculty_filter, spacing="1em"),
        rx.vstack(
            *[BookCard(resource) for resource in filtered_resources], spacing="2em"
        ),
        padding="2em",
    )
