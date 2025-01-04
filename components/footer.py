import reflex as rx

def Footer():
    """Generates the footer of the e-library app with useful links, social media, and contact information."""
    
    # Footer content
    return rx.Footer(
        padding="20px",
        background_color="gray.800",
        color="white",
        text_align="center",
        children=rx.Stack(
            children=[
                # Logo or App Name (can be customized)
                rx.Text("e-Library App", font_size="xl", font_weight="bold"),

                # Links section
                rx.Stack(
                    children=[
                        rx.Link("Terms of Service", href="/terms", color="white", font_size="sm", _hover={"color": "blue.300"}),
                        rx.Link("Privacy Policy", href="/privacy", color="white", font_size="sm", _hover={"color": "blue.300"}),
                        rx.Link("Contact Us", href="/contact", color="white", font_size="sm", _hover={"color": "blue.300"}),
                    ],
                    direction="row",
                    spacing="15px",
                    wrap="wrap",  # Ensures the links stack properly on smaller screens
                    justify="center",  # Center the links
                    margin_top="10px"
                ),

                # Social Media Links
                rx.Stack(
                    children=[
                        rx.Link("Facebook", href="https://facebook.com", color="white", font_size="sm", _hover={"color": "blue.500"}),
                        rx.Link("Twitter", href="https://twitter.com", color="white", font_size="sm", _hover={"color": "blue.400"}),
                        rx.Link("LinkedIn", href="https://linkedin.com", color="white", font_size="sm", _hover={"color": "blue.600"}),
                    ],
                    direction="row",
                    spacing="15px",
                    wrap="wrap",
                    justify="center",
                    margin_top="10px"
                ),

                # Contact Email
                rx.Text("For support, contact us at: support@elibrary.com", font_size="sm", margin_top="10px"),

                # Copyright text
                rx.Text("© 2025 e-Library. All Rights Reserved.", font_size="sm", margin_top="20px"),
            ],
            spacing="10px",  # Space between items in the stack
        ),
    )
