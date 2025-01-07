# App-wide state management

from reflex import State
from models import setup_database, User, Book
from typing import Optional
from sqlalchemy.exc import NoResultFound
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize database session
Session = setup_database()
session = Session()

class AppState(State):
    """
    App-wide state management.
    """
    current_user: Optional[str] = None # Stores the currently logged-in user
    message = ""  # General state for user notifications
    search_results = []  # Holds the search results for the search page
    user_favorites = []  # Tracks books marked as favorites by the current user

    def login(self, email, password):
        """
        Log in a user by verifying credentials.
        """
        try:
            user = session.query(User).filter(User.email == email).one()
            if check_password_hash(user.password_hash, password):
                self.current_user = user
                self.message = "Login successful!"
            else:
                self.message = "Incorrect password."
        except NoResultFound:
            self.message = "User not found."
        except Exception as e:  # Catch broader exceptions
            self.message = f"An error occurred: {e}"
            print(f"Database error during login: {e}") # Log the error for debugging
        finally:
            session.close() # Ensure the session is closed even if errors occur



    def logout(self):
        """
        Log out the current user.
        """
        self.current_user = None
        self.message = "Logged out successfully."

    def register(self, username, email, password):
        """
        Register a new user.
        """
        if session.query(User).filter_by(email=email).first():
            self.message = "Email already registered. Please log in."
            return

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password)
        session.add(new_user)
        session.commit()
        self.message = f"User {username} registered successfully! Please log in."

    def search_books(self, query):
        """
        Search for books by title, author, or department.
        """
        try:
            results = (
                session.query(Book)
                .filter(
                    (Book.title.ilike(f"%{query}%"))
                    | (Book.author.ilike(f"%{query}%"))
                    | (Book.department.ilike(f"%{query}%"))
                )
                .all()
            )
            self.search_results = results
            self.message = f"Found {len(results)} result(s) for '{query}'."
        except Exception as e:
            self.message = f"An error occurred during the search: {e}"
            print(f"Database error during search: {e}") # Log the error for debugging
        finally:
            session.close() # Ensure the session is closed even if errors occur

    


    def add_to_favorites(self, book_id):
        """
        Add a book to the user's favorites.
        """
        try:
            if not self.current_user:
                self.message = "Please log in to add favorites."
                return

            book = session.query(Book).get(book_id)
            if book in self.current_user.favorites:
                self.message = "Book already in favorites."
                return

            self.current_user.favorites.append(book)
            session.commit()
            self.message = f"Book '{book.title}' added to favorites."
        except Exception as e:
            self.message = f"An error occurred adding to favorites: {e}"
            print(f"Database error adding to favorites: {e}") # Log the error for debugging
        finally:
            session.close() # Ensure the session is closed even if errors occur



    def remove_from_favorites(self, book_id):
        """
        Remove a book from the user's favorites.
        """
        if not self.current_user:
            self.message = "Please log in to remove favorites."
            return

        book = session.query(Book).get(book_id)
        if book not in self.current_user.favorites:
            self.message = "Book not in favorites."
            return

        self.current_user.favorites.remove(book)
        session.commit()
        self.message = f"Book '{book.title}' removed from favorites."

    def upload_book(self, title, author, faculty, department, description, file):
        """
        Handle book upload.
        """
        if not self.current_user:
            self.message = "Please log in to upload books."
            return

        # Ensure upload directory exists
        upload_dir = "uploads"
        os.makedirs(upload_dir, exist_ok=True)

        # Save the file
        file_path = os.path.join(upload_dir, file["filename"])
        with open(file_path, "wb") as f:
            f.write(file["content"])

        # Generate download URL
        download_url = f"/{upload_dir}/{file['filename']}"

        # Add book to database
        new_book = Book(
            title=title,
            author=author,
            faculty=faculty,
            department=department,
            description=description,
            download_url=download_url,
            uploader=self.current_user,
        )
        session.add(new_book)
        session.commit()
        self.message = f"Book '{title}' uploaded successfully!"

    def load_user_favorites(self):
        """
        Load the current user's favorite books.
        """
        if self.current_user:
            self.user_favorites = self.current_user.favorites
        else:
            self.user_favorites = []
            self.message = "Please log in to view favorites."


# Example Usage
if __name__ == "__main__":
    # Initialize state
    app_state = AppState()

    # Example: User registration
    app_state.register("JohnDoe", "john@example.com", "password123")
    print(app_state.message)

    # Example: User login
    app_state.login("john@example.com", "password123")
    print(app_state.message)

    # Example: Book search
    app_state.search_books("Physics")
    print(app_state.message)
    for book in app_state.search_results:
        print(book)
