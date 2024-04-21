# fastapi라이브러리에서 FastAPI를 불러온다.
from fastapi import FastAPI
from src.routers.house import house_router

# FastAPI 함수를 실행시키면 Fasapi서버가 열리는데, 
# 그 서버를 app라는 변수에 담김
app = FastAPI()

# /house 라는 경로를 타면 house_router로 가게끔 길을 붙여준다.
app.include_router(house_router, prefix = '/house')

# app.include_router(house_router, perfix = '/house')


# @ 데코레이터라고 불리고 꾸며주는 아이
@app.get("/")
# 비동기 함수
async def root():
    return {"message": "Hello World"}

@app.get("/user")
async def root():
    return 'test'


# HTTP 5개
# GET(read), POST(create), PUT(update), PATCH(update), DELETE(delete)