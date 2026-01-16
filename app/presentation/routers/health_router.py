
from fastapi import APIRouter
from fastapi.responses import JSONResponse


route: APIRouter =  APIRouter()


@route.get("/health", tags=["system"])
def health_check() -> JSONResponse:
    return JSONResponse(
        status_code=200,
        content={
            "status":"Okay"
        }
    )





