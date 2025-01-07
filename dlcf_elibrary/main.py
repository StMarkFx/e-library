import reflex as rx
from dlcf_elibrary.pages import index, explore, my_collections, profile, upload_new # Import your pages
from dlcf_elibrary.state import State # Import your state


# Initialize the app.
app = rx.App(state=State)

# Add pages to the app.
app.add_page(index)
app.add_page(explore)
app.add_page(my_collections)
app.add_page(profile)
app.add_page(upload_new)

# Run the app.
app.compile()