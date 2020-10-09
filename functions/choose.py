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
years = ["1990","1991","1992","1993","1994","1995","1996","1997","1998","1999",
        "2000","2001","2002","2003","2004","2005","2006","2007","2008","2009",
        "2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"]
month = ["00","01","02","03","04","05","06","07","08","09","10","11","12"]
day = ["00","01","02","03","04","05","06","07","08","09","10",
            "11","12","13","14","15","16","17","18","19","20",
            "21","22","23","24","25","26","27","28","29","30","31"]
day_of_month = [ 31,28,31, 30,31,30, 31,31,30, 31,30,31]


# today = datetime.date.today()
today = datetime.date(2010,10,3)

year = sys.argv[1]
goal_money = sys.argv[2]
in_per_year = sys.argv[3]
mode = sys.argv[4]#1:投資 2:圓夢 3:退休
first_input = float(sys.argv[5])
nnnn = int(sys.argv[6])
first_input = first_input*10000
year = int(year)
goal_money = round(float(goal_money))
in_per_year = int(in_per_year)
mode = int(mode)

username = sys.argv[7]
password = sys.argv[8]



# year = 40
# goal_money = 6*25*12*10000*(1.0172**40)
# in_per_year =  120000
# mode = 3
# first_input = 15
# nnnn = 1
# first_input = first_input*10000

# username = "max"
# password = "1234"




use_year_input=0

if mode!=1:
    # print("not mode1")
    money = np.zeros(year+1)
    money[0] = first_input*(-1)

    for i in range(1,year):
        money[i] = in_per_year*(-1)
    
    money[year] = goal_money
    # print(money)
    
    expect_reward_y = npf.irr (money)
    # print(expect_reward_y)
    
    money = np.zeros(year*12+1)
    money[0] = first_input*(-1)
    for i in range(1,year*12):
        money[i] = in_per_year/12*(-1)
    
    money[year*12] = goal_money
    # print(money)
    expect_reward_m = npf.irr(money)*12
    # print(expect_reward_m)
else:
    # print("mode1")
    # in_per_year = input_money
    money = np.zeros(year+1)
    money[0] = in_per_year*(-1)
    for i in range(1,year):
        money[i] = 0
    money[year] = goal_money

    expect_reward_m = npf.irr(money)
    expect_reward_y = expect_reward_m
    use_year_input=1
    # expect_reward = expect_reward_m

# print(money)
expect_reward = expect_reward_m
# expect_reward = 0.0647
# print(expect_reward)


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

v1 = stk + etf

year = ["1990","1991","1992","1993","1994","1995","1996","1997","1998","1999",
        "2000","2001","2002","2003","2004","2005","2006","2007","2008","2009",
        "2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"]
month = ["00","01","02","03","04","05","06","07","08","09","10","11","12"]
day = ["00","01","02","03","04","05","06","07","08","09","10",
            "11","12","13","14","15","16","17","18","19","20",
            "21","22","23","24","25","26","27","28","29","30","31"]
day_of_month = [ 31,28,31, 30,31,30, 31,31,30, 31,30,31]

db = pymysql.connect("localhost", "root", "esfortest", "etf")
cursor = db.cursor()
# sql = "select * from `各長年化值` where (year =  '"+str(today.year) +"' and length = '"+str(nnnn) +"')"
# cursor.execute(sql)
# result_select = cursor.fetchall()
# db.commit()
# # print(result_select)
# df_reward_std = pd.DataFrame(list(result_select))
# df_reward_std = df_reward_std.drop([0,1],axis=1)



test = []
for i in range(len(etf)):
    test.append(etf[i])


df_reward_std = pd.DataFrame(columns=['2', '3', '4'])

# print(test)

for i in range(len(test)):
    sql = "select * from `各長年化值` where (year =  '"+str(today.year) +"' and length = '"+str(nnnn) +"' and name = '"+str(test[i]) +"')"
    cursor.execute(sql)
    result_select = cursor.fetchall()
    db.commit()
    if (len(result_select))!=0:
        df_reward_std.loc[i] = [result_select[0][2], result_select[0][3], result_select[0][4]]

df_reward_std = df_reward_std.reset_index(drop=True)


# temp = 'NVDA,NFLX,XLK,IWF,EQIX,CAT,COST,SPY,VT,SBUX,XLV,VZ,VEA,BIV,EFA,KO,PFE,VMBS,XLF,BDX'
# temp_arr = temp.split(',')
# test = []
# for i in range(len(temp_arr)):
#     test.append(temp_arr[i])

# df_reward_std = pd.DataFrame(columns=['2', '3', '4'])

# db = pymysql.connect("localhost", "root", "esfortest", "etf")
# cursor = db.cursor()

# for i in range(len(test)):
#     sql = "select * from `各長年化值` where (year =  '"+str(today.year) +"' and length = '"+str(nnnn) +"' and name = '"+str(test[i]) +"')"
#     cursor.execute(sql)
#     result_select = cursor.fetchall()
#     db.commit()
#     df_reward_std.loc[len(df_reward_std)] = [result_select[0][2], result_select[0][3], result_select[0][4]]

down_range = 0.055
up_range = 0.055

#相關性的表([1][1]開始喔)
# db = pymysql.connect("localhost", "root", "esfortest", "etf")
# cursor = db.cursor()
sql = "select * from close"
cursor.execute(sql)
result_select = cursor.fetchall()
db.commit()
df = pd.DataFrame(list(result_select))
df = df.drop([0],axis=1)
corr_pd1 = df.corr()


# code = [] #ETF代碼從0開始
# for produce in range(0,len(v1)):
#     code.append(produce)



class Etfs:
    def _init_(self,the_name,the_code,the_reward,the_risk):
        self.the_name = the_name
        self.the_code = the_code
        self.the_reward = the_reward
        self.the_risk = the_risk
        # self.the_sharp = the_sharp
etf_target = []
for i in range(df_reward_std.shape[0]):
    mazda = Etfs()
    mazda.the_name = str(df_reward_std['2'][i])
    mazda.the_code = v1.index(str(df_reward_std['2'][i]))
    mazda.the_reward = float(df_reward_std['3'][i])
    mazda.the_risk = float(df_reward_std['4'][i])
    # mazda.the_sharp = sharp[i]
    etf_target.append(mazda)

import operator
# sort_etf_target = sorted(etf_target,reverse = True,key=operator.attrgetter('the_sharp'))
# sort_etf_target = sorted(etf_target,key=operator.attrgetter('the_reward'))
#按照risk由小到大排序
sort_etf_target = sorted(etf_target,key=operator.attrgetter('the_risk'))
#將排序好的區分比expect_reward高的和低的
# for i in range(len(sort_etf_target)):
#     if sort_etf_target[i].the_reward >= expect_reward-down_range and sort_etf_target[i].the_reward <= expect_reward and limit<20:
#         sort_etf_target_down_raw.append(sort_etf_target[i])
#         count = count + 1 
#     if sort_etf_target[i].the_reward <= expect_reward+up_range and sort_etf_target[i].the_reward >= expect_reward and limit<20:
#         sort_etf_target_up_raw.append(sort_etf_target[i])
#         count = count + 1 
final_choose_etf = []
final_reward = 0
true_final_risk = 100
ans_count = 0


while(ans_count==0):
    down_range = down_range - 0.01
    down_range = format(down_range , '0.3f')
    down_range = float(down_range)
    if(down_range<0):
        break
    else:
        limit = 0
        sort_etf_target_up_raw = []
        sort_etf_target_down_raw = []
        for i in range(len(sort_etf_target)):
            if ((sort_etf_target[i].the_reward >= expect_reward - down_range) and (sort_etf_target[i].the_reward <= expect_reward) and limit<20):
                sort_etf_target_down_raw.append(sort_etf_target[i])
                # count = count + 1 
            if ((sort_etf_target[i].the_reward <= expect_reward + up_range) and( sort_etf_target[i].the_reward > expect_reward) and limit<20):
                sort_etf_target_up_raw.append(sort_etf_target[i])
                # count = count + 1

        if (len(sort_etf_target_up_raw) == 0):
            break

        for num in range(4,21):
            #先把choose_etf擺一個比較高的進去
            sort_etf_target_up = sort_etf_target_up_raw.copy()
            sort_etf_target_down = sort_etf_target_down_raw.copy()

            if (len(sort_etf_target_up)+len(sort_etf_target_down))<num:
                break

            final_risk = 100
            choose_etf = []
            # choose_etf.append(sort_etf_target_up[0])
            # del sort_etf_target_up[0]    

            if len(sort_etf_target_down)!= 0:
                if (len(sort_etf_target_down)==0 and len(sort_etf_target_up)==0):
                    break
                choose_etf.append(sort_etf_target_up[int(len(sort_etf_target_up)/5)])
                del sort_etf_target_up[int(len(sort_etf_target_up)/5)]    
            else:
                if (len(sort_etf_target_down)==0 and len(sort_etf_target_up)==0):
                    break
                choose_etf.append(sort_etf_target_down[int(len(sort_etf_target_down)/5)])
                del sort_etf_target_down[int(len(sort_etf_target_down)/5)]    


            #如果還沒有到達所需檔數，就繼續添加
            while(len(choose_etf)<num):

                calc_reward = 0
                for b in range(len(choose_etf)):
                    calc_reward = calc_reward + choose_etf[b].the_reward
                average_reward = calc_reward/len(choose_etf)


                if (len(sort_etf_target_down)==0 and len(sort_etf_target_up)==0):
                    break


                if((average_reward >= expect_reward)):
                    if(len(sort_etf_target_down)!=0):
                        min_risk = 100
                        min_test_etf = []
                        min_index = -1
                        #由於股債平衡的概念，跑sort_etf_target_down，選出組合risk最低的etf出來
                        for i in range(len(sort_etf_target_down)):
                            test_etf = choose_etf.copy()
                            test_etf.append(sort_etf_target_down[i])
                            length = len(test_etf)
                            w_d = 0
                            for g in range(length): 
                                w_d += (1/length ** 2) * (test_etf[g].the_risk ** 2)
                            w_cov = 0
                            w_cov1 = 0
                            for g in range(length): 
                                for j in range(length):
                                    if g != j:
                                        w_cov1 += (1/length * test_etf[g].the_risk) * (1/length * test_etf[j].the_risk) * corr_pd1[test_etf[g].the_code+1][test_etf[j].the_code+1]
                            risk = (w_d + w_cov1) ** (1/2)
                            if risk < min_risk:
                                min_risk = risk
                                min_test_etf = test_etf.copy()
                                min_index = i
                        final_risk = min_risk
                        del sort_etf_target_down[min_index]
                        choose_etf = min_test_etf.copy()
                    else:
                        if (len(sort_etf_target_up)!=0):
                            min_risk = 100
                            min_test_etf = []
                            min_index = -1
                            for i in range(len(sort_etf_target_up)):
                                test_etf = choose_etf.copy()
                                test_etf.append(sort_etf_target_up[i])
                                length = len(test_etf)
                                w_d = 0
                                for g in range(length): 
                                    w_d += (1/length ** 2) * (test_etf[g].the_risk ** 2)
                                w_cov = 0
                                w_cov1 = 0
                                for g in range(length): 
                                    for j in range(length):
                                        if g != j:
                                            # print(length)
                                            # print(test_etf[g].the_risk)
                                            # print(test_etf[j].the_risk)
                                            # print(corr_pd1[test_etf[g].the_code+1][test_etf[j].the_code+1])
                                            w_cov1 += (1/length * test_etf[g].the_risk) * (1/length * test_etf[j].the_risk) * corr_pd1[test_etf[g].the_code+1][test_etf[j].the_code+1]
                                risk = (w_d + w_cov1) ** (1/2)
                                if risk < min_risk:
                                    min_risk = risk
                                    min_test_etf = test_etf.copy()
                                    min_index = i
                            final_risk = min_risk
                            del sort_etf_target_up[min_index]
                            choose_etf = min_test_etf.copy()
                            

                if((average_reward < expect_reward)):
                    if (len(sort_etf_target_up)!=0):
                        min_risk = 100
                        min_test_etf = []
                        min_index = -1
                        for i in range(len(sort_etf_target_up)):
                            test_etf = choose_etf.copy()
                            test_etf.append(sort_etf_target_up[i])
                            length = len(test_etf)
                            w_d = 0
                            for g in range(length): 
                                w_d += (1/length ** 2) * (test_etf[g].the_risk ** 2)
                            w_cov = 0
                            w_cov1 = 0
                            for g in range(length): 
                                for j in range(length):
                                    if g != j:
                                        # print(length)
                                        # print(test_etf[g].the_risk)
                                        # print(test_etf[j].the_risk)
                                        # print(corr_pd1[test_etf[g].the_code+1][test_etf[j].the_code+1])
                                        w_cov1 += (1/length * test_etf[g].the_risk) * (1/length * test_etf[j].the_risk) * corr_pd1[test_etf[g].the_code+1][test_etf[j].the_code+1]
                            risk = (w_d + w_cov1) ** (1/2)
                            if risk < min_risk:
                                min_risk = risk
                                min_test_etf = test_etf.copy()
                                min_index = i
                        final_risk = min_risk
                        del sort_etf_target_up[min_index]
                        choose_etf = min_test_etf.copy()
                    else:
                        if(len(sort_etf_target_down)!=0):
                            min_risk = 100
                            min_test_etf = []
                            min_index = -1
                            #由於股債平衡的概念，跑sort_etf_target_down，選出組合risk最低的etf出來
                            for i in range(len(sort_etf_target_down)):
                                test_etf = choose_etf.copy()
                                test_etf.append(sort_etf_target_down[i])
                                length = len(test_etf)
                                w_d = 0
                                for g in range(length): 
                                    w_d += (1/length ** 2) * (test_etf[g].the_risk ** 2)
                                w_cov = 0
                                w_cov1 = 0
                                for g in range(length): 
                                    for j in range(length):
                                        if g != j:
                                            w_cov1 += (1/length * test_etf[g].the_risk) * (1/length * test_etf[j].the_risk) * corr_pd1[test_etf[g].the_code+1][test_etf[j].the_code+1]
                                risk = (w_d + w_cov1) ** (1/2)
                                if risk < min_risk:
                                    min_risk = risk
                                    min_test_etf = test_etf.copy()
                                    min_index = i
                            final_risk = min_risk
                            del sort_etf_target_down[min_index]
                            choose_etf = min_test_etf.copy()
                
                
                # if((average_reward >= expect_reward)):
                #     if (len(choose_etf)==num or (len(sort_etf_target_down)) == 0):
                #         break
                #     if(len(sort_etf_target_down)!=0):
                #         min_risk = 100
                #         min_test_etf = []
                #         min_index = -1
                #         #由於股債平衡的概念，跑sort_etf_target_down，選出組合risk最低的etf出來
                #         for i in range(len(sort_etf_target_down)):
                #             test_etf = choose_etf.copy()
                #             test_etf.append(sort_etf_target_down[i])
                #             length = len(test_etf)
                #             w_d = 0
                #             for g in range(length): 
                #                 w_d += (1/length ** 2) * (test_etf[g].the_risk ** 2)
                #             w_cov = 0
                #             w_cov1 = 0
                #             for g in range(length): 
                #                 for j in range(length):
                #                     if g != j:
                #                         w_cov1 += (1/length * test_etf[g].the_risk) * (1/length * test_etf[j].the_risk) * corr_pd1[test_etf[g].the_code+1][test_etf[j].the_code+1]
                #             risk = (w_d + w_cov1) ** (1/2)
                #             if risk < min_risk:
                #                 min_risk = risk
                #                 min_test_etf = test_etf.copy()
                #                 min_index = i
                #         final_risk = min_risk
                #         del sort_etf_target_down[min_index]
                #         choose_etf = min_test_etf.copy()


                #     if (len(choose_etf)==num or (len(sort_etf_target_down)) == 0):
                #         break

                # elif((average_reward < expect_reward)):
                #     if (len(choose_etf)==num or (len(sort_etf_target_up)) == 0):
                #         break
                #     if (len(sort_etf_target_up)!=0):
                #         min_risk = 100
                #         min_test_etf = []
                #         min_index = -1
                #         for i in range(len(sort_etf_target_up)):
                #             test_etf = choose_etf.copy()
                #             test_etf.append(sort_etf_target_up[i])
                #             length = len(test_etf)
                #             w_d = 0
                #             for g in range(length): 
                #                 w_d += (1/length ** 2) * (test_etf[g].the_risk ** 2)
                #             w_cov = 0
                #             w_cov1 = 0
                #             for g in range(length): 
                #                 for j in range(length):
                #                     if g != j:
                #                         # print(length)
                #                         # print(test_etf[g].the_risk)
                #                         # print(test_etf[j].the_risk)
                #                         # print(corr_pd1[test_etf[g].the_code+1][test_etf[j].the_code+1])
                #                         w_cov1 += (1/length * test_etf[g].the_risk) * (1/length * test_etf[j].the_risk) * corr_pd1[test_etf[g].the_code+1][test_etf[j].the_code+1]
                #             risk = (w_d + w_cov1) ** (1/2)
                #             if risk < min_risk:
                #                 min_risk = risk
                #                 min_test_etf = test_etf.copy()
                #                 min_index = i
                #         final_risk = min_risk
                #         del sort_etf_target_up[min_index]
                #         choose_etf = min_test_etf.copy()

                #     if (len(choose_etf)==num or (len(sort_etf_target_up)) == 0):
                #         break
                
                
            calc_reward = 0
            for b in range(len(choose_etf)):
                calc_reward = calc_reward + choose_etf[b].the_reward
            average_reward = calc_reward/len(choose_etf)
            # print("目前選股個數")
            # print(num)
            # print("solution")
            # for c in range(len(choose_etf)):
            #     print(choose_etf[c].the_name)
            # print("reward")
            # print(average_reward)
            # print("risk")
            # print(final_risk)
            if average_reward > expect_reward:
                ans_count = ans_count + 1
                if(final_risk < true_final_risk):
                    final_choose_etf = choose_etf.copy()
                    final_reward = average_reward
                    true_final_risk = final_risk
    # print("final count")
    # print(ans_count)
    # print("final solution")
    # for c in range(len(final_choose_etf)):
    #     print(final_choose_etf[c].the_name)
    # print("final_reward")
    # print(final_reward)
    # print("final_risk")
    # print(true_final_risk)
final_w = []
for i in range(len(final_choose_etf)):
    final_w.append(format((1/len(final_choose_etf)), '0.5f') ) 
sql_final_reward = 0

name = []
for i in range(len(final_choose_etf)):
    name.append(final_choose_etf[i].the_name)
sql_expect_reward = expect_reward

last_money = []
last_money_temp = []
# 如果是第一年做再平衡 
for i in range(len(name)):
    last_money_temp.append(first_input*float(final_w[i]))
# print(last_money_temp)


sql_final_name =  ' '.join(name)
sql_final_w = ' '.join(final_w)
sql_max_reward = format(final_reward*100, '0.3f') + "%"
sql_min_risk = format(true_final_risk , '0.3f')
sql_use_year_input = 0

sql_final_reward = '0'
sql_final_div = '0'
print(sql_final_name)
print(sql_final_w)
print(sql_max_reward)
print(sql_min_risk)
print('0 0 0 0 0 0')
print(sql_use_year_input)
print('0 0 0 0 0 0')
print('0 0 0 0 0 0')
print(sql_expect_reward)
print(today.year)
print(today.month)
print(today.day)




temp = []
for i in range(len(name)):
    temp.append(0)
temp = str(temp)
sql_final_temp = temp.replace(',',' ')
sql_final_temp = sql_final_temp.replace('[','')
sql_final_temp = sql_final_temp.replace(']','')
# print(sql_final_temp)

db = pymysql.connect("localhost", "root", "esfortest", "etf")
cursor = db.cursor()



last_money = str(last_money_temp)
last_money = last_money.replace(',',' ')
last_money = last_money.replace('[','')
last_money = last_money.replace(']','')

sum_of_money = sum(last_money_temp)

new_asset = []
for i in range(len(last_money_temp)):
    if sum_of_money == 0:
        new_asset.append(0)
    new_asset.append(last_money_temp[i]/sum_of_money)
new_asset = str(new_asset)
new_asset = new_asset.replace(',',' ')
new_asset = new_asset.replace('[','')
new_asset = new_asset.replace(']','')


# sql="UPDATE  `user_data` SET (`start_time`,`last_time`,`target`,`weight`,`last_money`,`expect_reward`,`reward`,`first_time`, `in_per_year`,`balence`,`tolerance`,`type`,`sell_buy`,`risk`,`nodiv_reward`,`dividend`  ) VALUES where id = '"+password+"'"
sql= "UPDATE user_data SET start_time='%s', last_time='%s', target='%s', weight='%s', last_money='%s', expect_reward='%s', reward='%s', first_time='%s', in_per_year='%s', balence='%s', tolerance='%s', type='%s', sell_buy='%s', risk='%s', nodiv_reward='%s', dividend='%s', last_ratio='%s' WHERE id='%s'" % (str(today),str(today),str(sql_final_name),str(sql_final_w),str(last_money),str(sql_expect_reward),str(sql_max_reward),str(first_input),str(in_per_year),'0.2','0.1','3',str(sql_final_temp),str(sql_min_risk),str(sql_final_reward),str(sql_final_div),str(new_asset),str(password))
# values = "('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
# sql += values % (str(today),str(today),str(sql_final_name),str(sql_final_w),str(sql_final_temp),str(sql_expect_reward),str(sql_max_reward),str(first_input),str(sql_use_year_input),'0.2','0.1','3',str(sql_final_temp),str(sql_min_risk))
# cursor.execute(sql)
# db.commit()
# db.close()


sqlr= "UPDATE user_datar SET start_time='%s', last_time='%s', target='%s', weight='%s', last_money='%s', expect_reward='%s', reward='%s', first_time='%s', in_per_year='%s', balence='%s', tolerance='%s', type='%s', sell_buy='%s', risk='%s', nodiv_reward='%s', dividend='%s', last_ratio='%s' WHERE id='%s'" % (str(today),str(today),str(sql_final_name),str(sql_final_w),str(last_money),str(sql_expect_reward),str(sql_max_reward),str(first_input),str(in_per_year),'0.2','0.1','3',str(sql_final_temp),str(sql_min_risk),str(sql_final_reward),str(sql_final_div),str(new_asset),str(password))


try:
    cursor.execute(sql)
    cursor.execute(sqlr)
    db.commit()
    # print("Data are successfully inserted")
except Exception as e:
    db.rollback()
    # print("Exception Occured : ", e)
db.close()


# db = pymysql.connect("localhost", "root", "esfortest", "etf")
# cursor = db.cursor()
# sql="insert into `選股結果3` (`name`,`weight`,`reward`,`risk`,`expect_reward`,`y_input`,`nodiv_reward`, `dividend`  ) VALUES"
# values = "('%s','%s',%f,%f,%f,%f,%f,%f)"
# sql += values % (str(sql_final_name),str(sql_final_w),float(sql_max_reward),float(sql_min_risk),sql_expect_reward,sql_use_year_input,float(sql_final_reward),float(sql_final_div))
# try:
#     cursor.execute(sql)
#     db.commit()
#     # print("Data are successfully inserted")
# except Exception as e:
#     db.rollback()
#     # print("Exception Occured : ", e)
# db.close()




# justify = 0
# length =  len(final_choose_etf)
# for i in range(length):
#     justify = justify + final_choose_etf[i].the_reward

# justify_reward = justify/length


# w_d = 0
# for g in range(length): 
#     w_d += (1/length ** 2) * (final_choose_etf[g].the_risk ** 2)
# w_cov = 0
# w_cov1 = 0
# for g in range(length): 
#     for j in range(length):
#         if g != j:
#             w_cov1 += (1/length * final_choose_etf[g].the_risk) * (1/length * final_choose_etf[j].the_risk) * corr_pd1[final_choose_etf[g].the_code+1][final_choose_etf[j].the_code+1]
# justify_risk = (w_d + w_cov1) ** (1/2)

# print(justify_reward)
# print(justify_risk)

