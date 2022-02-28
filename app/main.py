from fastapi import FastAPI
import sys
sys.path.append('''E:\Work\TechSoft\Elearning''')
from app.routes import AuthRoute, UserRoute, AdminRoute
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)
app.include_router(AdminRoute.router)
app.include_router(AuthRoute.router)
app.include_router(UserRoute.router)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Hello World"}
