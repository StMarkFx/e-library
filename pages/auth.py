# Combines Sign-Up, Login, Password Reset

from reflex import pc
from reflex.state import State


# Define the Authentication State
class AuthState(State):
    email: str = ""
    password: str = ""
    confirm_password: str = ""
    error_message: str = ""

    @staticmethod
    def validate_signup():
        """Validate sign-up details."""
        if not AuthState.email or not AuthState.password:
            AuthState.error_message = "Email and Password are required."
            return False
        if AuthState.password != AuthState.confirm_password:
            AuthState.error_message = "Passwords do not match."
            return False
        return True

    @staticmethod
    def validate_login():
        """Validate login details."""
        if not AuthState.email or not AuthState.password:
            AuthState.error_message = "Email and Password are required."
            return False
        return True

    @staticmethod
    def signup():
        """Handle user sign-up."""
        if AuthState.validate_signup():
            print(f"User signed up with email: {AuthState.email}")
            AuthState.error_message = "Sign-Up successful! Please login."
        else:
            print("Sign-Up failed.")

    @staticmethod
    def login():
        """Handle user login."""
        if AuthState.validate_login():
            print(f"User logged in with email: {AuthState.email}")
            AuthState.error_message = "Login successful!"
        else:
            print("Login failed.")

    @staticmethod
    def reset_password():
        """Handle password reset."""
        if not AuthState.email:
            AuthState.error_message = "Please provide an email address."
            return
        print(f"Password reset link sent to: {AuthState.email}")
        AuthState.error_message = "Password reset link sent to your email."


# Reusable Form Layout
def auth_form(title, inputs, button_label, action, footer_text, footer_link, footer_action):
    """Reusable form layout."""
    return pc.box(
        pc.vstack(
            pc.text(title, font_size="2xl", font_weight="bold"),
            *inputs,
            pc.button(button_label, on_click=action, bg="blue", color="white"),
            pc.text(AuthState.error_message, color="red"),
            pc.hstack(
                pc.text(footer_text, font_size="sm"),
                pc.link(footer_link, on_click=footer_action, font_size="sm", color="blue"),
                spacing="0.5rem",
            ),
            spacing="1rem",
        ),
        padding="2rem",
        box_shadow="md",
        border_radius="md",
        width="100%",
        max_width="400px",
        margin="auto",
    )


# Sign-Up Page
def signup_page():
    return auth_form(
        title="Sign-Up",
        inputs=[
            pc.input(placeholder="Email", on_change=lambda e: AuthState.set_state(email=e.target.value)),
            pc.input(placeholder="Password", type_="password", on_change=lambda e: AuthState.set_state(password=e.target.value)),
            pc.input(placeholder="Confirm Password", type_="password", on_change=lambda e: AuthState.set_state(confirm_password=e.target.value)),
        ],
        button_label="Sign-Up",
        action=AuthState.signup,
        footer_text="Already have an account?",
        footer_link="Login Here",
        footer_action=lambda: print("Navigate to login page"),  # Replace with navigation logic
    )


# Login Page
def login_page():
    return auth_form(
        title="Login",
        inputs=[
            pc.input(placeholder="Email", on_change=lambda e: AuthState.set_state(email=e.target.value)),
            pc.input(placeholder="Password", type_="password", on_change=lambda e: AuthState.set_state(password=e.target.value)),
        ],
        button_label="Login",
        action=AuthState.login,
        footer_text="Forgot your password?",
        footer_link="Reset it here",
        footer_action=lambda: print("Navigate to reset page"),  # Replace with navigation logic
    )


# Password Reset Page
def reset_password_page():
    return auth_form(
        title="Reset Password",
        inputs=[
            pc.input(placeholder="Email", on_change=lambda e: AuthState.set_state(email=e.target.value)),
        ],
        button_label="Send Reset Link",
        action=AuthState.reset_password,
        footer_text="Remember your password?",
        footer_link="Login Here",
        footer_action=lambda: print("Navigate to login page"),  # Replace with navigation logic
    )


# Page Router
def render_auth_page(page_name):
    if page_name == "signup":
        return signup_page()
    elif page_name == "login":
        return login_page()
    elif page_name == "reset":
        return reset_password_page()
    else:
        return login_page()  # Default to login page
