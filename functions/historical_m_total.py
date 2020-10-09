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
starttime = datetime.datetime.now()
from dateutil.relativedelta import relativedelta


choose1_raw = str(sys.argv[1])
weight1_raw = str(sys.argv[2])
want_m_raw = int(sys.argv[3])-1
input_per_month_raw = float(sys.argv[4])/12

date1 = int(sys.argv[5])
date2 = int(sys.argv[6])
date3 = int(sys.argv[7])

today = datetime.date(date3,date2,date1)

# choose1_raw = 'SCHP,MINT,VZ,TIP'
# weight1_raw ='0.25,0.25,0.25,0.25'
# want_m_raw = 10
# input_per_month_raw = 10000
# today = datetime.date(2015,9,19)

check = 0
while check != 1000 :
    try :
        years = ["1990","1991","1992","1993","1994","1995","1996","1997","1998","1999",
                "2000","2001","2002","2003","2004","2005","2006","2007","2008","2009",
                "2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"]
        month = ["00","01","02","03","04","05","06","07","08","09","10","11","12"]
        day = ["00","01","02","03","04","05","06","07","08","09","10",
                    "11","12","13","14","15","16","17","18","19","20",
                    "21","22","23","24","25","26","27","28","29","30","31"]
        day_of_month = [ 31,28,31, 30,31,30, 31,31,30, 31,30,31]

        temp = 'SPY,IVV,VTI,VOO,QQQ,AGG,GLD,VEA,IEFA,BND,VWO,VUG,IWF,LQD,IEMG,VTV,EFA,VIG,IJH,IJR,IWM,VCIT,IWD,VGT,XLK,VO,USMV,IAU,VCSH,BNDX,IVW,HYG,VNQ,VB,ITOT,VYM,BSV,VXUS,VEU,EEM,XLV,TIP,IWB,DIA,SCHX,MBB,IXUS,SHY,SHV,IWR,IGSB,IEF,SCHF,QUAL,VV,GDX,XLF,MUB,TLT,PFF,EMB,IVE,SCHB,XLY,SDY,SLV,GOVT,MDY,BIV,XLP,VT,BIL,JPST,MINT,VBR,RSP,JNK,DVY,IWP,SCHD,VGK,ACWI,SCHP,SCHG,XLI,XLU,DGRO,VMBS,VHT,MTUM,IGIB,IEI,VBK,EFAV,XLC,IWS,GSLC,EWJ,FDN,SCHA'
        temp_arr = temp.split(',')
        etf = []
        for i in range(100):
            etf.append(temp_arr[i])

        temp = 'KO,PLD,CSX,MMC,AAPL,MSFT,AMZN,FB,GOOGL,GOOG,JNJ,V,PG,NVDA,JPM,HD,MA,UNH,VZ,DIS,ADBE,CRM,PYPL,MRK,NFLX,INTC,T,CMCSA,PFE,BAC,WMT,PEP,ABT,TMO,CSCO,MCD,ABBV,XOM,ACN,COST,NKE,AMGN,AVGO,CVX,MDT,NEE,BMY,UNP,LIN,DHR,QCOM,PM,TXN,LLY,LOW,ORCL,HON,UPS,AMT,IBM,SBUX,C,LMT,MMM,WFC,CHTR,RTX,AMD,FIS,BA,NOW,SPGI,BLK,ISRG,GILD,CAT,MDLZ,INTU,MO,ZTS,CVS,TGT,BKNG,AXP,BDX,VRTX,DE,D,ANTM,EQIX,CCI,APD,SYK,CL,TMUS,CI,GS,DUK,MS,ATVI'
        temp_arr = temp.split(',')
        stk = []
        for i in range(100):
            stk.append(temp_arr[i])

        v1 = stk + etf

        # starttime = datetime.datetime.now()
        db = pymysql.connect("localhost", "root", "esfortest", "etf")
        cursor = db.cursor()

        # choose1 = 'SCHP,MINT,VZ,TIP'
        # weight1 ='0.25,0.25,0.25,0.25'
        # want_m = 10
        # input_per_month = 10000

        # choose1 = 'SPY,GOVT,VT,VEA'
        # weight1 ='0.31,0.23,0.23,0.23'
        # want_m = 10
        # input_per_month = 10000

        choose1 = choose1_raw
        weight1 = weight1_raw
        want_m = want_m_raw
        input_per_month = input_per_month_raw


        today = today - datetime.timedelta(days=check)
        yesterday =  today - datetime.timedelta(days=10)


        choose = choose1.split(',')
        # choose = ['VOO','VOE','VT','VEA']

        weight = weight1.split(',')
        # weight = ['0.31','0.23','0.23','0.23']
        for i in range(len(weight)):
            weight[i] = float(weight[i])


        y = 999
        for a in range(len(choose)):
            sql = "select 成立年限 from detail where name = '"+choose[a]+"'"
            # print(sql)
            cursor.execute(sql)
            result_select2 = cursor.fetchall()
            db.commit()
            # print(result_select2)
            if(result_select2[0][0] < y ):
                y = result_select2[0][0]-1
                # y=1
        if((want_m/12) <y):#小於成立年限
            if want_m>37:
                m=want_m
            else:
                m=37
        else:
            m=y*12


        target = [3+1,6+1,12+1,24+1,36+1]
        # target=[]



        # m=37
        # m=0
        rewards = np.zeros(m)#放每月的報酬率
        in_money_arr=[]#投入總金額
        for i in range(m):
            in_money_arr.append(i*input_per_month)
        d_now=yesterday
        # d_now = datetime.date(yesterday.year,yesterday.month,3)
        for b in range(m):
            if b==0:
                d_now=yesterday
            else:
                d_now = d_pre

            # if d_now.month-2<0:
            #     d_now_premonth=11
            # else:
            #     d_now_premonth = d_now.month-2
            # # d_now_premonth=d_now.month
            # dminus= day_of_month[d_now_premonth]-1
            # d_pre = d_now - datetime.timedelta(days=dminus)

            if d_now.month==1:
                pre_month = 12
                pre_year = d_now.year-1
            else:
                pre_month = d_now.month-1
                pre_year = d_now.year

            d_pre = datetime.date(pre_year,pre_month,yesterday.day)

            w = d_now.weekday()
            if w==6:
                d_now = d_now - datetime.timedelta(days=2)
            elif w==5:
                d_now = d_now - datetime.timedelta(days=1)
            w = d_pre.weekday()
            if w==6:
                d_pre = d_pre - datetime.timedelta(days=2)
            elif w==5:
                d_pre = d_pre - datetime.timedelta(days=1)
            for c in range(len(choose)):
                sql = "select close from etf_close where (name = '"+choose[c]+"' and date = '"+str(d_now) + "')"
                # print(sql)
                cursor.execute(sql)
                result_select3 = cursor.fetchall()
                db.commit()
                sql = "select close from etf_close where (name = '"+choose[c]+"' and date = '"+str(d_pre) + "')"
                # print(sql)
                cursor.execute(sql)
                result_select4 = cursor.fetchall()
                db.commit()
                if len(result_select3) >0:
                    reward_now = result_select3[0][0]
                # else:
                    # print(choose[c]+str(d_now)+'no result')
                if len(result_select4) >0:
                    reward_pre = result_select4[0][0]
                # else:
                    # print(choose[c]+str(d_pre)+'no result')
                rewarddd = (float(reward_now)-float(reward_pre))/float(reward_pre)
                rewards[b] += rewarddd * weight[c]
        #把報酬率陣列反過來排 共m個月
        result = []
        # rewards2 = []
        for x in range(len(rewards)):
            result.append(rewards[len(rewards)-1-x])
            # rewards2.append(rewards[len(rewards)-1-x])
        # print(result)
        # reward_arr = result[len(result)-6:]
        # print(len(reward_arr))
        # print(reward_arr)

        #歷史回測圖
        his_fig_rew2=[]
        his_fig_rew = result[len(result)-(want_m):]
        for i in range(len(his_fig_rew)):
            his_fig_rew2.append(str(his_fig_rew[i]))

        result0 = ' '.join(his_fig_rew2)
        print(result0)

        count = 0  
        every_reward = []  
        final_ans=[]   
        final_inmoney=[]
        for m in target:

            reward_arr = result[len(result)-(m-1):]
            # print(len(reward_arr))


            ans = np.zeros(m)

            for i in range(1,m):
                ans[i] = ans[i-1] * (reward_arr[i-1]+1) +input_per_month
            # print(ans)
            final_r = (ans[m-1]-(input_per_month*(m-1)))/(input_per_month*(m-1))
            # print(ans[m-1],input_per_month*m)
            final_r = format(final_r*100 , '0.3f')
            # every_reward[count] = str(final_r)
            # count+=1
            every_reward.append(final_r+'%')
            final_ans.append(format(ans[m-1] , '0.2f'))
            # final_ans.append(str(round(ans[m-1])))
            final_inmoney.append(str(input_per_month*(m-1)))
            # db.close()



        result1 = ' '.join(every_reward)
        result2 = ' '.join(final_ans)
        result3 = ' '.join(final_inmoney)
        print(result1)
        print(result2)
        print(result3)
        # print('0')
        # print('0')
        # print('0')
        # print(every_reward)
        # print(choose)


        endtime = datetime.datetime.now()


        start_years=[2014,2015,2016,2018]
        start_months=[6,12,6,3]
        start_days=[20,17,23,22]
        end_years=[2016,2018,2020,2020]
        end_months=[2,12,7,7]
        end_days=[11,19,28,28]


        result = []

        for a in range(len(start_days)):
        # for a in range(0):

            start_d = datetime.date(start_years[a],start_months[a],start_days[a])
            end_d =  today - datetime.timedelta(days=7)
            vary = relativedelta(end_d,start_d)
            if vary.days<=0:
                result.append('nan')
                continue
            # end_d = datetime.date(end_years[a],end_months[a],end_days[a])

            if( start_d.month < end_d.month ):#足一年
                y = end_d.year - start_d.year
                if(start_d.day < end_d.day):#足一個月
                    # end_ddd = datetime.date(end_d.year,end_d.month,start_d.day)
                    mm = end_d.month - start_d.month
                else:
                    mm = end_d.month - start_d.month -1
            else:
                y = end_d.year - start_d.year-1
                if(start_d.day < end_d.day):#足一個月
                    mm = end_d.month - start_d.month +12
                else:
                    mm = end_d.month - start_d.month +12-1
            # print(y,mm)
            m = y*12 + mm

            # if(start_d.day!=end_d.day):
            m+=1#最後不滿一個月的部分也要算

            # print(m)

            rewards = np.zeros(m)#放每月的報酬率
            in_money_arr=[]#投入總金額
            for i in range(m):
                in_money_arr.append(i*input_per_month)
            in_money_arr.append((m-1)*input_per_month)
            # d_now=yesterday
            d_now = start_d
            for b in range(m):
                if b==m-1:
                    d_now = d_aft
                    d_aft = end_d
                else:
                    if b==0:
                        d_now = start_d
                    else:
                        d_now = d_aft

                    if d_now.month==12:
                        aft_month = 1
                        aft_year = d_now.year + 1
                    else:
                        aft_month = d_now.month + 1
                        aft_year = d_now.year

                    if(start_d.day>day_of_month[aft_month-1]):
                        aft_day = day_of_month[aft_month-1]    
                    else:
                        aft_day = start_d.day

                    d_aft = datetime.date(aft_year,aft_month,aft_day)

                w = d_now.weekday()
                if w==6:
                    d_now = d_now - datetime.timedelta(days=2)
                elif w==5:
                    d_now = d_now - datetime.timedelta(days=1)

                w = d_aft.weekday()
                if w==6:
                    d_aft = d_aft - datetime.timedelta(days=2)
                elif w==5:
                    d_aft = d_aft - datetime.timedelta(days=1)

                # print(d_now,d_aft)



                for c in range(len(choose)):
                    sql = "select close from etf_close where (name = '"+choose[c]+"' and date = '"+str(d_aft) + "')"
                    # print(sql)
                    cursor.execute(sql)
                    result_select3 = cursor.fetchall()
                    db.commit()
                    sql = "select close from etf_close where (name = '"+choose[c]+"' and date = '"+str(d_now) + "')"
                    # print(sql)
                    cursor.execute(sql)
                    result_select4 = cursor.fetchall()
                    db.commit()
                    if len(result_select3) >0:
                        reward_aft = result_select3[0][0]
                    # else:
                        # print(choose[c]+str(d_now)+'no result')
                    if len(result_select4) >0:
                        reward_now = result_select4[0][0]
                    # else:
                        # print(choose[c]+str(d_pre)+'no result')
                    rewarddd = (float(reward_aft)-float(reward_now))/float(reward_now)
                    rewards[b] += rewarddd * weight[c]

            # print(rewards)

            

            ans = np.zeros(m+1)
            for i in range(1,m):
                ans[i] = ans[i-1] * (rewards[i-1]+1) +input_per_month
            ans[m] = ans[m-1] * (rewards[m-1]+1) 

            # for i in range(len(ans)):
            #     print(in_money_arr[i],ans[i])



            final_r = (ans[m]-(input_per_month*(m-1)))/(input_per_month*(m-1))
            # print(ans[m-1],input_per_month*m)
            final_r = format(final_r*100 , '0.3f')
            # every_reward[count] = str(final_r)
            # count+=1
            # print(ans)
            # print(final_r+'%')
            # print(format(ans[m] , '0.2f'))
            # print(input_per_month*(m-1))
            result.append(final_r+'%')

        # print(result)
        result4 = ' '.join(result)
        print(result4)
        endtime2 = datetime.datetime.now()
        # print((endtime-starttime).seconds)
        # print((endtime2-starttime).seconds)
        check = 1000
    except:
        check = check + 1

db.close()
