import uvicorn
from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import os

from database import engine, Base
from routers import users, projects, tasks # Replace with your actual routers

app = FastAPI(title="Project Management API", version="1.0.0", openapi_url="/openapi.json", docs_url="/docs")

# CORS Configuration
origins = ["*"] # In production, replace with specific origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)

# Database Initialization
Base.metadata.create_all(bind=engine)

# Router Registration
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(projects.router, prefix="/api/projects", tags=["Projects"])
app.include_router(tasks.router, prefix="/api/tasks", tags=["Tasks"]) # Example router

# Health Check Endpoint
@app.get("/health", response_model=dict)
def health_check():
    return {"status": "ok"}

# Static Files Serving
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

    @app.get("/{path:path}")
    async def serve_frontend(path: str, request: Request):
        if path.startswith("api"):
            return await request.app.dispatch(request)
        static_file = os.path.join("static", path)
        if os.path.isfile(static_file):
            return FileResponse(static_file)
        return FileResponse(os.path.join("static", "index.html")) # SPA routing
else:
    print("Warning: 'static' directory not found. Frontend assets will not be served.")

# Exception Handling
@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

# Start the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
