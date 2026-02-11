from fastapi import APIRouter, Depends, HTTPException
from db.session import get_session
from schema.schemas import OrderSchema
from sqlalchemy.orm import Session
from models.models import Order

order_route = APIRouter(prefix="/orders", tags=["orders"])

@order_route.get("/")
async def get_orders():
    return {"messagem": "voce acessou a rota de orders"}


@order_route.post("/order")
async def create_order(orderSchema: OrderSchema, session: Session = Depends(get_session)):
    new_order = Order(user=orderSchema.user)
    session.add(new_order)
    session.commit()
    return HTTPException(status_code=201, detail=f"order created {new_order.id}")