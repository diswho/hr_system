# HR System Backend

A FastAPI-based backend for an HR system with employee management, authentication, and more.

## Features
- Employee management
- User authentication (JWT)
- PostgreSQL database integration
- RESTful API endpoints

## Setup Instructions

1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up PostgreSQL:
   - Install PostgreSQL if not already installed
   - Create a database named `hr_system`
   - Update the `.env` file with your database credentials:
     ```
     DATABASE_URL=postgresql://username:password@localhost:5432/hr_system
     SECRET_KEY=your-secret-key-here
     ALGORITHM=HS256
     ACCESS_TOKEN_EXPIRE_MINUTES=30
     ```

5. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

6. Access the API documentation at:
   - http://localhost:8000/docs (Swagger UI)
   - http://localhost:8000/redoc (ReDoc)

## API Endpoints
- `/api/v1/auth/register` - User registration
- `/api/v1/auth/token` - Get access token
- `/api/v1/employees` - Employee management