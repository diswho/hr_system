from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import auth, employees
from app.db.session import engine, Base

app = FastAPI(title="HR System API", version="0.1.0")

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(employees.router, prefix="/api/v1/employees", tags=["employees"])

@app.on_event("startup")
async def startup():
    # Create database tables
    Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "HR System API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)