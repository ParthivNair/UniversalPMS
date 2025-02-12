from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

USER_DATA_FILE = "users.json"
DASHBOARD_DATA_FILE = "dashboard.json"

users = {
    "tenant": {"username": "tenant", "password": "tenant", "userType": "tenant"},
    "manager": {"username": "manager", "password": "manager", "userType": "manager"},
    "staff": {"username": "staff", "password": "staff", "userType": "staff"}
}

dashboard_data = {
    "tenant": {
        "message": "Welcome back, Tenant!",
        "unit": "Unit 200, University Center",
        "rent_amount": "$1575",
        "due_date": "2025-02-01",
        "maintenance_requests": 2,
        "unread_messages": 3
    },
    "manager": {
        "message": "Hello, Manager! Here’s a summary of the property",
        "total_properties": 24,
        "active_tenants": 186,
        "pending_tasks": 12,
        "maintenance_requests": 8
    },
    "staff": {
        "message": "Hi Staff, check your assigned tasks.",
        "tasks_pending": 5,
        "assigned_properties": 3,
        "schedule": 12
    }
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

with open(USER_DATA_FILE, "w") as f:
    json.dump(users, f)

with open(DASHBOARD_DATA_FILE, "w") as f:
    json.dump({
        "tenant": {"message": "Welcome, Tenant!", "rent_amount": "$1200", "due_date": "2025-03-01"},
        "manager": {"message": "Hello, Manager! Here’s a summary of the property"},
        "staff": {"message": "Hi Staff, check maintenance requests."}
    }, f)


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    with open(USER_DATA_FILE, "r") as f:
        users_login = json.load(f)

    user = users_login.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    return {"access_token": form_data.username, "token_type": "bearer", "userType": user["userType"]}


@app.get("/dashboard")
def get_dashboard(token: str = Depends(oauth2_scheme)):
    if token in dashboard_data:
        return dashboard_data[token]
    else:
        raise HTTPException(status_code=404, detail="User data not found")

