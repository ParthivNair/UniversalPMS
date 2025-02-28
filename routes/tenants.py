from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from schemas import TenantCreate, TenantUpdate
from crud import create_tenant, update_tenant, delete_tenant
from models import Tenant

router = APIRouter()


@router.post("/tenants/", response_model=TenantCreate)
def add_tenant(tenant: TenantCreate, db: Session = Depends(get_db)):
    return create_tenant(db, tenant)


@router.get("/tenants/")
def read_tenants(db: Session = Depends(get_db)):
    return db.query(Tenant).all()


@router.put("/tenants/{tenant_id}")
def update_tenant_route(tenant_id: int, tenant_data: TenantUpdate, db: Session = Depends(get_db)):
    return update_tenant(db, tenant_id, tenant_data)


@router.delete("/tenants/{tenant_id}")
def delete_tenant_route(tenant_id: int, db: Session = Depends(get_db)):
    return delete_tenant(db, tenant_id)
