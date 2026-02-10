from fastapi import APIRouter

auth_route = APIRouter(prefix="/auth", tags=["auth"])

@auth_route.get("/")
async def get_auth():
    return {"message": "voce acessou a rota de auth"}