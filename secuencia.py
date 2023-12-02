from mysql_connection import *
from api_yelp import *
from transform_API import *
from etl_pipeline import *
import time
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')


print(datetime.now())
extract_businesses()
get_reviewsYelp_API()
print('Paso 1 extraccion, completo')


transform_business()
trasnform_reviews_yelp()
print('Paso 2 transformacion, completo')


yelp_ER()
yelp_review_ER()
print('Paso 3 carga, completo')

