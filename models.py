from sqlalchemy import Column, Integer, String
from db import Base


class Tenant(Base):
    __tablename__ = "tenants"

    tenant_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone_number = Column(String(10), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
