from mysql_connection import *
from api_yelp import *
from transform_API import *
from etl_pipeline import *
import time
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

print('-'*50)
print(datetime.now())
print('-'*50)

print('-'*50)
print('-Paso 1 extraccion')
print('-'*50)

time.sleep(3)

extract_businesses()
get_reviewsYelp_API()

print('Completo')

time.sleep(5)

print('-'*50)
print('-Paso 2 transformacion')
print('-'*50)

transform_business()
trasnform_reviews_yelp()


print('-'*50)
print('Completo')
print('-'*50)


time.sleep(5)

print('-'*50)
print('-Paso 3 carga, completo')
print('-'*50)

yelp_ER()
yelp_review_ER()


print('-'*50)
print('Completo')
print('-'*50)
