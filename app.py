# Reflex app entry point

import reflex as rx
from state import State
from pages import auth, home, profile, search, upload, admin
from components import navbar, footer

# Define routes for the app
def index():
    return pc.fragment(
        navbar.render(),
        home.home_page(),
        footer.render(),
    )


def profile_page():
    return pc.fragment(
        navbar.render(),
        profile.profile_page(),
        footer.render(),
    )


def search_page():
    return pc.fragment(
        navbar.render(),
        search.search_page(),
        footer.render(),
    )


def upload_page():
    return pc.fragment(
        navbar.render(),
        upload.upload_page(),
        footer.render(),
    )


def admin_page():
    return pc.fragment(
        navbar.render(),
        admin.admin_page(),
        footer.render(),
    )


def auth_page():
    return auth.auth_page()


# Configure the Reflex app
app = pc.App(state=State)

# Add routes
app.add_page(index, route="/", title="E-Library Home")
app.add_page(auth_page, route="/auth", title="Login/Sign Up")
app.add_page(profile_page, route="/profile", title="User Profile")
app.add_page(search_page, route="/search", title="Search Books")
app.add_page(upload_page, route="/upload", title="Upload Books")
app.add_page(admin_page, route="/admin", title="Admin Dashboard")

# Add static assets
app.compile(
    static_dir="./assets",
    output_dir="./build",
)

# Run the app
if __name__ == "__main__":
    app.run()
