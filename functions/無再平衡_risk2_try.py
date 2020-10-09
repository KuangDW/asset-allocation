#%%
#from selenium import webdriver
#from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import pymysql
import datetime
#from selenium.webdriver.chrome.options import Options
import time
from dateutil.relativedelta import relativedelta
import sys


#%%
year = ["1990","1991","1992","1993","1994","1995","1996","1997","1998","1999",
        "2000","2001","2002","2003","2004","2005","2006","2007","2008","2009",
        "2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"]
month = ["00","01","02","03","04","05","06","07","08","09","10","11","12"]
day = ["00","01","02","03","04","05","06","07","08","09","10",
            "11","12","13","14","15","16","17","18","19","20",
            "21","22","23","24","25","26","27","28","29","30","31"]
day_of_month = [ 31,28,31, 30,31,30, 31,31,30, 31,30,31]

# etf=['VOO', 'VOE', 'VT', 'VEA']
# weight=[0.25, 0.25, 0.25, 0.25]
# # 資料庫
# name = 'max'
# #密碼
# password = '1234'




username = sys.argv[1]
password = sys.argv[2]



db = pymysql.connect("localhost", "root", "esfortest", "etf")
cursor = db.cursor()
sql = "select * from `user_datat` where (name = '"+ username +"' and id = '" + password +"')"
cursor.execute(sql)
result_select = cursor.fetchall()
db.commit()
start_date = result_select[0][3]
final_date = start_date
etf = result_select[0][4].split(' ')
#取得今天與昨天日期
today = datetime.date.today()
#print(today)
yesterday = today - datetime.timedelta(days=3)
#print(yesterday)

# sql = 'select date FROM `close`'
# cursor.execute(sql)
# result_select = cursor.fetchall()
# db.commit()
# # print(result_select[-1][0])
# todayyy = result_select[-1][0]
input_money_record=[]
money_record = []
ratio_record = []
every_money_record = []
date_record = []
#%%
sql = 'select date,'
for a in range(len(etf)-1):
    sql+=(etf[a]+',')
sql+= etf[-1] +' FROM `close`'
# print(sql)
cursor.execute(sql)
result_select = cursor.fetchall()
db.commit()
# print(result_select)
df = pd.DataFrame(list(result_select))
df = df.rename(columns={0:'date'})
for a in range(len(etf)):
    df = df.rename(columns={a+1:etf[a]})
# print(df)

# i=0
# while(True):
#     have_nan = True
#     for a in range(len(etf)):
#         if np.isnan(df[etf[a]][i])==True: #是空的
#             have_nan = False
#             break
#     if have_nan==False:
#         df = df.drop([i],axis=0)
#         i+=1
#     else:
#         break

for i in range(len(df)):
    have_nan = True
    for a in range(len(etf)):
        if np.isnan(df[etf[a]][i])==True: #是空的
            have_nan = False
            break
    if have_nan==False:
        df = df.drop([i],axis=0)





#今天之前的最後交易日
todayyy = today
# todayyy = datetime.date(2020, 8, 16)
df = df.reset_index(drop=True)
while (todayyy in list(df['date']))==False and ( datetime.datetime.strptime(str(todayyy),"%Y-%m-%d")>datetime.datetime.strptime(str(df['date'][0]),"%Y-%m-%d") ):
    todayyy -= datetime.timedelta(days=1)
# print(start_date)
if (todayyy in list(df['date']))==True:
    todayyy_index = list(df['date']).index(todayyy) 
else:
    todayyy_index = 0
df = df[:todayyy_index+1]
df = df.reset_index(drop=True)

#%%
m_moneys=[]
m_units=[]
first_do_allocation=1
# while((final_date+ relativedelta(years=1))<todayyy):
while((final_date)<todayyy):
    sql = "select * from `user_datat` where (name = '"+ username +"' and id = '" + password +"')"
    # db = pymysql.connect("localhost", "root", "esfortest", "etf")
    # cursor = db.cursor()
    # sql = 'SELECT * FROM `user_data`'
    cursor.execute(sql)
    result_select = cursor.fetchall()
    db.commit()
    etf = result_select[0][4].split(' ')
    weight = result_select[0][5].split(' ')
    for i in range(len(weight)):
        weight[i] = float(weight[i])
    
    rewards = np.zeros(len(etf))
    total_unit = np.zeros(len(etf))
    final_money = np.zeros(len(etf))
    total_cost = np.zeros(len(etf))
    moneys=[]
    units=[]
    
    #交易日
    transcation_day = result_select[0][2].day
    div_month = result_select[0][2].month
    start_allocation = result_select[0][2]
    # print(rewards)
    a=0
    
    #每月投入資金
    # input_month_total = 1000
    input_month_total = float(result_select[0][10])/12
    #目前分別資產
    # first_input_total = [1600,1800,2100,1700] 
    first_input_money = float(result_select[0][9])
    
    # first_input_total = []
    # for i in range(len(weight)):
    #     first_input_total.append(first_input_money*weight[i])
    
    first_input_total = result_select[0][6].split('  ')
    for i in range(len(first_input_total)):
        first_input_total[i] = float(first_input_total[i])
    
    # first_input_total=7200
    start_date = result_select[0][3]
    
    #再平衡區
    balence_zone = float(result_select[0][11])
    #可容忍區
    tolerance_zone = float(result_select[0][12])
    #調整方式
    mode = int(result_select[0][13])

    if first_do_allocation==1:
        input_money_record.append(first_input_money)
        first_do_allocation=0

    # sql = 'select date,'
    # for a in range(len(etf)-1):
    #     sql+=(etf[a]+',')
    # sql+= etf[-1] +' FROM `close`'
    # # print(sql)
    # cursor.execute(sql)
    # result_select = cursor.fetchall()
    # db.commit()
    # # print(result_select)
    # df = pd.DataFrame(list(result_select))
    # df = df.rename(columns={0:'date'})
    # for a in range(len(etf)):
    #     df = df.rename(columns={a+1:etf[a]})
    # # print(df)
    
    
    # i=0
    # while(True):
    #     have_nan = True
    #     for a in range(len(etf)):
    #         if np.isnan(df[etf[a]][i])==True: #是空的
    #             have_nan = False
    #             break
    #     if have_nan==False:
    #         df = df.drop([i],axis=0)
    #         i+=1
    #     else:
    #         break
    
    # df = df.reset_index(drop=True)

    while (start_date in list(df['date']))==False and ( datetime.datetime.strptime(str(start_date),"%Y-%m-%d")<datetime.datetime.strptime(str(df['date'][len(df)-1]),"%Y-%m-%d") ):
        start_date += datetime.timedelta(days=1)
    # print(start_date)
    if (start_date in list(df['date']))==True:
        start_date_index = list(df['date']).index(start_date) 
    else:
        start_date_index = -1
    # start_close = df[etf[a]][start_date_index]
    # print(start_close)

    # final_date = start_date + relativedelta(years=1)
    final_date = todayyy
    final_date_index = -1
    # final_date = datetime.date(final_date.year,final_date.month,transcation_day)
    # while (final_date in list(df['date']))==False and ( datetime.datetime.strptime(str(final_date),"%Y-%m-%d")<datetime.datetime.strptime(str(df['date'][len(df)-1]),"%Y-%m-%d") ):
    #     final_date += datetime.timedelta(days=1)
    # # print(final_date)
    # if (final_date in list(df['date']))==True:
    #     final_date_index = list(df['date']).index(final_date) 
    # else:
    #     # break
    #     final_date_index = -1 


    # final_date_index = start_date_index+1
    # final_date = df['date'][final_date_index]
    # final_close = df[etf[a]][final_date_index]
    # print(final_close)
    
    df2 = df[start_date_index:final_date_index]
    df2 = df2.reset_index(drop=True)

    final_moneys = []
    for a in range(len(etf)):
    # for a in range(1):
    
        #從性質表抓、總費用率、配息率
        sql = "select * from detail where name = '"+etf[a]+"'"
        # print(sql)
        cursor.execute(sql)
        result_select = cursor.fetchall()
        db.commit()
        # print(result_select)
    
        #手續費
        process_fee_percent = 0.1425/100
        
        #總費用率費(內扣)
        manage_fee = float(result_select[0][5])#從性質表拿總費用率
        manage_fee_day = manage_fee /100/252#每天平均的內扣
        # print(manage_fee)
        
        #配息率
        div_percent = result_select[0][8]#從性質表拿配息率
        # print(div_percent)
    
    
        start_month = start_date.month

        money =    []
        unit =     []
    
        input_month = input_month_total*weight[a]
        first_input = first_input_total[a]
        start_unit = first_input/df2[etf[a]][0]
        
        
        unit.append(start_unit)
        money.append(first_input)
            
    
        now_month = df2['date'][0].month
    
        # already_input = 0  
        for i in range(len(df2)):
    
            now_money = money[i]#昨天資產
            if i == 0:
                # print(df2['date'][i],'i=0')
                pre_day = df['date'][start_date_index-1].day
            else:
                pre_day = df2['date'][i-1].day
            now_day = df2['date'][i].day
            # next_day = df['date'][final_date_index].day
            # pre_month = now_month
            now_month = df2['date'][i].month
            now_close = df2[etf[a]][i]
            if a==0:
                date_record.append(df2['date'][i])

            # if (pre_day<transcation_day and now_day>=transcation_day):#每月投入錢
            if (pre_day<transcation_day and now_day>=transcation_day) or (pre_day>now_day and now_day>=transcation_day):
                if a==0:
                    if len(input_money_record)==0:
                        #print(df2['date'][i],first_input_money)
                        input_money_record.append(first_input_money)
                    else:
                        #print(df2['date'][i],input_money_record[-1],input_month_total)
                        input_money_record.append(input_money_record[-1]+input_month_total)
                # already_input = 1
                if now_month == div_month:#投入配息
                    buy_unit = (input_month + now_money*div_percent )/now_close
                    # print('month + div input',df2['date'][i],pre_day,transcation_day,now_day)
                else:
                    buy_unit = input_month/now_close
                    # print('month input',df2['date'][i],pre_day,transcation_day,now_day)
                
                now_unit = unit[i] + buy_unit #昨天的單位數+今天買的
                now_money = now_unit * now_close - manage_fee_day
                now_unit = now_money/now_close
                money.append(now_money) #將目前持有資金金額存入陣列以便觀察
                unit.append(now_unit) #將目前持有單位數存入陣列以便觀察
            else:
                if a==0:
                    if len(input_money_record)==0:
                        # print(df2['date'][i],first_input_money)
                        input_money_record.append(first_input_money)
                    else:
                        #print(df2['date'][i],input_money_record[-1])
                        input_money_record.append(input_money_record[-1])
                now_unit = unit[i] #今天的單位數=昨天的單位數
                now_money = now_unit * now_close - manage_fee_day
                now_unit = now_money/now_close
                money.append(now_money) #將目前持有資金金額存入陣列以便觀察
                unit.append(now_unit) #將目前持有單位數存入陣列以便觀察
            # print(df2['date'][i],now_money,now_unit)
            
        final_money = money[-1]
        moneys.append(money)
        units.append(unit)
        final_moneys.append(final_money)
        

    m_moneys.append(moneys)
    # m_moneys = m_moneys+moneys
    # m_units.append(units)
    # print(final_moneys)
    # print(sum(final_moneys))
    
    #最後的各資產
    sum_of_final_money = sum(final_moneys)

    # 調整前list
    before_adj_ratio = []
    for i in range(len(final_moneys)):
        before_adj_ratio.append(final_moneys[i]/sum_of_final_money)
    # print(total_cost)
    
    balence_array = []
    for i in range(len(weight)):
        balence_array.append(weight[i]*balence_zone)
    up_range = []
    for i in range(len(weight)):
        up_range.append(weight[i]+balence_array[i])
    down_range = []
    for i in range(len(weight)):
        down_range.append(weight[i]-balence_array[i])
    tolerance_array = []
    for i in range(len(weight)):
        tolerance_array.append(weight[i]*tolerance_zone)
    up_range_tolerance = []
    for i in range(len(weight)):
        up_range_tolerance.append(weight[i]+tolerance_array[i])
    down_range_tolerance = []
    for i in range(len(weight)):
        down_range_tolerance.append(weight[i]-tolerance_array[i])
    
    
    
    sell_buy = []
    # 調整後list
    after_adj_ratio = []
    # mode = 1
    if mode == 1 :
        for i in range(len(before_adj_ratio)):
            if (before_adj_ratio[i] > up_range[i] or before_adj_ratio[i] < down_range[i]):
                sell_buy.append(weight[i]-before_adj_ratio[i])
                after_adj_ratio.append(weight[i]) 
            else:
                sell_buy.append(0)
                after_adj_ratio.append(before_adj_ratio[i]) 
    elif mode == 2:
        for i in range(len(before_adj_ratio)):
            if (before_adj_ratio[i] > up_range[i]):
                sell_buy.append(up_range[i]-before_adj_ratio[i])
                after_adj_ratio.append(up_range[i]) 
            elif (before_adj_ratio[i] < down_range[i]):
                sell_buy.append(down_range[i]-before_adj_ratio[i])
                after_adj_ratio.append(down_range[i]) 
            else:
                sell_buy.append(0)
                after_adj_ratio.append(before_adj_ratio[i])
    elif mode == 3:
        for i in range(len(before_adj_ratio)):
            if (before_adj_ratio[i] > up_range[i]):
                sell_buy.append(up_range_tolerance[i]-before_adj_ratio[i])
                after_adj_ratio.append(up_range_tolerance[i]) 
            elif (before_adj_ratio[i] < down_range[i]):
                sell_buy.append(down_range_tolerance[i]-before_adj_ratio[i])
                after_adj_ratio.append(down_range_tolerance[i]) 
            else:
                sell_buy.append(0)
                after_adj_ratio.append(before_adj_ratio[i]) 
    new_asset = []
    for i in range(len(first_input_total)):
        new_asset.append(after_adj_ratio[i]*sum_of_final_money)
    # print(before_adj_ratio)
    # print(after_adj_ratio)
    # print(final_moneys)
    # print(new_asset)
    # print(sell_buy)
    money_record.append(round(sum_of_final_money,5))

    new_asset = str(new_asset)
    new_asset = new_asset.replace(',',' ')
    new_asset = new_asset.replace('[','')
    new_asset = new_asset.replace(']','')
    
    if final_date>=todayyy:
        break    
    sql = "UPDATE user_datat SET last_money = '"+ str(new_asset) +"' WHERE name = '" +username+"'; "
    # print(sql)
    cursor.execute(sql)
    result_select = cursor.fetchall()
    db.commit()
    
    sql = "UPDATE user_datat SET last_time = '"+ str(final_date) +"' WHERE name = '" +username+"'; "
    # print(sql)
    cursor.execute(sql)
    result_select = cursor.fetchall()
    db.commit()
    sell_buy = str(sell_buy)
    sell_buy = sell_buy.replace(',',' ')
    sell_buy = sell_buy.replace('[','')
    sell_buy = sell_buy.replace(']','') 
    sql = "UPDATE user_datat SET sell_buy = '"+ str(sell_buy) +"' WHERE name = '" +username+"'; "
    # print(sql)
    cursor.execute(sql)
    result_select = cursor.fetchall()
    db.commit()
    
    after_adj_ratio = str(after_adj_ratio)
    after_adj_ratio = after_adj_ratio.replace(',',' ')
    after_adj_ratio = after_adj_ratio.replace('[','')
    after_adj_ratio = after_adj_ratio.replace(']','') 
    sql = "UPDATE user_datat SET last_ratio = '"+ str(after_adj_ratio) +"' WHERE name = '" +username+"'; "
    # print(sql)
    cursor.execute(sql)
    result_select = cursor.fetchall()
    db.commit()

date_record.append(df['date'][len(df)-1])

# %%
mmm_total=[]
# m_moneys[0]:第一個月的資料
# m_moneys[0][0]:第一個月第一個etf的資料
for j in range(len(m_moneys[0])):#第j個etf
    mmm=[]
    for i in range(len(m_moneys)):#第i個月
        if i==0:
            mmm = mmm + m_moneys[i][j]
        else:
            mmm = mmm + m_moneys[i][j][1:]
    mmm_total.append(mmm)

# print(len(mmm_total[0]))
# print(len(date_record))
date_record_df = pd.DataFrame(date_record,columns=['date'])
# %%
day_ratio_record = []
sum_money_record = []
for i in range(len(mmm_total[0])):
    ratiosss = []
    sum_money = 0
    for j in range(len(etf)):
        sum_money += mmm_total[j][i]
    sum_money_record.append(sum_money)
    for j in range(len(etf)):
        r = mmm_total[j][i]/sum_money
        ratiosss.append(r)
    day_ratio_record.append(ratiosss)

df = pd.DataFrame(day_ratio_record)
df = pd.concat([df, date_record_df],axis=1)
df_result = pd.concat([df, pd.DataFrame(sum_money_record,columns=['sum'])],axis=1)
df_result = pd.concat([df_result, pd.DataFrame(input_money_record,columns=['in_sum'])],axis=1)



# %%

# import matplotlib.pyplot as plt
# plt.plot(df_result['date'],df_result['sum'])
# plt.show()


# for i in range(len(etf)):
#     plt.plot(df['date'],df[i])
# plt.show()

df_result['sum_change']=0
# money_change = []
for i in range(len(df_result)):
    df_result.loc[i,'sum_change'] = df_result['sum'][i]/df_result['in_sum'][i]


# %%
# date_record_df = pd.DataFrame(date_record,columns=['date'])
# df = (pd.DataFrame(r)).T
# df = pd.concat([df, date_record_df],axis=1)
# df_result = pd.concat([df, pd.DataFrame(money_record,columns=['sum'])],axis=1)

first_date = df_result['date'][0]
final_date = df_result['date'][len(df_result)-1]

db = pymysql.connect("localhost", "root", "esfortest", "etf")
cursor = db.cursor()
sql = 'select date,'
for a in range(len(etf)-1):
    sql+=(etf[a]+',')
sql+= etf[-1] +' FROM `close`'
# print(sql)
# sql = "select * from close"
cursor.execute(sql)
result_select = cursor.fetchall()
db.commit()
df = pd.DataFrame(list(result_select))
# df = df.drop([0],axis=1)
df = df.rename(columns={0:'date'})
for a in range(len(etf)):
    df = df.rename(columns={a+1:etf[a]})
# print(df)
first_date_index = list(df['date']).index(first_date)
final_date_index = list(df['date']).index(final_date)
df2 = df[first_date_index:final_date_index+1]
# i=0
# while(True):
#     have_nan = True
#     for a in range(len(etf)):
#         if np.isnan(df[etf[a]][i])==True: #是空的
#             have_nan = False
#             break
#     if have_nan==False:
#         df = df.drop([i],axis=0)
#         i+=1
#     else:
#         break

df2 = df2.reset_index(drop=True)
# print(df2)
#%%
# 平均股價
for i in range(len(df2)):
    if np.isnan(df2[etf[0]][i])==True: #是空的
        df2 = df2.drop([i],axis=0)
df2 = df2.reset_index(drop=True)

df2['avg'] = 0
# df2 = df2.drop(['avg'],axis=1)
for i in range(len(df2['avg'])):
    for a in range(len(etf)):
        df2.loc[i,'avg'] += df2[etf[a]][i]*df_result[a][i]


# %%
import statistics
import math
# 漲幅
establish_risk=np.zeros(4)

df2['day_return'] = 0 
for i in range(len(df2)-1):
    df2.loc[i+1,'day_return'] = (df2['avg'][i+1] - df2['avg'][i])/df2['avg'][i]
# print(df2)

# 無風險利率
risk_free_return = 0.01/365
# risk_free_return = 0

avg_return = statistics.mean(df2['day_return'][1:])
# print(avg_return)

# 標準差
std_dev = statistics.stdev(df2['day_return'][1:])* math.sqrt(252)
# print(std_dev)#0.1757400215841394
establish_risk[0]=std_dev*100


# 資產標準差
std_dev_money = statistics.stdev(df_result['sum_change'])* math.sqrt(252)
# print(std_dev)#0.1757400215841394
establish_risk[3]=std_dev_money


# 夏普值
sharpe = (avg_return-risk_free_return) / std_dev * math.sqrt(252)
# sharpe = (avg_return) / std_dev * math.sqrt(252)
# print(sharpe)#0.5267990017907497
establish_risk[1]=sharpe

# 最大回徹率
# df3 = df2
df2['max']=0
s1 = df2['avg']
for i in range(len(df2)):
    df2.loc[i,'max'] = s1[0:i+1].max() 

df2['dd'] = 0
df2['dd'] = 1-(df2['avg']/df2['max'])

mdd = df2['dd'].max()
establish_risk[2]=mdd

# print(establish_risk)

# %%
df2['sharpe']=0
df2['std_dev']=0
df_result['money_std']=0
# df2['mdd']=0
mdds=[]
for i in range(21):
    mdds.append(0)

for i in range(21,len(df2)):
    df3 = df2[i-21:i]
    df3 = df3.reset_index(drop=True)
    avg_return = statistics.mean(df3['day_return'][1:])
    std_dev = statistics.stdev(df3['day_return'][1:])* math.sqrt(252)
    sharpe = (avg_return-risk_free_return) / std_dev * math.sqrt(252)
    df2.loc[i,'std_dev']=round(std_dev*100,3) 
    df2.loc[i,'sharpe']=round(sharpe,5) 
    df4=df_result[i-21:i]
    df_result.loc[i,'money_std'] = statistics.stdev(df4['sum_change'])* math.sqrt(252)
    # df2['std_dev'][i] = round(std_dev*100,3)   
    # df2['sharpe'][i] = round(sharpe,5) 
    # print(df2['std_dev'][i],df2['sharpe'][i])
    # print(round(std_dev*100,3),round(sharpe,5))
    df3['max']=0
    s1 = df3['avg']
    for i in range(len(df3)):
        df3.loc[i,'max'] = s1[0:i+1].max() 
    df3['dd'] = 0
    df3['dd'] = 1-(df3['avg']/df3['max'])
    mdd = df3['dd'].max()
    mdds.append(mdd)
    # df2.loc[i,'mdd']=round(mdd,5)
    # print(df2['mdd'][i]) 
df2 = pd.concat([df2, pd.DataFrame(mdds,columns=['mdd'])],axis=1)
# %%

df_final = df2[['date','sharpe','std_dev','mdd']]

# %%
# plt.plot(df_final['date'],df_final['sharpe'])
# plt.show()
# plt.plot(df_final['date'],df_final['std_dev'])
# plt.show()
# plt.plot(df_final['date'],df_final['mdd'])
# plt.show()

# %%# %%
date_list=[]
result_date_list = list(df_final['date'])
for i in range(len(result_date_list)):
    if i%21 == 0 or i==len(result_date_list)-1:
        date_list.append(result_date_list[i].strftime('%Y%m'))
    # result_date_list[i] = result_date_list[i].strftime('%Y%m%d')
# print(result_date_list)
# result_date = ' '.join(result_date_list)
result_date_list = ' '.join(date_list)
print(result_date_list)

# date_list=[]
# date_list1 = list(df2['date'])
# for i in range(len(date_list1)):
#     if i%21 == 0 or i==len(date_list1)-1:
#         date_list.append(date_list1[i].strftime('%Y%m'))
# result_date_list = ' '.join(date_list)

# %%
money_list=[]
sum_money_list = list(df_result['sum'])
for i in range(len(sum_money_list)):
    if i%21 == 0 or i==len(sum_money_list)-1:
        money_list.append(str(round(sum_money_list[i],3)))
    # sum_money_list[i] = str(round(sum_money_list[i],3))
# print(sum_money_list)
result_sum_money = ' '.join(money_list)
print(result_sum_money)

# %%

for a in range(len(etf)):
    print_raio_list = list(df_result[a])
    ratio_list=[]
    for i in range(len(print_raio_list)):
        if i%21 == 0 or i==len(print_raio_list)-1:
            ratio_list.append(str(round(print_raio_list[i],5)))
            # print_raio_list[i] = str(round(print_raio_list[i],5))
    result_ratio = ' '.join(ratio_list)
    print(result_ratio)
# %%
sharpe_list=[]
result_sharpe_list = list(df_final['sharpe'])
for i in range(len(result_sharpe_list)):
    if i%21 == 0 or i==len(result_sharpe_list)-1:
        sharpe_list.append(str(round(result_sharpe_list[i],5)))
    # result_sharpe_list[i] = str(round(result_sharpe_list[i],5))
# print(result_sharpe_list)
result_sharpe = ' '.join(sharpe_list)
print(result_sharpe)

# %%
std_list=[]
result_std_dev_list = list(df_final['std_dev'])
for i in range(len(result_std_dev_list)):
    if i%21 == 0 or i==len(result_std_dev_list)-1:
        std_list.append(str(round(result_std_dev_list[i],3)))
    # result_std_dev_list[i] = str(round(result_std_dev_list[i],3))
# print(result_std_dev_list)
result_std_dev = ' '.join(std_list)
print(result_std_dev)

# %%
mdd_list=[]
result_mdd_list = list(df_final['mdd'])
for i in range(len(result_mdd_list)):
    if i%21 == 0 or i==len(result_mdd_list)-1:
        mdd_list.append(str(round(result_mdd_list[i],5)))
    # result_mdd_list[i] = str(round(result_mdd_list[i],5))
# print(result_mdd_list)
result_mdd = ' '.join(mdd_list)
print(result_mdd)


# %%

establish_risk_list = list(establish_risk)
for i in range(len(establish_risk_list)):
    establish_risk_list[i] = str(round(establish_risk_list[i],5))
# print(establish_risk_list)
result_establish_risk = ' '.join(establish_risk_list)
print(result_establish_risk)


# %%
money_dev_list=[]
sum_money_dev_list = list(df_result['money_std'])
for i in range(len(sum_money_dev_list)):
    if i%21 == 0 or i==len(sum_money_dev_list)-1:
        money_dev_list.append(str(round(sum_money_dev_list[i],3)))
    # sum_money_list[i] = str(round(sum_money_list[i],3))
# print(sum_money_list)
result_sum_money_dev = ' '.join(money_dev_list)
print(result_sum_money_dev)


# str_data1 = 'C:/Users/User/Downloads/資產配置/無再平衡1.csv'
# str_data2 = 'C:/Users/User/Downloads/資產配置/無再平衡2.csv'
# df_result.to_csv(str_data1, index= False)
# df_final.to_csv(str_data2, index= False)

# %%
# start_time = datetime.date(2014,1,2)
# last_time = datetime.date(2014,1,2)
# sql_final_name = 'QQQ MBB XLI XLK VGT FDN'
# sql_final_w = '0.16667 0.16667 0.16667 0.16667 0.16667 0.16667'
# last_money = '25000  25000  25000  25000  25000  25000'
# sql_expect_reward = 0.07734729178524269
# sql_max_reward = '7.887%'
# first_input = 150000
# in_per_year = 120000
# sql_final_temp = '0 0 0 0 0 0 0 0 0 0'
# sql_min_risk = 0.186
# sql_final_reward = 0
# sql_final_div = 0
# new_asset = '0.16667 0.16667 0.16667 0.16667 0.16667 0.16667'
# password = '1234'
# db = pymysql.connect("localhost", "root", "esfortest", "etf")
# cursor = db.cursor()
# sql= "UPDATE user_data SET start_time='%s', last_time='%s', target='%s', weight='%s', last_money='%s', expect_reward='%s', reward='%s', first_time='%s', in_per_year='%s', balence='%s', tolerance='%s', type='%s', sell_buy='%s', risk='%s', nodiv_reward='%s', dividend='%s', last_ratio='%s' WHERE id='%s'" % (str(start_time),str(last_time),str(sql_final_name),str(sql_final_w),str(last_money),str(sql_expect_reward),str(sql_max_reward),str(first_input),str(in_per_year),'0.2','0.1','3',str(sql_final_temp),str(sql_min_risk),str(sql_final_reward),str(sql_final_div),str(new_asset),str(password))
# try:
#     cursor.execute(sql)
#     db.commit()
#     # print("Data are successfully inserted")
# except Exception as e:
#     db.rollback()
#     # print("Exception Occured : ", e)
# db.close()




# name = 'max'
# password = '1234'
db = pymysql.connect("localhost", "root", "esfortest", "etf")
cursor = db.cursor()
sql = "select * from `user_datatr` where (name = '"+ username +"' and id = '" + password +"')"
cursor.execute(sql)
result_select = cursor.fetchall()
db.commit()

start_time = result_select[0][2]
last_time = result_select[0][3]
sql_final_name =  result_select[0][4]
sql_final_w = result_select[0][5]
last_money = result_select[0][6]
sql_expect_reward = result_select[0][7]
sql_max_reward = result_select[0][8]
first_input = result_select[0][9]
in_per_year = result_select[0][10]
sql_final_temp = '0 0 0 0 0 0 0 0 0 0'
sql_min_risk = result_select[0][15]
sql_final_reward = 0
sql_final_div = 0
new_asset = result_select[0][24]


sql= "UPDATE user_datat SET start_time='%s', last_time='%s', target='%s', weight='%s', last_money='%s', expect_reward='%s', reward='%s', first_time='%s', in_per_year='%s', balence='%s', tolerance='%s', type='%s', sell_buy='%s', risk='%s', nodiv_reward='%s', dividend='%s', last_ratio='%s' WHERE id='%s'" % (str(start_time),str(last_time),str(sql_final_name),str(sql_final_w),str(last_money),str(sql_expect_reward),str(sql_max_reward),str(first_input),str(in_per_year),'0.2','0.1','3',str(sql_final_temp),str(sql_min_risk),str(sql_final_reward),str(sql_final_div),str(new_asset),str(password))
cursor.execute(sql)
db.commit()
db.close()
# %%
