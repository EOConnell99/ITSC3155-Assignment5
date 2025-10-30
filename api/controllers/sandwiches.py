from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create (db: Session, sandwich):
    db_sandwich = models.Sandwich(
        id = sandwich.id,
        price = sandwich.price,
        sandwich_name = sandwich.sandwich_name
    )
    db.add(db_sandwich)
    db.commit()