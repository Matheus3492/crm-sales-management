from fastapi import FastAPI

from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    description="CRM para gerenciamento de vendas, clientes e oportunidades.",
    version=settings.app_version,
)


@app.get("/")
def root():
    return {
        "message": settings.app_name,
        "version": settings.app_version,
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
    }