from typing import List
import xgboost as xgb
import pandas as pd

loaded_model = xgb.XGBRegressor()

loaded_model.load_model('src/models/xgb_model.json')


# 서버를 위한 로직
# 아래 속성들을 이용해 MEDV를 예측하는 것
# CRIM : 자치시(town) 별 1인당 범죄율. 대략 0~20 사이의 float
# ZN : 25,000 평방피트를 초과하는 거주지역의 비율. 대략 0, 75, 12.5, 18인 것으로 보야. 0~100 사이의 float로 하면 될 듯
# INDUS : 비소매상업지역이 점유하고 있는 토지의 비율. 대충 0~50 사이의 float.
# CHAS : 찰스강에 대한 더미 변수(강 경계의 위치한 경우 1 아니면 0) 0 or 1 int.
# NOX : 10ppm당 농축 일산화질소. 대략 0~1 사이의 float.
# RM : 주택 1가구당 평균 방의 개수. 대략 1~10 사이의 float.
# AGE : 1940년 이전에 건축된 소유주택의 비율. 대략 0~100 사이의 float.
# DIS : 5개의 보스턴 직업센터까지의 접근성 지수. 대략 1~10(좀더 쳐서 1.5~6) 사이의 float.
# RAD : 방사형 도로까지의 접근성 지수. 대략 1~25 사이의 int.
# TAX : 10,000 달러 당 재산세율. 대략 200~1000 사이의 float.
# PTRATIO : 자치시 (town)별 학생/교사 비율. 대략 15~21 사이의 float.
# B : 1000(Bk-0.64)^2, 여기서 Bk는 자치시별 흑인의 비율. 대략 0~400 사이의 float.
# LSTAT : 모집단의 하위계층의 비율(%). 0~100 사이의 float.
# MEDV : 본인 소유의 주택 가격(중앙값) (단위 : $1,000).


async def runModel(crim: float, rm: float) -> float:
  dic = {
    "CRIM": [crim],
    "ZN": [18.0],
    "INDUS": [22.37],
    "CHAS": [0],
    "NOX": [0.145],
    "RM": [rm],
    "AGE": [66.7],
    "DIS": [4.291],
    "RAD": [13],
    "TAX": [333.333],
    "PTRATIO": [21.0],
    "B": [197.6],
    "LSTAT": [23.4]
  }
      
  # dictionary 형태를 DataFrame 형태로 변환한다.
  input = pd.DataFrame.from_dict(dic, orient='columns')
  
  # input 값을 이용해서 예측값을 만들고, z에 대입한다.  
  z = loaded_model.predict(input)

  # 변수 z의 타입이 numpy이기 때문에 list로 바꿔준다.
  result: List[float] = z.tolist()
  
  return result[0]