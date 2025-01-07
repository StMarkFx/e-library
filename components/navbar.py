import reflex as rx

def Navbar():
    """Generates a responsive navigation bar for the e-library app."""
 
    # Define navigation links
    nav_links = [
        ("Home", "/"),
        ("Browse Books", "/browse"),
        ("Search", "/search"),
        ("Upload Book", "/upload"),
        ("Profile", "/profile"),
    ]

    # Navbar content 
    return rx.Navbar(
        background_color="gray.800",
        color="white",
        padding="10px 20px",
        children=rx.HStack(
            children=[
                # Logo Section (could be customized)
                rx.Link(
                    children=rx.Image(src="/assets/logo.png", alt="e-Library Logo", box_size="50px"),
                    href="/",
                ),
                
                # Navigation Links (for larger screens)
                rx.HStack(
                    children=[
                        # Create a link for each navigation item
                        *[rx.Link(
                            children=link[0],
                            href=link[1],
                            color="white",
                            font_size="lg",
                            _hover={"color": "blue.400"},
                            _active={"color": "blue.500"},  # Highlight active link
                        ) for link in nav_links],
                    ],
                    spacing="30px",
                    display={"base": "none", "md": "flex"},  # Only show on larger screens
                ),

                # User Profile Icon (on the right)
                rx.HStack(
                    children=[
                        # Profile icon, can be linked to the user profile page or dropdown
                        rx.Link(
                            children=rx.Icon(name="person", box_size="30px", color="white"),
                            href="/profile",  # Example link to user profile
                            _hover={"color": "blue.400"},
                        ),
                    ],
                    spacing="20px",
                    align="center",
                ),

                # Mobile Menu Toggle (Hamburger icon for smaller screens)
                rx.HStack(
                    children=[
                        rx.IconButton(
                            icon=rx.Icon(name="menu"),
                            aria_label="Open Menu",
                            on_click=lambda: rx.toggle("menu_visible"),  # Toggles the menu visibility
                            color="white",
                            _hover={"color": "blue.400"},
                            display={"base": "flex", "md": "none"},  # Only show on mobile screens
                        ),
                    ],
                    spacing="0",
                    align="center",
                    display={"base": "flex", "md": "none"},
                ),
            ],
            spacing="20px",
            align="center",
        ),
        # Mobile Menu Dropdown (only visible when toggled)
        bottom=rx.Box(
            children=rx.VStack(
                children=[
                    *[rx.Link(
                        children=link[0],
                        href=link[1],
                        color="white",
                        font_size="lg",
                        _hover={"color": "blue.400"},
                        _active={"color": "blue.500"},
                    ) for link in nav_links],
                ],
                spacing="10px",
                align="start",
            ),
            padding="10px",
            bg_color="gray.800",
            display={"base": "none", "md": "flex"},
            visibility={"menu_visible": "visible", "hidden": "hidden"},  # Show on mobile when toggled
        ),
    )
