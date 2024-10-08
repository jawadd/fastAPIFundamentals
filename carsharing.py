from datetime import datetime

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def welcome(name):
    """Return a friendly welcome message."""
    return {'message': f"Welcome, {name}, the Car Sharing service!"}


@app.get("/date")
def date():
    """Return the current date/time."""
    return {'date': datetime.now()}