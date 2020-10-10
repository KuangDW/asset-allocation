import sys
import pandas as pd
import numpy as np
import pymysql
import math
import statistics
import time
import datetime
from itertools import combinations, permutations
from scipy.special import comb, perm
import numpy_financial as npf
from dateutil.relativedelta import relativedelta


starttime = datetime.datetime.now()
temp = 'KO,PLD,CSX,MMC,AAPL,MSFT,AMZN,FB,GOOGL,GOOG,JNJ,V,PG,NVDA,JPM,HD,MA,UNH,VZ,DIS,ADBE,CRM,PYPL,MRK,NFLX,INTC,T,CMCSA,PFE,BAC,WMT,PEP,ABT,TMO,CSCO,MCD,ABBV,XOM,ACN,COST,NKE,AMGN,AVGO,CVX,MDT,NEE,BMY,UNP,LIN,DHR,QCOM,PM,TXN,LLY,LOW,ORCL,HON,UPS,AMT,IBM,SBUX,C,LMT,MMM,WFC,CHTR,RTX,AMD,FIS,BA,NOW,SPGI,BLK,ISRG,GILD,CAT,MDLZ,INTU,MO,ZTS,CVS,TGT,BKNG,AXP,BDX,VRTX,DE,D,ANTM,EQIX,CCI,APD,SYK,CL,TMUS,CI,GS,DUK,MS,ATVI'
temp_arr = temp.split(',')
stk = []
for i in range(100):
    stk.append(temp_arr[i])

# temp = 'VTI,VOO,VXUS,SPY,BND,IVV,BNDX,QQQ,VUG,VEA,VO,1306,VB,VWO,VTV,AGG,GLD,2840,VXF,IEFA,IWF,VNQ,1321,LQD,BSV,IEMG,VIG,EFA,IJH,IJR,IWM,VCIT,VEU,VGT,BIV,XLK,IWD,VCSH,VTIP,USMV,VYM,IVW,IAU,HYG,ITOT,VV,VBR,VBK,IWB,XLV,EEM,TIP,DIA,SCHX,MBB,SHY,IWR,IXUS,IGSB,SCHF,QUAL,SHV,IEF,VT,XLF,GDX,TLT,VOE,MUB,VOT,PFF,SCHB,VGK,EMB,IVE,XLY,SLV,SDY,MDY,GOVT,MINT,XLP,JPST,BIL,IWP,JNK,RSP,VHT,DVY,SCHD,BLV,VGSH,SCHG,ACWI,VMBS,XLU,MTUM,SCHP,DGRO,XLI'
temp = 'SPY,IVV,VTI,VOO,QQQ,AGG,GLD,VEA,IEFA,BND,VWO,VUG,IWF,LQD,IEMG,VTV,EFA,VIG,IJH,IJR,IWM,VCIT,IWD,VGT,XLK,VO,USMV,IAU,VCSH,BNDX,IVW,HYG,VNQ,VB,ITOT,VYM,BSV,VXUS,VEU,EEM,XLV,TIP,IWB,DIA,SCHX,MBB,IXUS,SHY,SHV,IWR,IGSB,IEF,SCHF,QUAL,VV,GDX,XLF,MUB,TLT,PFF,EMB,IVE,SCHB,XLY,SDY,SLV,GOVT,MDY,BIV,XLP,VT,BIL,JPST,MINT,VBR,RSP,JNK,DVY,IWP,SCHD,VGK,ACWI,SCHP,SCHG,XLI,XLU,DGRO,VMBS,VHT,MTUM,IGIB,IEI,VBK,EFAV,XLC,IWS,GSLC,EWJ,FDN,SCHA'
temp_arr = temp.split(',')
etf = []
for i in range(100):
    etf.append(temp_arr[i])


etf = stk + etf

print(etf)

year = ["1990","1991","1992","1993","1994","1995","1996","1997","1998","1999",
        "2000","2001","2002","2003","2004","2005","2006","2007","2008","2009",
        "2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"]
month = ["00","01","02","03","04","05","06","07","08","09","10","11","12"]
day = ["00","01","02","03","04","05","06","07","08","09","10",
            "11","12","13","14","15","16","17","18","19","20",
            "21","22","23","24","25","26","27","28","29","30","31"]
day_of_month = [ 31,28,31, 30,31,30, 31,31,30, 31,30,31]

# etf = ['XLC','SPY','IVV']

# today = datetime.date.today()
today = datetime.date(2016,12,1)
for nnnn in range(2,6):
    max_length = []
    # nnnn = 1
    if nnnn == 0 :
        nnnn = 10000
    if nnnn > 0 :
        # 資料庫
        db = pymysql.connect("localhost", "root", "esfortest", "etf")
        cursor = db.cursor()

        rewards = np.zeros(len(etf))
        # print(rewards)
        a=0
        #while(a<len(etf)):
        # while(a<1):
        for a in range(len(etf)):
        # for a in range(3,4):    
            print(etf[a])
            sql = "select * from detail where name = '"+etf[a]+"'"
            # print(sql)
            cursor.execute(sql)
            result_select = cursor.fetchall()
            db.commit()
            # print(result_select)

            found  = result_select[0][10]

            vary = relativedelta(today,found)
            y = vary.years
            if y <= 0:
                max_length.append(-2)
                continue
            
            if y >= nnnn :
                y = nnnn
                max_length.append(y)
            else:
                max_length.append(-1)
            
            

            # y = result_select[0][9]-1 #成立年限


            
            # y=1
            r = np.zeros(y) #放每年的報酬率

            #手續費
            process_fee_percent = 0.1425/100

            #總費用率費(內扣)
            manage_fee = float(result_select[0][5])#從性質表拿總費用率
            manage_fee_day = manage_fee /100/365#每天平均的內扣
            # print(manage_fee)

            #配息率
            div_percent = float(result_select[0][8])#從性質表拿配息率
            # div_percent = float(result_select[0][7])/100#從性質表拿配息率
            # print(div_percent)


            #取得今天與昨天日期
            # today = datetime.date.today()
            # print(today)
            yesterday = today - datetime.timedelta(days=10)
            # yesterday = datetime.date(2017,7,17)
            #print(yesterday)


            #計算每一年的報酬率
            for b in range(y):
            #for b in range(1):
                final_date = yesterday - datetime.timedelta(days=b*365)

                w = final_date.weekday()
                # print(w)
                if w==6:
                    final_date = final_date - datetime.timedelta(days=2)
                elif w==5:
                    final_date = final_date - datetime.timedelta(days=1)

                # print(final_date)



                start_date = final_date - datetime.timedelta(days=365)
                # print(start_date)
                w = start_date.weekday()
                if w==6:
                    start_date = start_date - datetime.timedelta(days=2)
                elif w==5:
                    start_date = start_date - datetime.timedelta(days=1)

                # print(start_date)



                #每月投入資金
                input_month = 1000
                #投資幾年
                year_amt = 1

                #賣出日期
                final_date = str(final_date)
                final_year = int(final_date[0:4])
                final_year = final_year-1990
                final_month = int(final_date[5:7])
                final_day = int(final_date[8:])
                #final_day = 12
                # print(final_year,final_month,final_day)

                #投入日期 
                start_date = str(start_date)
                start_year = int(start_date[0:4])
                start_year = start_year-1990
                start_month = int(start_date[5:7])
                start_day = int(start_date[8:])
                # print(start_year,start_month,start_day)

                #第一個一月(每年一月投入配息)
                if start_month==1:
                    first_Jan = 1
                else:
                    first_Jan = (12-start_month)+1
                # print(first_Jan)

                #計算投資月份數
                #第一年12-投入月份+中間年數*12+最後一年投入月份數
                month_amt = 12
                # print(month_amt)

                buy_unit = np.empty(month_amt)
                close = np.empty(month_amt)
                manage = np.empty(month_amt)
                money = np.empty(month_amt)
                unit = np.empty(month_amt)



                #從資料庫取得最終日收盤價
                sql = "select * from etf_close where (name = '"+etf[a]+"' and date = '" + final_date + "')"
                # print(sql)
                cursor.execute(sql)
                result_select = cursor.fetchall()
                db.commit()

                temp_date = datetime.datetime.strptime(final_date,'%Y-%m-%d')
                while len(result_select) == 0:
                    temp_date = temp_date - datetime.timedelta(days=1)
                    temp = str(temp_date).split(' ')
                    # print(temp[0])
                    sql = "select * from etf_close where (name = '"+etf[a]+"' and date = '" + str(temp[0]) + "')"
                    # print(sql)
                    cursor.execute(sql)
                    result_select = cursor.fetchall()
                    db.commit()

                final_close = result_select[0][2]
                # print(result_select)
                # print(final_close)

                #取得每月第一天收盤價 
                #若起始日為當月1日則由當月開始計算，否則由下個月1日開始
                i=start_year
                if start_day==1:
                    j=start_month
                else:
                    j=start_month+1
                    if j>12:
                        j=1
                        i+=1
                # print(i,j)
                k=0
                #若<12月繼續迴圈 >12月則年份加一 從1月重新開始
                while(k < month_amt and i<=final_year):
                    while(j<=12 and k < month_amt):
                        sql = "select * from etf_close where (name = '"+etf[a]+"' and date like '" + year[i]+"-"+month[j]+"%')"#從資料庫取當月所有收盤價
                        # print(sql)
                        cursor.execute(sql)
                        result_select = cursor.fetchall()
                        db.commit()
                        close[k] = result_select[0][2]#取當月第一筆資料 存入收盤價陣列以便之後使用

                        j+=1
                        k+=1
                    j=1
                    i+=1
                # db.close()
                # print(close)

                #考慮管理費與內扣計算總額
                #配息在每年一月投入
                l=0
                now_money = 0.0
                now_unit = 0.0
                while(l<month_amt):
                    #下個月的收盤價
                    if l+1<month_amt:
                        next_close = close[l+1]
                    else:
                        next_close = final_close

                    input_money=input_month#投入的錢=每月投入金額
                    #print( (l-first_Jan)%12 )
                    if (l-first_Jan)%12==0:#看是否為一月 若是則要投入配息 加進投入的錢裡
                        #配息=目前持有總資金*殖利率
                        div = now_money*div_percent
                        input_money += div   
                    #手續費=投入金額*手續費趴數     
                    process_fee = input_money*process_fee_percent
                    input_money-=process_fee

                    buy_unit[l] = input_money/close[l]#當月買的單位數=投入的錢/當月1日收盤價
                    now_unit += buy_unit[l]#將當月買入的單位數加入目前總單位數

                    now_money =float( now_unit) * float(next_close) #下個月將持有的資金=目前持有單位數*下月1日收盤價
                    #(此項為估算)這一個月內所扣掉的所有內扣 = 每天內扣趴數 * 每個月有幾天 *下個月持有資金
                    manage[l] = manage_fee_day * day_of_month[(l-first_Jan)%12] * now_money 
                    now_money -= manage[l]#下個月持有的資金-內扣
                    now_unit = now_money / float(next_close)#下個月扣完內扣後所持有的單位數
                    money[l] = now_money #將目前持有資金金額存入陣列以便觀察
                    unit[l] = now_unit #將目前持有單位數存入陣列以便觀察

                    l+=1

                # print(money) 
                # print(unit)      

                #持有單位數終值
                total_unit = unit[month_amt-1]
                # print(total_unit)

                #資產終值 賣出時再扣一次手續費
                final_money = money[month_amt-1] - money[month_amt-1]*process_fee_percent
                # print(final_money)

                #總投入資金=每月投入金額*投入月份總數
                total_cost = input_month * month_amt
                # print(total_cost)

                #報酬率=(資產終值-投入總金額)/投入總金額
                reward = ( final_money - total_cost )/total_cost
                # print(reward)

                r[b] = reward

            # print(r)
            r=r+1
            # print(r)

            re = np.prod(r)**(1.0/len(r)) #幾何平均
            # print(re)
            rewards[a]=re-1 #VTI 0.04344901

        # print(rewards)
        db.close()

        reward_min = []

        for i in range(len(rewards)):
            reward_min.append(rewards[i])


    print(reward_min)


    db = pymysql.connect("localhost", "root", "esfortest", "etf")
    cursor = db.cursor()
    for i in range(len(etf)):
        sql_select = "select * from `各長年化值` where (year = '"+str(today.year)+"' and length = '"+str(max_length[i])+"' and name = '"+str(etf[i])+"')"
        cursor.execute(sql_select)
        result_select = cursor.fetchall()
        print(result_select)
        if  result_select == ():
            try:
                sql = "INSERT INTO `各長年化值`(`year`,`length`,`name`,`reward`) VALUES"
                values = "('%s','%s','%s','%s')"
                sql += values % (str(today.year),str(max_length[i]),str(etf[i]),str(reward_min[i]))
                cursor.execute(sql)
                db.commit()
            except Exception as e:
                db.rollback()
    db.close()
