import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "Bazel FastAPI App")
    API_STR: str = "/api"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "dev")
    ALLOWED_ORIGINS: list[str] = os.getenv(
        "ALLOWED_ORIGINS", "http://localhost:3000"
    ).split(",")
    CERT_FILE: str = os.getenv("CERT_FILE", "./cert.pem")
    KEY_FILE: str = os.getenv("KEY_FILE", "./key.pem")
    HTTP_PORT: int = int(os.getenv("HTTP_PORT", 8000))
    QUIC_PORT: int = int(os.getenv("QUIC_PORT", 8443))

    @property
    def is_development(self) -> bool:
        return self.ENVIRONMENT == "dev"

    @property
    def is_production(self) -> bool:
        return self.ENVIRONMENT == "prod"


settings = Settings()
