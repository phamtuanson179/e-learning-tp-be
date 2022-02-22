from fastapi import FastAPI
import sys
sys.path.append('''E:\Work\TechSoft\Elearning''')
from app.routes import AuthRoute, UserRoute, AdminRoute

app = FastAPI()
app.include_router(AdminRoute.router)
app.include_router(AuthRoute.router)
app.include_router(UserRoute.router)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Hello World"}
