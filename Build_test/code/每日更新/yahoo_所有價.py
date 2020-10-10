
from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import datetime
from selenium.webdriver.chrome.options import Options
import requests
import datetime
from dateutil.parser import parse 
import pymysql

#ETF類表
etf = ['VTI','VOO','VXUS','SPY','BND','IVV','BNDX','VEA','VO',
       'VUG','VB','VWO','VTV','QQQ','BSV','BIV','VTIP','VOE','IEF',
       'SHY','TLT','IVE','VT','GOVT']
#輸入Mysql前的資料，並且先都設定為0
input_data_open = []
input_data_high = []
input_data_low = []
input_data_adj = []
input_data_close = []
input_data_volume = []
true_today =[]

for i in range(24):
    input_data_open.append(0)
for i in range(24):
    input_data_high.append(0)
for i in range(24):
    input_data_low.append(0)
for i in range(24):
    input_data_adj.append(0)
for i in range(24):
    input_data_close.append(0)
for i in range(24):
    input_data_volume.append(0)
for i in range(24):
    true_today.append(0)
# #開啟瀏覽器並進入DJ網頁for 抓取正確日期
# driver = webdriver.Chrome("C:/Users/User/Downloads/chromedriver.exe")
# driver.get("https://www.moneydj.com/ETF/X/Basic/Basic0003.xdjhtm?etfid=VTI")
# time.sleep(2)
# driver.get(driver.current_url)
# soup = bs(driver.page_source,"html.parser")
# check_raw_data = [data.text for data in soup.find_all('td',{'class':['col01']})]
# check_raw_data[0]=check_raw_data[0].strip()
# today = check_raw_data[0]
# true_today = today[3:13]
# print(true_today)
# driver.close()
# time.sleep(2)
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")




url1 = 'https://finance.yahoo.com/quote/'
url2 = '/history?p='
url3 = '&.tsrc=fin-srch'
#開啟瀏覽器並進入yahoo網頁
driver = webdriver.Chrome("C:/Users/User/Downloads/安裝檔案/chromedriver.exe", chrome_options = chrome_options)
driver.get("https://finance.yahoo.com/quote/VTI/history?p=VTI")
soup = bs(driver.page_source,"html.parser")

time.sleep(5)
#根據ETF列表重複執行抓取資料的動作
for i in range(24):
    print(etf[i])
    print(i)
    # # 找到網頁中的輸入name，並把ETF名稱輸入
    # search_input = driver.find_element_by_name("yfin-usr-qry")
    # search_input.send_keys(etf[i])
    # time.sleep(1)
    # # click
    # start_search_btn = driver.find_element_by_id("search-button")
    # start_search_btn.click()
    # time.sleep(1)
    # # 進入新的網頁，重新分析網頁組成
    # driver.get(driver.current_url)
    # soup = bs(driver.page_source,"html.parser")
    # time.sleep(2)

    url = url1 + etf[i] + url2 + etf[i] + url3
    driver.get(url)
    time.sleep(5)
    soup = bs(driver.page_source,"html.parser")

    #raw_data = [data.text for data in soup.find('td',{'class':['Py(10px) Ta(start) Pend(10px)','Py(10px) Pstart(10px)']})]

    # 抓取資料
    # if etf[i] == "BND" or etf[i] == "BNDX" or etf[i] == "BSV" or etf[i] == "BIV" or etf[i] == "IEF" or etf[i] == "SHY" or etf[i] == "TLT" or etf[i] == "GOVT":
    #     raw_data = [data.text for data in soup.find('tr',{'class':['BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'],'data-reactid':["118"]})]
    # else:
    #     raw_data = [data.text for data in soup.find('tr',{'class':['BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'],'data-reactid':["111"]})]
    raw_data = [data.text for data in soup.find('tr',{'class':['BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'],'data-reactid':["51"]})]
    # raw_data = [data.text for data in soup.find('tr',{'class':['BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)']})]

    print(raw_data)
    # 4:close 5:Adj close 6:volume
    input_data_open[i] = raw_data[1]
    input_data_high[i] = raw_data[2]
    input_data_low[i] = raw_data[3]
    input_data_close[i] = raw_data[4]
    input_data_adj[i] = raw_data[5]
    input_data_volume[i] = raw_data[6]
    true_today[i] = parse(raw_data[0])

    time.sleep(5)

# close the driver
driver.close()


set1=set(true_today)
days = len(set1)

if days != 1:
    print('錯！')


for b in range(24):
    input_data_volume[b] = input_data_volume[b].replace(',','')

print(input_data_volume)

# # 把input_data寫成sql語法
# sql_open = "INSERT INTO open (`日期`,`VTI`,`VOO`,`VXUS`,`SPY`,`BND`,`IVV`,`BNDX`,`VEA`,`VO`,`VUG`,`VB`,`VWO`,`VTV`,`QQQ`,`BSV`,`BIV`,`VTIP`,`VOE`,`IEF`, `SHY`,`TLT`,`IVE`,`VT`,`GOVT`) VALUES"
# values = "('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"

# sql_open += values % (true_today[0],input_data_open[0],input_data_open[1],input_data_open[2],input_data_open[3],input_data_open[4],
# input_data_open[5],input_data_open[6],input_data_open[7],input_data_open[8],input_data_open[9],
# input_data_open[10],input_data_open[11],input_data_open[12],input_data_open[13],input_data_open[14],
# input_data_open[15],input_data_open[16],input_data_open[17],input_data_open[18],input_data_open[19],
# input_data_open[20],input_data_open[21],input_data_open[22],input_data_open[23])
# print(sql_open)

# # 把input_data寫成sql語法
# sql_high = "INSERT INTO high (`日期`,`VTI`,`VOO`,`VXUS`,`SPY`,`BND`,`IVV`,`BNDX`,`VEA`,`VO`,`VUG`,`VB`,`VWO`,`VTV`,`QQQ`,`BSV`,`BIV`,`VTIP`,`VOE`,`IEF`, `SHY`,`TLT`,`IVE`,`VT`,`GOVT`) VALUES"
# values = "('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"

# sql_high += values % (true_today[0],input_data_high[0],input_data_high[1],input_data_high[2],input_data_high[3],input_data_high[4],
# input_data_high[5],input_data_high[6],input_data_high[7],input_data_high[8],input_data_high[9],
# input_data_high[10],input_data_high[11],input_data_high[12],input_data_high[13],input_data_high[14],
# input_data_high[15],input_data_high[16],input_data_high[17],input_data_high[18],input_data_high[19],
# input_data_high[20],input_data_high[21],input_data_high[22],input_data_high[23])
# print(sql_high)

# # 把input_data寫成sql語法
# sql_low = "INSERT INTO low (`日期`,`VTI`,`VOO`,`VXUS`,`SPY`,`BND`,`IVV`,`BNDX`,`VEA`,`VO`,`VUG`,`VB`,`VWO`,`VTV`,`QQQ`,`BSV`,`BIV`,`VTIP`,`VOE`,`IEF`, `SHY`,`TLT`,`IVE`,`VT`,`GOVT`) VALUES"
# values = "('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"

# sql_low += values % (true_today[0],input_data_low[0],input_data_low[1],input_data_low[2],input_data_low[3],input_data_low[4],
# input_data_low[5],input_data_low[6],input_data_low[7],input_data_low[8],input_data_low[9],
# input_data_low[10],input_data_low[11],input_data_low[12],input_data_low[13],input_data_low[14],
# input_data_low[15],input_data_low[16],input_data_low[17],input_data_low[18],input_data_low[19],
# input_data_low[20],input_data_low[21],input_data_low[22],input_data_low[23])
# print(sql_low)

# # 把input_data寫成sql語法
# sql_adj = "INSERT INTO adj_close (`日期`,`VTI`,`VOO`,`VXUS`,`SPY`,`BND`,`IVV`,`BNDX`,`VEA`,`VO`,`VUG`,`VB`,`VWO`,`VTV`,`QQQ`,`BSV`,`BIV`,`VTIP`,`VOE`,`IEF`, `SHY`,`TLT`,`IVE`,`VT`,`GOVT`) VALUES"
# values = "('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"

# sql_adj += values % (true_today[0],input_data_adj[0],input_data_adj[1],input_data_adj[2],input_data_adj[3],input_data_adj[4],
# input_data_adj[5],input_data_adj[6],input_data_adj[7],input_data_adj[8],input_data_adj[9],
# input_data_adj[10],input_data_adj[11],input_data_adj[12],input_data_adj[13],input_data_adj[14],
# input_data_adj[15],input_data_adj[16],input_data_adj[17],input_data_adj[18],input_data_adj[19],
# input_data_adj[20],input_data_adj[21],input_data_adj[22],input_data_adj[23])
# print(sql_adj)

# 把input_data寫成sql語法
sql_close = "INSERT INTO close (`date`,`VTI`,`VOO`,`VXUS`,`SPY`,`BND`,`IVV`,`BNDX`,`VEA`,`VO`,`VUG`,`VB`,`VWO`,`VTV`,`QQQ`,`BSV`,`BIV`,`VTIP`,`VOE`,`IEF`, `SHY`,`TLT`,`IVE`,`VT`,`GOVT`) VALUES"
values = "('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"

sql_close += values % (true_today[0],input_data_close[0],input_data_close[1],input_data_close[2],input_data_close[3],input_data_close[4],
input_data_close[5],input_data_close[6],input_data_close[7],input_data_close[8],input_data_close[9],
input_data_close[10],input_data_close[11],input_data_close[12],input_data_close[13],input_data_close[14],
input_data_close[15],input_data_close[16],input_data_close[17],input_data_close[18],input_data_close[19],
input_data_close[20],input_data_close[21],input_data_close[22],input_data_close[23])
print(sql_close)


# # 把input_data寫成sql語法
# sql_volume = "INSERT INTO volume (`日期`,`VTI`,`VOO`,`VXUS`,`SPY`,`BND`,`IVV`,`BNDX`,`VEA`,`VO`,`VUG`,`VB`,`VWO`,`VTV`,`QQQ`,`BSV`,`BIV`,`VTIP`,`VOE`,`IEF`, `SHY`,`TLT`,`IVE`,`VT`,`GOVT`) VALUES"
# values = "('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"

# sql_volume += values % (true_today[0],input_data_volume[0],input_data_volume[1],input_data_volume[2],input_data_volume[3],input_data_volume[4],
# input_data_volume[5],input_data_volume[6],input_data_volume[7],input_data_volume[8],input_data_volume[9],
# input_data_volume[10],input_data_volume[11],input_data_volume[12],input_data_volume[13],input_data_volume[14],
# input_data_volume[15],input_data_volume[16],input_data_volume[17],input_data_volume[18],input_data_volume[19],
# input_data_volume[20],input_data_volume[21],input_data_volume[22],input_data_volume[23])
# print(sql_volume)









# 資料庫
db = pymysql.connect("localhost", "root", "esfortest", "etf")
cursor = db.cursor()
# 為了防止重複抓
sql_select = "select * from close where date='%s'" % (true_today[0])
cursor.execute(sql_select)
result_select = cursor.fetchall()

if  result_select == ():
    try:
        # cursor.execute(sql_open)
        # db.commit()
        # print("Data are successfully inserted")
        # cursor.execute(sql_high)
        # db.commit()
        # print("Data are successfully inserted")
        # cursor.execute(sql_low)
        # db.commit()
        # print("Data are successfully inserted")
        # cursor.execute(sql_adj)
        # db.commit()
        # print("Data are successfully inserted")
        cursor.execute(sql_close)
        db.commit()
        print("Data are successfully inserted")
        # cursor.execute(sql_volume)
        # db.commit()
        # print("Data are successfully inserted")
        
    except Exception as e:
        db.rollback()
        print("Exception Occured : ", e)
else:
    print('File already exists')

db.close()



for a in range(len(etf)):
    #for a in range(1):
    
    sql="insert into `etf_close` (`name`,`date`, `close` ) VALUES"
    values = "('%s','%s',%s)"
    sql += values % (etf[a],true_today[a],input_data_close[a])
    print(sql)
    # insert into `etf_close` (`name`,`date`, `close` ) VALUES('GOVT','2020-01-10',26.075001)
    # insert into `etf_close` (`name`,`date`, `close` ) VALUES('VTI','2020/01/09',165.9400)
    db = pymysql.connect("localhost", "root", "esfortest", "etf")
    cursor = db.cursor()
    sql_select = "select * from `etf_close` where (date = '"+str(true_today[a])+"' and name = '"+etf[a] +"')"
    print(sql_select)
    cursor.execute(sql_select)
    result_select = cursor.fetchall()
    
    print(result_select)
    
    
    if  result_select == ():
        try:
            cursor.execute(sql)
            db.commit()
            print("Data are successfully inserted")
        except Exception as e:
            db.rollback()
            print("Exception Occured : ", e)
    else:
        print('File already exists')
    
    db.close()



# for a in range(len(etf)):
#     #for a in range(1):
    
#     sql="insert into `etf_open` (`name`,`date`, `open` ) VALUES"
#     values = "('%s','%s',%s)"
#     sql += values % (etf[a],true_today[a],input_data_open[a])
#     print(sql)
#     # insert into `etf_close` (`name`,`date`, `close` ) VALUES('GOVT','2020-01-10',26.075001)
#     # insert into `etf_close` (`name`,`date`, `close` ) VALUES('VTI','2020/01/09',165.9400)
#     db = pymysql.connect("localhost", "root", "esfortest", "etf")
#     cursor = db.cursor()
#     sql_select = "select * from `etf_open` where (date = '" +str(true_today[a])+"' and name = '"+etf[a] +"')"
#     print(sql_select)
#     cursor.execute(sql_select)
#     result_select = cursor.fetchall()
    
#     print(result_select)
    
    
#     if  result_select == ():
#         try:
#             cursor.execute(sql)
#             db.commit()
#             print("Data are successfully inserted")
#         except Exception as e:
#             db.rollback()
#             print("Exception Occured : ", e)
#     else:
#         print('File already exists')
    
#     db.close()



# for a in range(len(etf)):
#     #for a in range(1):
    
#     sql="insert into `etf_high` (`name`,`date`, `high` ) VALUES"
#     values = "('%s','%s',%s)"
#     sql += values % (etf[a],true_today[a],input_data_high[a])
#     print(sql)
#     # insert into `etf_close` (`name`,`date`, `close` ) VALUES('GOVT','2020-01-10',26.075001)
#     # insert into `etf_close` (`name`,`date`, `close` ) VALUES('VTI','2020/01/09',165.9400)
#     db = pymysql.connect("localhost", "root", "esfortest", "etf")
#     cursor = db.cursor()
#     sql_select = "select * from `etf_high` where (date = '"+str(true_today[a])+"' and name = '"+etf[a] +"')"
#     print(sql_select)
#     cursor.execute(sql_select)
#     result_select = cursor.fetchall()
    
#     print(result_select)
    
    
#     if  result_select == ():
#         try:
#             cursor.execute(sql)
#             db.commit()
#             print("Data are successfully inserted")
#         except Exception as e:
#             db.rollback()
#             print("Exception Occured : ", e)
#     else:
#         print('File already exists')
    
#     db.close()



# for a in range(len(etf)):
#     #for a in range(1):
    
#     sql="insert into `etf_low` (`name`,`date`, `low` ) VALUES"
#     values = "('%s','%s',%s)"
#     sql += values % (etf[a],true_today[a],input_data_low[a])
#     print(sql)
#     # insert into `etf_close` (`name`,`date`, `close` ) VALUES('GOVT','2020-01-10',26.075001)
#     # insert into `etf_close` (`name`,`date`, `close` ) VALUES('VTI','2020/01/09',165.9400)
#     db = pymysql.connect("localhost", "root", "esfortest", "etf")
#     cursor = db.cursor()
#     sql_select = "select * from `etf_low` where (date = '"+str(true_today[a])+"' and name = '"+etf[a] +"')"
#     print(sql_select)
#     cursor.execute(sql_select)
#     result_select = cursor.fetchall()
    
#     print(result_select)
    
    
#     if  result_select == ():
#         try:
#             cursor.execute(sql)
#             db.commit()
#             print("Data are successfully inserted")
#         except Exception as e:
#             db.rollback()
#             print("Exception Occured : ", e)
#     else:
#         print('File already exists')
    
#     db.close()




# for a in range(len(etf)):
#     #for a in range(1):
    
#     sql="insert into `etf_adj_close` (`name`,`date`, `adj_close` ) VALUES"
#     values = "('%s','%s',%s)"
#     sql += values % (etf[a],true_today[a],input_data_adj[a])
#     print(sql)
#     # insert into `etf_close` (`name`,`date`, `close` ) VALUES('GOVT','2020-01-10',26.075001)
#     # insert into `etf_close` (`name`,`date`, `close` ) VALUES('VTI','2020/01/09',165.9400)
#     db = pymysql.connect("localhost", "root", "esfortest", "etf")
#     cursor = db.cursor()
#     sql_select = "select * from `etf_adj_close` where (date = '"+str(true_today[a])+"' and name = '"+etf[a] +"')"
#     print(sql_select)
#     cursor.execute(sql_select)
#     result_select = cursor.fetchall()
    
#     print(result_select)
    
    
#     if  result_select == ():
#         try:
#             cursor.execute(sql)
#             db.commit()
#             print("Data are successfully inserted")
#         except Exception as e:
#             db.rollback()
#             print("Exception Occured : ", e)
#     else:
#         print('File already exists')
    
#     db.close()




# for a in range(len(etf)):
#     #for a in range(1):
    
#     sql="insert into `etf_volume` (`name`,`date`, `volume` ) VALUES"
#     values = "('%s','%s',%s)"
#     sql += values % (etf[a],true_today[a],input_data_volume[a])
#     print(sql)
#     # insert into `etf_close` (`name`,`date`, `close` ) VALUES('GOVT','2020-01-10',26.075001)
#     # insert into `etf_close` (`name`,`date`, `close` ) VALUES('VTI','2020/01/09',165.9400)
#     db = pymysql.connect("localhost", "root", "esfortest", "etf")
#     cursor = db.cursor()
#     sql_select = "select * from `etf_volume` where (date = '"+str(true_today[a])+"' and name = '"+etf[a] +"')"
#     print(sql_select)
#     cursor.execute(sql_select)
#     result_select = cursor.fetchall()
    
#     print(result_select)
    
    
#     if  result_select == ():
#         try:
#             cursor.execute(sql)
#             db.commit()
#             print("Data are successfully inserted")
#         except Exception as e:
#             db.rollback()
#             print("Exception Occured : ", e)
#     else:
#         print('File already exists')
    
#     db.close()

