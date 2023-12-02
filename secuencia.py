from mysql_connection import *
from api_yelp import *
from transform_API import *
from etl_pipeline import *
import time
import warnings
warnings.filterwarnings('ignore')


extract_businesses()
get_reviewsYelp_API()
print('Paso 1 extraccion, completo')
time.sleep(60)

transform_business()
trasnform_reviews_yelp()
print('Paso 2 transformacion, completo')
time.sleep(60)

yelp_ER()
yelp_review_ER()
print('Paso 3 carga, completo')
