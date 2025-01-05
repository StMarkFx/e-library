 # Database models for users, books, etc.

from sqlalchemy import (
    Column,
    String,
    Integer,
    Text,
    ForeignKey,
    DateTime,
    Boolean,
    Table,
    create_engine,
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

# Initialize the base class for models
Base = declarative_base()

# Many-to-Many relationship for user favorites
user_favorites = Table(
    "user_favorites",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("book_id", Integer, ForeignKey("books.id"), primary_key=True),
)

# User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False)  # Admin flag
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    uploaded_books = relationship("Book", back_populates="uploader")
    reading_history = relationship("ReadingHistory", back_populates="user")
    favorites = relationship(
        "Book", secondary=user_favorites, back_populates="favorited_by"
    )

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, is_admin={self.is_admin})>"


# Book model
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(150), nullable=False)
    author = Column(String(100), nullable=False)
    faculty = Column(String(100), nullable=False)
    department = Column(String(100), nullable=False)
    description = Column(Text)
    download_url = Column(String(255), nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    # Foreign Key
    uploader_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    uploader = relationship("User", back_populates="uploaded_books")
    favorited_by = relationship(
        "User", secondary=user_favorites, back_populates="favorites"
    )

    def __repr__(self):
        return f"<Book(id={self.id}, title={self.title}, author={self.author})>"


# Reading history model
class ReadingHistory(Base):
    __tablename__ = "reading_history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))
    read_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="reading_history")
    book = relationship("Book")

    def __repr__(self):
        return f"<ReadingHistory(id={self.id}, user_id={self.user_id}, book_id={self.book_id})>"


# Database setup
def setup_database(database_url="sqlite:///e_library.db"):
    """
    Set up the database engine, create tables, and return a session maker.
    """
    engine = create_engine(database_url, echo=False)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)


# Usage example
if __name__ == "__main__":
    # Initialize the database
    Session = setup_database()
    session = Session()

    # Example: Add a new user
    new_user = User(username="admin", email="admin@example.com", password_hash="hashed_password", is_admin=True)
    session.add(new_user)
    session.commit()
    print(f"User added: {new_user}")
