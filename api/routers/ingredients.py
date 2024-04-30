# routers/ingredient_router.py

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..controllers import ingredient as controller
from ..schemas import ingredient as schema

router = APIRouter()

@router.post("/ingredients/", response_model=schema.IngredientRead, status_code=status.HTTP_201_CREATED)
def create_ingredient_route(ingredient: schema.IngredientCreate, db: Session = Depends(get_db)):
    return controller.create_ingredient(db, ingredient)

@router.get("/ingredients/{ingredient_id}", response_model=schema.IngredientRead)
def read_ingredient_route(ingredient_id: int, db: Session = Depends(get_db)):
    return controller.get_ingredient(db, ingredient_id)

@router.put("/ingredients/{ingredient_id}", response_model=schema.IngredientRead)
def update_ingredient_route(ingredient_id: int, updated_ingredient: schema.IngredientUpdate, db: Session = Depends(get_db)):
    return controller.update_ingredient(db, ingredient_id, updated_ingredient)

@router.delete("/ingredients/{ingredient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_ingredient_route(ingredient_id: int, db: Session = Depends(get_db)):
    controller.delete_ingredient(db, ingredient_id)
    return {"ok": True}
