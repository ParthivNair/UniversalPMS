from pydantic import BaseModel


class TenantCreate(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: str


class TenantUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    phone_number: str | None = None
    email: str | None = None
