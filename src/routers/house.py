from fastapi import APIRouter
from src.services.house import runModel


# routers/house에서 house_router를 불러온다.
# from src.routers.house import house_router

house_router = router = APIRouter()

@router.get('/price/predict')
async def get_prediction_of_house_price(criminal : float, room: float):
        price = await runModel(criminal, room)
        
        print(price)

        return price

# @router.get('/price/what')