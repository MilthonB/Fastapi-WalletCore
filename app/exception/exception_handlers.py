
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.application.exceptions.application_exception  import ApplicationException
from app.application.exceptions.dto_exceptions import DtoException
from app.application.exceptions.mapper_exception import MapperException
from app.infrastructure.exceptions.datasources_exeptions import DatasourcesExceptions
import logging

def exception_handlers(app: FastAPI) -> None:

    logger =  logging.getLogger("app")


    @app.exception_handler(ApplicationException)
    async def application_exception_handler( request: Request, exc:ApplicationException)-> JSONResponse:

        if exc.status_code == 500:
            logger.critical(f"{exc.__class__.__name__}: {exc} | path={request.url.path}", exc_info=True)
        else:
            logger.warning(f"{exc.__class__.__name__}: {exc} | path={request.url.path}")

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": exc.__class__.__name__,
                "message": str(exc)
            }
        )

    @app.exception_handler(DtoException)
    async def dto_exception_handler(request: Request, exc: DtoException) -> JSONResponse:
        logger.warning(f"{exc.__class__.__name__}: {exc} | path:{request.url.path}")
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error":exc.__class__.__name__,
                "message": str(exc)
            }
        )

    @app.exception_handler(MapperException)
    async def mapper_exception_handler(request:Request, exc:MapperException)-> JSONResponse:
        logger.warning(f"{exc.__class__.__name__}: {exc} | path:{request.url.path}")
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": exc.__class__.__name__,
                "message": str(exc)
            }
        )

    @app.exception_handler(DatasourcesExceptions)
    async def datasources_exeptions_handler(request: Request, exc: DatasourcesExceptions) -> JSONResponse:
        if exc.status_code != 500:
            logger.warning(f"{exc.__class__.__name__}: {exc} | path:{request.url.path}")
        else:
            logger.critical(f"{exc.__class__.__name__}: {exc} | path:{request.url.path}")


        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": exc.__class__.__name__,
                "message": str(exc)
            }
        )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
        logger.critical(f"{exc.__class__.__name__}: {exc} | path:{request.url.path}")
        return JSONResponse(
            status_code=500,
            content={
                "error": "InternaServerError",
                "message": "Ha ocurrido un error interno en el servidor"
            }
        )

