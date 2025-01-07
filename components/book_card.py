# Reusable book card component

import reflex as rx

def BookCard(title, author, faculty, department, description, download_url=None, on_read=None, on_download=None):
    """
    Creates a reusable book card component.

    Args:
        title (str): The title of the book.
        author (str): The author's name.
        faculty (str): The faculty under which the book falls.
        department (str): The department under which the book falls.
        description (str): A brief description of the book.
        download_url (str, optional): URL for downloading the book. Defaults to None.
        on_read (Callable, optional): Callback function for the "Read" button. Defaults to None.
        on_download (Callable, optional): Callback function for the "Download" button. Defaults to None.

    Returns:
        pc.Component: A Reflex (Pynecone) component representing the book card.
    """
    return rx.box(
        rx.vstack(
            # Book title
            rx.heading(title, size="lg", color="blue.600"),
            # Author and faculty/department
            rx.text(f"Author: {author}", font_size="sm", color="gray.600"),
            rx.text(f"Faculty: {faculty} | Department: {department}", font_size="sm", color="gray.500"),
            # Book description (truncated for card display)
            rx.text(
                description[:120] + "..." if len(description) > 120 else description,
                font_size="sm",
                color="gray.700",
            ),
            # Action buttons: Read and Download
            rx.hstack(
                rx.button(
                    "Read",
                    on_click=on_read,
                    color_scheme="blue",
                    size="sm",
                ) if on_read else None,
                rx.button(
                    "Download",
                    on_click=on_download,
                    color_scheme="green",
                    size="sm",
                    is_disabled=download_url is None,
                ) if on_download else None,
                spacing=4,
            ),
            spacing=2,  # Vertical spacing between elements
        ),
        border="1px solid",
        border_color="gray.300",
        border_radius="md",
        padding="4",
        shadow="sm",
        background="white",
        max_width="300px",
    )
