import os

class Settings:

    HTTP_PORT = int(os.environ.get("HTTP_PORT", 8000))
    QUIC_PORT = int(os.environ.get("QUIC_PORT", 8443))
    CERT_FILE = os.environ.get("CERT_FILE", "cert.pem")
    KEY_FILE = os.environ.get("KEY_FILE", "key.pem")
    ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS", "*").split(",")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "dev")

    @property
    def is_development(self) -> bool:
        return self.ENVIRONMENT == "dev"

    @property
    def is_production(self) -> bool:
        return self.ENVIRONMENT == "prod"

settings = Settings()
