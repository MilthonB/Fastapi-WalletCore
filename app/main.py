
from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware
from app.presentation.routers import wallet_routers


# ------------------------------------
# Crear instancia de FastAPI
# ------------------------------------
app = FastAPI(
    title="Api WalletCore",
    description="Api construida con clean architecture + DDD ligero",
    version="1.0.0"
)


# ------------------------------------
# Middleware: CORS (Cross-Origin Resource Sharing)
# ------------------------------------
# Permite llamadas desde cualquier frontend para desarrollo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringir a dominios específicos más tarde
    allow_methods=["*"],  # Permite GET, POST, PATCH, DELETE, etc.
    allow_headers=["*"],  # Permite cualquier header
)


test_router = APIRouter()

@test_router.get("/ping")
def ping()-> object:
    return {
        "status": "ok", 
        "message": "FastApi esta vivo"
    }

# ------------------------------------
# Incluir routers con prefijo de versión
# ------------------------------------
app.include_router(wallet_routers.router, prefix="/api/v1/wallets", tags=["wallets"])



@app.on_event("startup")
async def startup_event()-> None:
    print("🚀 Server starting up...")


@app.on_event("shutdown")
async def shutdown_event()-> None:
    print("Server shutting down...")



