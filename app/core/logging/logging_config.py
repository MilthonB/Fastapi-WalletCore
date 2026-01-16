import logging
import sys
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler


def configure_logging() -> None:

    logs_path = Path("logs")
    logs_path.mkdir(exist_ok=True)
    
    log_file = logs_path / "app.log"
    log_file.touch(exist_ok=True)
    # ======================
    # FORMATOS
    # ======================
    console_format = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(name)s - %(message)s'
    )

    file_format = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(name)s - %(message)s '
        '[%(filename)s:%(lineno)d]'
    )

    # ======================
    # HANDLER CONSOLA
    # ======================
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_format)

    # ======================
    # HANDLER ARCHIVO (5 días)
    # ======================
    file_handler = TimedRotatingFileHandler(
        filename="logs/app.log",
        when="D",
        interval=1,
        backupCount=5,
        encoding="utf-8",
        utc=False
    )
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(file_format)

    # ======================
    # LOGGER RAÍZ DEL PROYECTO
    # ======================
    logger = logging.getLogger("app")
    logger.setLevel(logging.DEBUG)

    # 🔒 Evita duplicados (FastAPI reload, tests, imports)
    if logger.handlers:
        logger.handlers.clear()

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False
