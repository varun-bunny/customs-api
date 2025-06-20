from fastapi import FastAPI
from .database import Base, engine
from .routers import customers, branches

Base.metadata.create_all(bind=engine)   # create tables on startup

app = FastAPI(
    title="Customs Customer & Branch API",
    description="Intern demo project – one-command Docker stack",
)

app.include_router(customers.router)
app.include_router(branches.router)

@app.get("/")
def root(): return {"msg": "Service healthy ✅"}
