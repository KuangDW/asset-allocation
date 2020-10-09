#%%

import pandas as pd
import numpy as np
import pymysql
import math
import statistics
import time
import datetime
from itertools import combinations, permutations
from scipy.special import comb, perm
from dateutil.relativedelta import relativedelta

#%%
today = datetime.date.today()
# starttime = datetime.datetime.now()
# db = pymysql.connect("localhost", "root", "esfortest", "etf")

# name = 'max'
# password = '1234'
import sys
username = sys.argv[1]
password = sys.argv[2]



db = pymysql.connect("localhost", "root", "esfortest", "etf")
cursor = db.cursor()
sql = "select * from `user_datat` where (name = '"+ str(username) +"' and id = '" + str(password) +"')"

cursor.execute(sql)
result_select = cursor.fetchall()
db.commit()

start_date = result_select[0][2]
vary = relativedelta(today,start_date)

every_asset_money = result_select[0][6].split('  ')
total_money = 0
for i in range(len(every_asset_money)):
    total_money = total_money + float(every_asset_money[i])


choose = result_select[0][4].split(' ')
weight = result_select[0][5].split(' ')
want_t = vary.months + (vary.years*12)
per_in_money = float(result_select[0][10])
input_money = want_t*(per_in_money/12) + float(result_select[0][9])
want_type = 2

print(input_money)
print(total_money)

sql_del1 = "TRUNCATE TABLE `user_datat`"
sql_del2 = "TRUNCATE TABLE `user_datatr`"
cursor.execute(sql_del1)
cursor.execute(sql_del2)
db.commit()

db.close()
# %%
