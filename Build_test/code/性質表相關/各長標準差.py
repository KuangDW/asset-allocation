
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import pymysql
import datetime
from selenium.webdriver.chrome.options import Options
import time
import math
import statistics
from dateutil.relativedelta import relativedelta
# etf = ['VTI','VOO','VXUS','SPY','BND','IVV','BNDX','VEA','VO',
#        'VUG','VB','VWO','VTV','QQQ','BSV','BIV','VTIP','VOE','IEF',
#        'SHY','TLT','IVE','VT','GOVT']

# etf = ['VTI','SPY','BSV','GOVT']

temp = 'KO,PLD,CSX,MMC,AAPL,MSFT,AMZN,FB,GOOGL,GOOG,JNJ,V,PG,NVDA,JPM,HD,MA,UNH,VZ,DIS,ADBE,CRM,PYPL,MRK,NFLX,INTC,T,CMCSA,PFE,BAC,WMT,PEP,ABT,TMO,CSCO,MCD,ABBV,XOM,ACN,COST,NKE,AMGN,AVGO,CVX,MDT,NEE,BMY,UNP,LIN,DHR,QCOM,PM,TXN,LLY,LOW,ORCL,HON,UPS,AMT,IBM,SBUX,C,LMT,MMM,WFC,CHTR,RTX,AMD,FIS,BA,NOW,SPGI,BLK,ISRG,GILD,CAT,MDLZ,INTU,MO,ZTS,CVS,TGT,BKNG,AXP,BDX,VRTX,DE,D,ANTM,EQIX,CCI,APD,SYK,CL,TMUS,CI,GS,DUK,MS,ATVI'
temp_arr = temp.split(',')
stk = []
for i in range(100):
    stk.append(temp_arr[i])

temp = 'VTI,VOO,VXUS,SPY,BND,IVV,BNDX,QQQ,VUG,VEA,VO,1306,VB,VWO,VTV,AGG,GLD,2840,VXF,IEFA,IWF,VNQ,1321,LQD,BSV,IEMG,VIG,EFA,IJH,IJR,IWM,VCIT,VEU,VGT,BIV,XLK,IWD,VCSH,VTIP,USMV,VYM,IVW,IAU,HYG,ITOT,VV,VBR,VBK,IWB,XLV,EEM,TIP,DIA,SCHX,MBB,SHY,IWR,IXUS,IGSB,SCHF,QUAL,SHV,IEF,VT,XLF,GDX,TLT,VOE,MUB,VOT,PFF,SCHB,VGK,EMB,IVE,XLY,SLV,SDY,MDY,GOVT,MINT,XLP,JPST,BIL,IWP,JNK,RSP,VHT,DVY,SCHD,BLV,VGSH,SCHG,ACWI,VMBS,XLU,MTUM,SCHP,DGRO,XLI'
temp = 'SPY,IVV,VTI,VOO,QQQ,AGG,GLD,VEA,IEFA,BND,VWO,VUG,IWF,LQD,IEMG,VTV,EFA,VIG,IJH,IJR,IWM,VCIT,IWD,VGT,XLK,VO,USMV,IAU,VCSH,BNDX,IVW,HYG,VNQ,VB,ITOT,VYM,BSV,VXUS,VEU,EEM,XLV,TIP,IWB,DIA,SCHX,MBB,IXUS,SHY,SHV,IWR,IGSB,IEF,SCHF,QUAL,VV,GDX,XLF,MUB,TLT,PFF,EMB,IVE,SCHB,XLY,SDY,SLV,GOVT,MDY,BIV,XLP,VT,BIL,JPST,MINT,VBR,RSP,JNK,DVY,IWP,SCHD,VGK,ACWI,SCHP,SCHG,XLI,XLU,DGRO,VMBS,VHT,MTUM,IGIB,IEI,VBK,EFAV,XLC,IWS,GSLC,EWJ,FDN,SCHA'
temp_arr = temp.split(',')
etf = []
for i in range(100):
    etf.append(temp_arr[i])


etf = stk + etf

day_of_month = [ 31,28,31, 30,31,30, 31,31,30, 31,30,31]
# 資料庫
db = pymysql.connect("localhost", "root", "esfortest", "etf")
cursor = db.cursor()

rewards = np.zeros(len(etf))
# print(rewards)

# etf = ['XLC','SPY','IVV']

# a=0
# y=5

# today = datetime.date.today()
today = datetime.date(2016,12,1)
for nnnn in  range(2,6):
    if nnnn == 0 :
        nnnn = 10000
    for a in range(len(etf)):
    # for a in range(1):
        print(etf[a])

        sql = "select * from detail where name = '"+etf[a]+"'"
        # print(sql)
        cursor.execute(sql)
        result_select = cursor.fetchall()
        db.commit()

        found  = result_select[0][10]

        vary = relativedelta(today,found)
        y = vary.years

        if y <= 0:
            max_length = -2
            continue
         
        if y >= nnnn :
            y = nnnn
            max_length = y 
        else:
            max_length = -1
        
        # print(result_select)
        # y = result_select[0][9]-1 #成立年限
        # y=10
        # r = np.zeros(y) #放每年的報酬率
        #手續費
        process_fee_percent = 0.1425/100

        #總費用率費(內扣)
        manage_fee = float(result_select[0][5])#從性質表拿總費用率
        manage_fee_day = manage_fee /100/365#每天平均的內扣
        # print(manage_fee)

        #配息率
        div_percent = result_select[0][8]#從性質表拿配息率
        # print(div_percent)

        #取得今天與昨天日期
        
        # today = datetime.date(2019,12,1)
        # print(today)
        yesterday = today - datetime.timedelta(days=2)
        if y !=-1:
            start_date = today - relativedelta(years=y)




        sql = "select * from etf_close where name = '"+etf[a]+"'"
        # print(sql)
        cursor.execute(sql)
        result_select = cursor.fetchall()
        db.commit()
        # print(result_select)
        df = pd.DataFrame(list(result_select))

        if y !=-1:
            while (start_date in list(df[1]))==False and ( datetime.datetime.strptime(str(start_date),"%Y-%m-%d")<datetime.datetime.strptime(str(df[1][len(df)-1]),"%Y-%m-%d") ):
                start_date += datetime.timedelta(days=1)
            # print(start_date)
            if (start_date in list(df[1]))==True:
                start_date_index = list(df[1]).index(start_date) 
            else:
                start_date_index = -1
        else:
            start_date_index = 0

        while (today in list(df[1]))==False and ( datetime.datetime.strptime(str(today),"%Y-%m-%d")<datetime.datetime.strptime(str(df[1][len(df)-1]),"%Y-%m-%d") ):
            today += datetime.timedelta(days=1)
        # print(start_date)
        if (today in list(df[1]))==True:
            today_index = list(df[1]).index(today) 
        else:
            today_index = -2

        df = df[start_date_index:today_index+1]
        df = df.reset_index(drop=True)


        m_first_day_index=[]
        m_first_day=[]
        m_first_day_close=[]

        for i in range(0,len(df)-1):
            date1=df[1][i]
            date2=df[1][i+1]
            if date2.day < date1.day:
                m_first_day.append(date2)
                m_first_day_index.append(i+1)
                m_first_day_close.append(df[2][i+1])

        # print(m_first_day)
        # print(m_first_day_index)
        # print(m_first_day_close)
        # news = pd.concat([news, pd.DataFrame(heads,columns=['head'])],axis=1)
        df2 = pd.DataFrame(m_first_day,columns=['date'])
        df2 = pd.concat([df2,pd.DataFrame(m_first_day_close,columns=['close'])],axis=1)


        #每月投入資金
        money=[0]
        unit=[0]
        date=[df2['date'][0]]
        input_month = 1000
        now_money=0
        now_unit=0
        for i in range(len(df2)-1):
            input_money=input_month#投入的錢=每月投入金額
            next_close = float(df2['close'][i+1])
            now_close = float(df2['close'][i])
            if df2['date'][i].month==1:#看是否為一月 若是則要投入配息 加進投入的錢裡
                div = now_money*div_percent #配息=目前持有總資金*殖利率
                input_money += div  

            process_fee = input_money*process_fee_percent #手續費=投入金額*手續費趴數 
            input_money -= process_fee 
            buy_unit = input_money/now_close 
            now_unit += buy_unit
            now_money = now_unit * next_close -( manage_fee_day * now_money * day_of_month[ df2['date'][i].month-1 ])
            now_unit = now_money / next_close
            money.append(now_money)
            unit.append(now_unit)
            date.append(df2['date'][i+1])

        df3 = pd.concat([pd.DataFrame(date,columns=['date']),pd.DataFrame(money,columns=['money'])],axis=1)
        # df3


        # df3 = pd.concat([pd.DataFrame(date,columns=['date']),pd.DataFrame(money,columns=['money'])],axis=1)
        df3['reward']=0
        for i in range(len(df3)):
            # df3.loc[i,'reward']=(df3['money'][i]-df3['money'][i-1])/df3['money'][i-1]
            df3.loc[i,'reward']=(df3['money'][i]-i*input_month)/(i*input_month)

        # df3



        std_dev_m = statistics.stdev(df3['reward'][2:])
        avg_m = statistics.mean(df3['reward'][2:])

        # math.pow( x, y ) x的y次方
        v1_std = std_dev_m * math.pow( 12, 0.5 )
        # v2_std = math.pow( ( math.pow( (math.pow(std_dev_m,2)) + (math.pow( 1+avg_m ,2 )) ,12)- (math.pow( 1+avg_m ,24 )) ),0.5 )

        print(v1_std)
        # print(v2_std)

        # sql= "UPDATE `各長年化值` SET `std` ='%s' WHERE (`name` ='%s' and `year` ='%s' and `length` ='%s')" % (str(v1_std),str(etf[a]),str(today.year),str(y))
        # cursor.execute(sql)
        # db.commit()


        try:
            # sql = "INSERT INTO `各長年化值`(`year`,`length`,`name`,`std`) VALUES"
            # values = "('%s','%s','%s','%s')"
            # sql += values % (str(today.year),str(max_length),str(etf[a]),str(v1_std))
            sql =  "UPDATE `各長年化值` SET `std` ='%s' WHERE (`name` ='%s' and `year` ='%s' and `length` ='%s')" % (str(v1_std),str(etf[a]),str(today.year),str(max_length))
            cursor.execute(sql)
            db.commit()
        except Exception as e:
            db.rollback()

db.close()
