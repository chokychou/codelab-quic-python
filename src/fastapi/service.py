import asyncio
import ssl
import aioquic
import os

from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from hypercorn.asyncio import serve
from hypercorn.config import Config

from src.fastapi.api.api_router.api import api_router
from src.fastapi.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(api_router, prefix=settings.API_STR)

config = Config()


def setup():
    config.bind = [f"0.0.0.0:{settings.HTTP_PORT}"]
    config.quic_bind = [f"0.0.0.0:{settings.QUIC_PORT}"]
    config.alpn_protocols = ["h3", "http/1.1"]

    if settings.is_development:
        setup_development_env()
    elif setting.is_production:
        setup_production_env()
    else:
        raise Exception("Invalid environment")

    configure_logging()
    return


def setup_production_env():
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["Content-Type", "Authorization"],
    )
    # In production, use a real certificate
    config.certfile = settings.CERT_FILE
    config.keyfile = settings.KEY_FILE
    return


def setup_development_env():
    # Allow all origins, methods, headers in development
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Generate a self-signed certificate for testing
    cert_path = Path(settings.CERT_FILE)
    key_path = Path(settings.KEY_FILE)
    if not cert_path.exists() or not key_path.exists():
        import subprocess

        subprocess.run(
            [
                "openssl",
                "req",
                "-x509",
                "-newkey",
                "rsa:4096",
                "-keyout",
                str(key_path),
                "-out",
                str(cert_path),
                "-days",
                "365",
                "-nodes",
                "-subj",
                "/CN=localhost",
            ]
        )
    config.certfile = str(cert_path)
    config.keyfile = str(key_path)
    return


def configure_logging():
    import logging
    import sys

    logger = logging.getLogger("uvicorn")
    logger.handlers = [logging.StreamHandler(sys.stdout)]
    if settings.is_development:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    return


if __name__ == "__main__":
    setup()
    asyncio.run(serve(app, config))
