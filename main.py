from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.router import router
from utils.supabase import init_supabase
from mangum import Mangum


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.supabase = init_supabase()

app.include_router(router)

handler = Mangum(app)
