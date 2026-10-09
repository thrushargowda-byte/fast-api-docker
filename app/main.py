from fastapi import FastAPI

app = FastAPI(title="Student CI/CD Demo")


@app.get("/")
def home():
    return {
        "message": "Hello from FastAPI!",
        "version": "v1"
    }


@app.get("/students")
def students():
    return {
        "students": [
            "Rahul",
            "Priya",
            "Amit",
            "Sneha",
            "Rohit",
            "Damodar",
            "Thrusha",
            "Arundhathi"
        ]
    }


@app.get("/health")
def health():
    return {
        "status": "running"
    }