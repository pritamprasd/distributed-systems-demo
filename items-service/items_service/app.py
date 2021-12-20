from fastapi import FastAPI
from items import items_router
from models import engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI(title="items-service")
app.include_router(items_router)

@app.get("/status")
def status():
    return "on"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="debug")