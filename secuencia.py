from mysql_connection import *
from api_yelp import *
from transform_API import *
from etl_pipeline import *
import time
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

print('-'*20)

print(datetime.now())

print('-'*40)
extract_businesses()
get_reviewsYelp_API()
print('-'*10)
print('-Paso 1 extraccion, completo')
print('-'*10)

transform_business()
trasnform_reviews_yelp()
print('-'*10)
print('-Paso 2 transformacion, completo')
print('-'*10)

yelp_ER()
yelp_review_ER()
print('-'*10)
print('-Paso 3 carga, completo')
print('-'*10)
