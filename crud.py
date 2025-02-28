from sqlalchemy.orm import Session
from models import Tenant
from schemas import TenantCreate, TenantUpdate
from fastapi import HTTPException


def create_tenant(db: Session, tenant: TenantCreate):
    existing_tenant = db.query(Tenant).filter(Tenant.email == tenant.email).first()
    if existing_tenant:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_tenant = Tenant(
        first_name=tenant.first_name,
        last_name=tenant.last_name,
        phone_number=tenant.phone_number,
        email=tenant.email
    )
    db.add(new_tenant)
    db.commit()
    db.refresh(new_tenant)
    return new_tenant


def update_tenant(db: Session, tenant_id: int, tenant_data: TenantUpdate):
    tenant = db.query(Tenant).filter(Tenant.tenant_id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")

    for field, value in tenant_data.dict(exclude_unset=True).items():
        setattr(tenant, field, value)

    db.commit()
    db.refresh(tenant)
    return tenant


def delete_tenant(db: Session, tenant_id: int):
    tenant = db.query(Tenant).filter(Tenant.tenant_id == tenant_id).first()
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")

    db.delete(tenant)
    db.commit()
    return {"message": "Tenant deleted successfully"}
