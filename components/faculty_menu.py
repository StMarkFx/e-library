# Faculty and department navigation

import reflex as rx
from typing import List

# Simulate fetching faculty and department data from a database or API
def get_faculty_data() -> List[dict]:
    """Simulates fetching faculty data from an API/database."""
    return [
        {"name": "Faculty of Science", "departments": ["Physics", "Chemistry", "Biology"]},
        {"name": "Faculty of Arts", "departments": ["History", "Linguistics", "Philosophy"]},
        {"name": "Faculty of Engineering", "departments": ["Mechanical Engineering", "Electrical Engineering", "Civil Engineering"]},
    ]

# Function to handle department selection
def on_department_click(department: str):
    """Handle department button click to filter books by department."""
    # For demonstration, this could call an API to fetch books by department
    print(f"Fetching books for department: {department}")
    # In a real app, you'd probably want to update the app state to reflect the filtered books.
    # This is a placeholder for your actual book fetching logic.

def FacultyMenu():
    """Generates the faculty menu with collapsible departments, clickable buttons, and animations."""
    
    # Fetch the faculty data
    faculties = get_faculty_data()

    # Faculty Menu items
    faculty_items = []
    for faculty in faculties:
        faculty_name = faculty["name"]
        departments = faculty["departments"]
        
        # Create a collapsible menu for each faculty
        faculty_item = rx.Collapsible(
            header=rx.Text(faculty_name, font_size="lg", font_weight="bold"),
            content=rx.Column([
                rx.Button(
                    department, 
                    variant="link", 
                    size="sm", 
                    color="blue",
                    _hover={"color": "white", "bg": "blue.500"},  # Hover effect
                    on_click=lambda dept=department: on_department_click(dept)
                ) 
                for department in departments
            ], gap=2),
            default_open=False,  # Faculty is initially collapsed
            animation={"duration": "0.3s", "easing": "ease-in-out"}  # Smooth collapse/expand animation
        )
        
        faculty_items.append(faculty_item)
    
    # Return the full menu
    return rx.Stack(faculty_items)

# Usage Example:
# To use the FacultyMenu component, it would be included in the main layout (e.g., in the sidebar or main page).
