from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.auth.router import router as router_auth
from fastapi.staticfiles import StaticFiles
from app.api.router import router as router_api

app = FastAPI() # Инициализация FastAPI происходит здесь

# Добавляем middleware для CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Разрешаем все источники - В ПРОИЗВОДСТВЕ ЭТО ОПАСНО!
    allow_credentials=True,
    allow_methods=["*"], # Разрешаем все методы - В ПРОИЗВОДСТВЕ ЭТО ОПАСНО!
    allow_headers=["*"], # Разрешаем все заголовки - В ПРОИЗВОДСТВЕ ЭТО ОПАСНО!
)

app.mount('/static', StaticFiles(directory='app/static'), name='static')

app.include_router(router_api) # Теперь app инициализирован

@app.get("/")
def home_page():
    return {
        "message": "Добро пожаловать! Пусть эта заготовка станет удобным инструментом для вашей работы и "
                   "приносит вам пользу!"
    }


app.include_router(router_auth)
