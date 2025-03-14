from fastapi import FastAPI
from routers import prospects, emails

app = FastAPI(title="Cold Email System", version="1.0.0")

# Include routers
app.include_router(prospects.router)
app.include_router(emails.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Cold Email System"}