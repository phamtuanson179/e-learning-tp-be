from fastapi import FastAPI
import sys
sys.path.append('''E:\Work\TechSoft\Elearning''')
from app.routes import AuthRoute, UserRoute

app = FastAPI()
app.include_router(UserRoute.router)
app.include_router(AuthRoute.router)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Hello World"}
