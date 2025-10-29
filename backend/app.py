from fastapi import FastAPI
from routes.items import router as items_router

app = FastAPI()

# python -m uvicorn app:app --reload --port 8000

# equivalente a app.use('/items', router) en Express
app.include_router(items_router, prefix="/items", tags=["items"])

@app.get("/")
async def root():
    return {"message": "ok"}