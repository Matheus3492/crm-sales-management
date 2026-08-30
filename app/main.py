from fastapi import FastAPI

app = FastAPI(
    title="CRM Sales Management",
    description="CRM para gerenciamento de vendas, clientes e oportunidades.",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "CRM Sales Management API",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
    }