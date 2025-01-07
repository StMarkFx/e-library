 # Admin Dashboard (Optional)

import reflex as rx
from components.navbar import Navbar
from components.footer import Footer

def AdminDashboard():
    """Admin Dashboard page to manage users and books in the e-library app."""

    # Example Data for Books and Users (Replace with actual database queries)
    total_books = 1200
    total_users = 350
    pending_contributions = 10

    # Manage Books Section
    manage_books = rx.Box(
        children=rx.VStack(
            children=[
                rx.Text("Manage Books", font_size="xl", font_weight="bold"),
                rx.Text(f"Total Books: {total_books}", font_size="lg"),
                rx.Button(
                    children="View All Books",
                    on_click=lambda: rx.navigate("/admin/books"),
                    color="white",
                    bg_color="blue.500",
                    _hover={"bg_color": "blue.400"},
                ),
            ],
            spacing="8px",
        ),
        padding="16px",
        border_radius="md",
        border="1px solid",
        border_color="gray.300",
        bg_color="white",
    )

    # Manage Users Section
    manage_users = rx.Box(
        children=rx.VStack(
            children=[
                rx.Text("Manage Users", font_size="xl", font_weight="bold"),
                rx.Text(f"Total Users: {total_users}", font_size="lg"),
                rx.Button(
                    children="View All Users",
                    on_click=lambda: rx.navigate("/admin/users"),
                    color="white",
                    bg_color="green.500",
                    _hover={"bg_color": "green.400"},
                ),
            ],
            spacing="8px",
        ),
        padding="16px",
        border_radius="md",
        border="1px solid",
        border_color="gray.300",
        bg_color="white",
    )

    # Pending Contributions Section
    pending_contrib = rx.Box(
        children=rx.VStack(
            children=[
                rx.Text("Pending Contributions", font_size="xl", font_weight="bold"),
                rx.Text(f"Contributions Pending: {pending_contributions}", font_size="lg"),
                rx.Button(
                    children="Approve Contributions",
                    on_click=lambda: rx.navigate("/admin/contributions"),
                    color="white",
                    bg_color="yellow.500",
                    _hover={"bg_color": "yellow.400"},
                ),
            ],
            spacing="8px",
        ),
        padding="16px",
        border_radius="md",
        border="1px solid",
        border_color="gray.300",
        bg_color="white",
    )

    # Admin Dashboard Layout
    return rx.Stack(
        children=[
            Navbar(),  # Including the responsive navbar
            rx.Box(
                children=rx.VStack(
                    children=[
                        # Admin Dashboard Heading
                        rx.Text(
                            children="Admin Dashboard",
                            font_size="3xl",
                            font_weight="bold",
                            text_align="center",
                            margin_bottom="20px",
                        ),
                        
                        # Cards for Books, Users, and Pending Contributions
                        rx.HStack(
                            children=[
                                manage_books,
                                manage_users,
                                pending_contrib,
                            ],
                            spacing="20px",
                            wrap="wrap",
                            justify="center",
                        ),
                    ],
                    spacing="20px",
                    align="center",
                ),
                padding="20px",
            ),
            Footer(),  # Adding footer to the page
        ]
    )

# Sample code for navigation, if needed, replace with the actual routing logic
def navigate(page: str):
    """Simulated navigation function for page redirection."""
    rx.navigate(page)
