## EmailServiceApp

EmailServiceApp is a RESTful API built using **FastAPI** and **PostgreSQL** to manage email sending efficiently. It provides routes to send the email to anyone at anytime and follows RESTful principles, ensuring high performance and seamless integration.

## Features
- FastAPI-based backend for high-speed API requests
- PostgreSQL for reliable and scalable data storage
- Provides to type of email sending routes
- Supports mostly all email services
- Email-based responses for User related operation.
- Asynchronous request handling for better performance

## Installation

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8+
- PostgreSQL
- pip

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Sumit0ubey/EmailServiceAPP.git
   cd EmailServiceAPP
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables for PostgreSQL connection:
   ```bash
   export DATABASE_URL="postgresql://username:password@localhost/dbname"
   ```
5. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

| Method | Endpoint                   | Description                          |
|--------|----------------------------|--------------------------------------|
| GET    | `/`                        | Retrieve APP info                    |
| POST   | `/users`                   | Create a new user                    |
| GET    | `/users/info`              | Gets a user info                     |
| GET    | `/users/upgrade`           | Gets a email with subscription plans |
| POST   | `/users/newToken/{id}`     | Generates a new token                |
| PUT    | `/users/secureAccount/{id}`| Sets a password                      |
| POST   | `/email/`                  | Sends a email with user email id     |
| POST   | `/email/default/`          | Sends a email with System email id   |


## Documentaion

## Author
Developed by [Sumit dubey](https://github.com/Sumit0ubey).

