from fastapi import APIRouter

order_route = APIRouter(prefix="/orders", tags=["orders"])


@order_route.get("/")
async def get_orders():
    return {"messagem": "voce acessou a rota de orders"}