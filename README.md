# DLCF OAU E-Library: A Reflex Application

This project implements a digital library for the Department of Computer and Information Science (DLCF) at Obafemi Awolowo University (OAU), leveraging the Reflex web framework.  It provides a platform for students, faculty, and staff to access, share, and manage academic resources.

## Features

* **User Authentication:** Secure login and signup with email/password or Google authentication.
* **Profile Management:** Users can create and manage their profiles, including avatar, display name, faculty, department, level, and interests.
* **Resource Upload:** Faculty and students can upload academic resources (e.g., PDFs, documents).  Uploads are subject to administrator approval.
* **Resource Exploration:** Users can search and filter resources by title, author, faculty, department, level, and keywords.
* **Personalized Recommendations:** The system provides personalized recommendations based on user profiles and interests.
* **Resource Management:** Users can view and manage their uploaded resources, including filtering by approval status and date.
* **Engagement Features:** Users can like and comment on resources.
* **Responsive Design:** The application is designed to be responsive and accessible across various devices.
* **Metrics Tracking:** The system tracks resource downloads and uploads.


## Technology Stack

* **Frontend:** Reflex (built on top of React and Next.js)
* **Backend:** Reflex (built on top of FastAPI)
* **Database:** MongoDB (or PostgreSQL - adaptable)
* **File Storage:**  (Adaptable - AWS S3, local storage, etc.)
* **Authentication:** bcrypt (password hashing), potentially Google OAuth


## Project Structure

```bash
dlcf-oau-elibrary/
├── .venv/ # Virtual environment (not tracked by Git)
├── assets/ # Static assets (images, CSS, etc.)
├── pages/ # Reflex page modules (homepage.py, explore.py, etc.)
│ ├── homepage.py
│ ├── explore.py
│ ├── profile.py
│ ├── upload.py
│ ├── my_collections.py
│ ├── login.py
│ ├── signup.py
│ ├── manage_uploads.py
│ └── ...
├── components/ # Reusable UI components (optional)
├── models.py # Pydantic models for User and Resource
├── state.py # Application state management
├── main.py # Main application module
├── rxconfig.py # Reflex application configuration
├── README.md # T
└── requirements.txt # Project dependencies
```

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   ```
2. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure the database:**  (Instructions will depend on your chosen database)
5. **Configure file storage:** (Instructions will depend on your chosen storage solution)
6. **Run the application:**
   ```bash
   reflex run
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

[MIT License]