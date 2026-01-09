
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from ..domain.exceptions.handlers.register_exception_handlers import (
    InvalidCurrencyError,
    WalletAlreadyExistsError,
    WalletNotFoundError
)


def exception_handlers(app: FastAPI)->None:

    @app.exception_handler(WalletAlreadyExistsError)
    async def wallet_exists_handler(reques:Request, exc:WalletAlreadyExistsError) -> JSONResponse:
        return JSONResponse(
            status_code=409,
            content={"detail": str(exc)}
        )
    @app.exception_handler(WalletNotFoundError)
    async def wallet_not_found_error(reques:Request, exc:WalletNotFoundError) -> JSONResponse:
        return JSONResponse(
            status_code=404,
            content={"detail": str(exc)}
        )
    @app.exception_handler(InvalidCurrencyError)
    async def Invalid_currency_error(request: Request, exc:InvalidCurrencyError)->JSONResponse:
        return JSONResponse(
            status_code=400,
            content={"detail":str(exc)}
        )
    @app.exception_handler(Exception)
    async def internal_server_error(request:Request, exc: Exception)->JSONResponse:
        return JSONResponse(
            status_code=500,
            content={"detail":"Internal server error"}
        )