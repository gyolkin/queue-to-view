from fastapi import FastAPI

from src.api.endpoints import router

app = FastAPI(
    title="Demo",
    docs_url="/docs",
)
app.include_router(router)
