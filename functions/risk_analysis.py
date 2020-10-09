# from selenium import webdriver
# from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import pymysql
import datetime
# from selenium.webdriver.chrome.options import Options
import math
import sys
import statistics
# etf = ['VTI','VOO','VXUS','SPY','BND','IVV','BNDX','VEA','VO',
#        'VUG','VB','VWO','VTV','QQQ','BSV','BIV','VTIP','VOE','IEF',
#        'SHY','TLT','IVE','VT','GOVT']






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

etf = stk + etf

choose1 = sys.argv[1]
weight1 = sys.argv[2]
choose = choose1.split(',')
weight = weight1.split(',')
for i in range(len(weight)):
    weight[i] = float(weight[i])


date1 = int(sys.argv[3])
date2 = int(sys.argv[4])
date3 = int(sys.argv[5])

today = datetime.date(date3,date2,date1)

# today = datetime.date(2020, 8, 16)
# choose = ['BKNG','SCHP','XLP','SBUX','PG','VZ']
# weight = [0.16667,0.16667, 0.16667, 0.16667, 0.16667, 0.16667]

# days = [30,90,365]
days = [21,63,252]

stddevs = np.zeros(4)
sharpes = np.zeros(4)
# print(MDD)

db = pymysql.connect("localhost", "root", "esfortest", "etf")
cursor = db.cursor()

sql = "select * from close"
cursor.execute(sql)
result_select = cursor.fetchall()
db.commit()
df = pd.DataFrame(list(result_select))
# df = df.drop([0],axis=1)


for a in range(len(etf)):
    df = df.rename(columns={a+1:etf[a]})
# print(df)

for a in range(-1,len(choose)):
    if a==-1:
        df2 = df[0]
    else:
        df2 = pd.concat([df2, df[choose[a]] ],axis=1)
# print(df2)

i=0
while(True):
    have_nan = True
    for a in range(len(choose)):
        if np.isnan(df2[choose[a]][i])==True: #是空的
            have_nan = False
            break
    if have_nan==False:
        df2 = df2.drop([i],axis=0)
        i+=1
    else:
        break

# print(df2)
df2 = df2.reset_index(drop=True)



todayyy = today
# todayyy = datetime.date(2020, 8, 16)
df2 = df2.reset_index(drop=True)
# print(df2)
while (todayyy in list(df2[0]))==False and ( datetime.datetime.strptime(str(todayyy),"%Y-%m-%d")>datetime.datetime.strptime(str(df2[0][0]),"%Y-%m-%d") ):
    todayyy -= datetime.timedelta(days=1)
# print(start_date)
if (todayyy in list(df2[0]))==True:
    todayyy_index = list(df2[0]).index(todayyy) 
else:
    todayyy_index = 0
df2 = df2[:todayyy_index+1]
df2 = df2.reset_index(drop=True)


# 平均股價
df2['avg'] = 0
# df2 = df2.drop(['avg'],axis=1)
for i in range(len(df2['avg'])):
    for a in range(len(choose)):
        df2.loc[i,'avg'] += df2[choose[a]][i]*weight[a]
# print(df2)

# 漲幅
df2['day_return'] = 0 
for i in range(len(df2)-1):
    df2.loc[i+1,'day_return'] = (df2['avg'][i+1] - df2['avg'][i])/df2['avg'][i]
# print(df2)
df2 = df2.fillna(0)
# 無風險利率
risk_free_return = 0.01/365
# risk_free_return = 0

avg_return = statistics.mean(df2['day_return'])
# print(avg_return)

# 標準差


# print(df2.isnull().sum())
# print(statistics.stdev(df2['day_return']))
std_dev = statistics.stdev(df2['day_return'][1:])* math.sqrt(252)
# print(std_dev)#0.1757400215841394
stddevs[3]=std_dev*100

# 夏普值
sharpe = (avg_return-risk_free_return) / std_dev * math.sqrt(252)
# sharpe = (avg_return) / std_dev * math.sqrt(252)
# print(sharpe)#0.5267990017907497
sharpes[3]=sharpe

i=0
for d in days:
    df3 = df2[d*(-1):]
    df3 = df3.reset_index(drop=True)
    std_dev = statistics.stdev(df3['day_return'][1:])* math.sqrt(252)
    sharpe = (avg_return-risk_free_return) / std_dev * math.sqrt(252)
    stddevs[i]=std_dev*100   
    sharpes[i]=sharpe 
    i+=1
    # print(std_dev)
    # print(sharpe)
    # print()
stddevs2 = np.zeros(5)
d2 = [63,126,252,204,756]
i=0
for d in d2:
    df3 = df2[d*(-1):]
    df3 = df3.reset_index(drop=True)
    std_dev = statistics.stdev(df3['day_return'][1:])* math.sqrt(252)
    # sharpe = (avg_return-risk_free_return) / std_dev * math.sqrt(252)
    stddevs2[i]=std_dev*100   
    # sharpes[i]=sharpe 
    i+=1

# 最大回徹率
mdds=[]
for d in days:
    df3 = df2[d*(-1):]
    df3 = df3.reset_index(drop=True)
    df3['avg'] = 0
    for i in range(len(df3['avg'])):
        for a in range(len(choose)):
            df3.loc[i,'avg'] += df3[choose[a]][i]*weight[a]
    df3['max']=0
    s1 = df3['avg']
    for i in range(len(df3)):
        df3.loc[i,'max'] = s1[0:i+1].max() 

    df3['dd'] = 0
    df3['dd'] = 1-(df3['avg']/df3['max'])

    mdd = df3['dd'].max()
    mdds.append(mdd)
    # print(mdd)

df2['max']=0
s1 = df2['avg']
for i in range(len(df2)):
    df2.loc[i,'max'] = s1[0:i+1].max() 

df2['dd'] = 0
df2['dd'] = 1-(df2['avg']/df2['max'])

mdd = df2['dd'].max()
# print(mdd)
mdds.append(mdd)


# print(mdds)#[0.014878441598282222, 0.08107850063969146, 0.3632447312443021, 0.3632447312443021]
# print(stddevs)#[ 9.16611393 21.14502543 28.76564975 17.57400216]
# print(sharpes)#[0.06835749 0.02963215 0.02178197 0.03565338]

r1=[]
r2=[]
r3=[]
r4=[]
for i in range(4):
    r1.append(format(mdds[i] , '0.5f'))
    r2.append(format(stddevs[i] , '0.3f'))
    r3.append(format(sharpes[i] , '0.5f'))
for i in range(5):
    r4.append(format(stddevs2[i] , '0.3f'))

result1=' '.join(r1)
result2=' '.join(r2)
result3=' '.join(r3)
result4=' '.join(r4)
print(result1)
print(result2)
print(result3)
print(result4)