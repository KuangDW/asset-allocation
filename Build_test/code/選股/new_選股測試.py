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
years = ["1990","1991","1992","1993","1994","1995","1996","1997","1998","1999",
        "2000","2001","2002","2003","2004","2005","2006","2007","2008","2009",
        "2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"]
month = ["00","01","02","03","04","05","06","07","08","09","10","11","12"]
day = ["00","01","02","03","04","05","06","07","08","09","10",
            "11","12","13","14","15","16","17","18","19","20",
            "21","22","23","24","25","26","27","28","29","30","31"]
day_of_month = [ 31,28,31, 30,31,30, 31,31,30, 31,30,31]

today = datetime.date(2020,1,1)
nnnn = 1


#ETF類表
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

db = pymysql.connect("localhost", "root", "esfortest", "etf")
cursor = db.cursor()

# sql = "select * from `各長年化值` where (year =  '"+str(today.year) +"' and length = '"+str(nnnn) +"' )"
# cursor.execute(sql)
# result_select = cursor.fetchall()
# df_reward_std1 = pd.DataFrame(list(result_select))
# df_reward_std1 = df_reward_std1.drop([0,1],axis=1)
# print(df_reward_std1)



test = []
for i in range(0,40,2):
    test.append(etf[i])

df_reward_std = pd.DataFrame(columns=['2', '3', '4'])

for i in range(len(test)):
    sql = "select * from `各長年化值` where (year =  '"+str(today.year) +"' and length = '"+str(nnnn) +"' and name = '"+str(test[i]) +"')"
    cursor.execute(sql)
    result_select = cursor.fetchall()
    db.commit()
    df_reward_std.loc[i] = [result_select[0][2], result_select[0][3], result_select[0][4]]

print(df_reward_std)




#相關性的表([1][1]開始喔)
db = pymysql.connect("localhost", "root", "esfortest", "etf")
cursor = db.cursor()
sql = "select * from close"
cursor.execute(sql)
result_select = cursor.fetchall()
db.commit()
df = pd.DataFrame(list(result_select))
df = df.drop([0],axis=1)
corr_pd1 = df.corr()

code = [] #ETF代碼從0開始

for produce in range(0,len(v1)):
    code.append(produce)

class Etfs:
    def _init_(self,the_name,the_code,the_reward,the_risk,the_sharp):
        self.the_name = the_name
        self.the_code = the_code
        self.the_reward = the_reward
        self.the_risk = the_risk
        self.the_sharp = the_sharp
    




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
sort_etf_target = sorted(etf_target,key=operator.attrgetter('the_risk'))

total_risk = []
total_reward = []
total_name = []
total_ratio = []
total_count = [] 


for i in range(4,21):
    print(i)
    #各種組合的產出
    choose_etf = list(combinations(sort_etf_target,i)) 

    for j in range(int(comb(len(sort_etf_target),i))):

        calc_reward = 0
        average_reward = 0
        risk = 100

        for k in range(len(choose_etf[j])):
            calc_reward = calc_reward + choose_etf[j][k].the_reward
        average_reward = calc_reward/len(choose_etf[j])

        length = len(choose_etf[j])

        w_d = 0
        for g in range(length): 
            w_d += (1/length ** 2) * (choose_etf[j][g].the_risk ** 2)
        w_cov = 0
        w_cov1 = 0
        for g in range(length): 
            for h in range(length):
                if g != h:
                    w_cov1 += (1/length * choose_etf[j][g].the_risk) * (1/length * choose_etf[j][h].the_risk) * corr_pd1[choose_etf[j][g].the_code+1][choose_etf[j][h].the_code+1]

        risk = (w_d + w_cov1) ** (1/2)

        total_risk.append(risk)
        total_reward.append(average_reward)
        total_count.append(length)
        total_ratio.append(1/length)
        name = []
        for b in range(len(choose_etf[j])):
            name.append(choose_etf[j][b].the_name)
        final_name =  ' '.join(name)
        total_name.append(final_name)


total = pd.DataFrame(total_count,columns=['count'])
total = pd.concat([total, pd.DataFrame(total_ratio,columns=['ratio'])],axis=1)
total = pd.concat([total, pd.DataFrame(total_name,columns=['name'])],axis=1)
total = pd.concat([total, pd.DataFrame(total_reward,columns=['reward'])],axis=1)
total = pd.concat([total, pd.DataFrame(total_risk,columns=['risk'])],axis=1)
# print(total['expect_r'])
# print(exp_rw[-1])
str_data = 'C:/Users/User/Downloads/資產配置/選股結果_新版_etf_20_5_final.csv'
total.to_csv(str_data, index= False)



# start_time = datetime.date(2016,5,5)
# last_time = datetime.date(2016,5,5)
# sql_final_name = 'QQQ MBB XLI XLK VGT FDN'
# sql_final_w = '0.16667 0.16667 0.16667 0.16667 0.16667 0.16667'
# last_money = '2500  2500  2500  2500  2500  2500'
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



