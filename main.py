from fastapi import FastAPI
from routes.tenants import router as tenant_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(tenant_router)


@app.get("/")
def root():
    return {"message": "Welcome to the Tenant Management System!"}