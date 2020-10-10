

# import yfinance as yf
# import pandas as pd
# import numpy as np
# import pymysql
# import datetime
# from dateutil.relativedelta import relativedelta

# temp = 'SPY,IVV,VTI,VOO,QQQ,AGG,GLD,VEA,IEFA,BND,VWO,VUG,IWF,LQD,IEMG,VTV,EFA,VIG,IJH,IJR,IWM,VCIT,IWD,VGT,XLK,VO,USMV,IAU,VCSH,BNDX,IVW,HYG,VNQ,VB,ITOT,VYM,BSV,VXUS,VEU,EEM,XLV,TIP,IWB,DIA,SCHX,MBB,IXUS,SHY,SHV,IWR,IGSB,IEF,SCHF,QUAL,VV,GDX,XLF,MUB,TLT,PFF,EMB,IVE,SCHB,XLY,SDY,SLV,GOVT,MDY,BIV,XLP,VT,BIL,JPST,MINT,VBR,RSP,JNK,DVY,IWP,SCHD,VGK,ACWI,SCHP,SCHG,XLI,XLU,DGRO,VMBS,VHT,MTUM,IGIB,IEI,VBK,EFAV,XLC,IWS,GSLC,EWJ,FDN,SCHA'
# temp_arr = temp.split(',')
# etf = []
# for i in range(100):
#     etf.append(temp_arr[i])

# temp = 'KO,PLD,CSX,MMC,AAPL,MSFT,AMZN,FB,GOOGL,GOOG,JNJ,V,PG,NVDA,JPM,HD,MA,UNH,VZ,DIS,ADBE,CRM,PYPL,MRK,NFLX,INTC,T,CMCSA,PFE,BAC,WMT,PEP,ABT,TMO,CSCO,MCD,ABBV,XOM,ACN,COST,NKE,AMGN,AVGO,CVX,MDT,NEE,BMY,UNP,LIN,DHR,QCOM,PM,TXN,LLY,LOW,ORCL,HON,UPS,AMT,IBM,SBUX,C,LMT,MMM,WFC,CHTR,RTX,AMD,FIS,BA,NOW,SPGI,BLK,ISRG,GILD,CAT,MDLZ,INTU,MO,ZTS,CVS,TGT,BKNG,AXP,BDX,VRTX,DE,D,ANTM,EQIX,CCI,APD,SYK,CL,TMUS,CI,GS,DUK,MS,ATVI'
# temp_arr = temp.split(',')
# stk = []
# for i in range(100):
#     stk.append(temp_arr[i])


# etf_stk = stk + etf

# db = pymysql.connect("localhost", "root", "esfortest", "etf")
# cursor = db.cursor()
# # 把input_data寫成sql語法
# for i in range(len(etf_stk)):
#     sql = "INSERT INTO detail (`name`) VALUES"
#     values = "('%s')"
#     sql += values % (etf_stk[i])
    
#     cursor.execute(sql)
#     db.commit()
#     print("Data are successfully inserted")

# db.close()


'''
資料表都有了 會更動的只有close
下面是創建資料庫 可以驅動網頁的執行順序
0.找到選股目標 擺入目標array
1.把detail的name先存入
2.由yahoo API 抓取close股價 存入etf_close 以及 寫入 成立年限 成立日期 以及是 股票 還是 ETF的三個欄位資料
3.dj資料爬蟲(總費用率)
4.配息率程式執行
5.其他yahoo資料爬蟲
6.年化報酬 年化標準 年報酬 月報酬資料庫
7.資料庫建置完成
'''






import yfinance as yf
import pandas as pd
import numpy as np
import pymysql
import datetime
from dateutil.relativedelta import relativedelta

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


etf_stk = stk + etf

db = pymysql.connect("localhost", "root", "esfortest", "etf")
cursor = db.cursor()
today = datetime.date.today()
for xxx in range(len(etf_stk)):
    print(xxx+1)
    stk = yf.Ticker(etf_stk[xxx])
    # 取得 2000 年至今的資料
    data = stk.history(start='1990-01-01')
    # 簡化資料，只取開、高、低、收以及成交量
    data = data[['Close']]
    data['Date'] = data.index
    data.columns = ['close','date']
    data = data.reset_index()
    data = data.drop(['Date'],axis=1)


    found = data['date'][0]
    found_temp = str(found).split(' ')
    found_sql = found_temp[0]
    vary = relativedelta(today,found)
    found_limit = vary.years
    print(etf_stk[xxx])
    print(found_limit)

    length = data.shape[0]

    if etf_stk[xxx] in etf :
        target_type = 'ETF'
    else:
        target_type = 'STOCK'    
    
    # sql = "INSERT INTO detail (`成立年限`,`成立日期`) VALUES WHERE `name` = '" +etf_stk[xxx]+"'"
    # values = "('%s','%s')"
    # sql += values % (found_limit,found_sql)
    sql= "UPDATE detail SET `成立年限` ='%s',`成立日期` ='%s', `類型` ='%s' WHERE `name` ='%s'" % (str(found_limit),str(found_sql),str(target_type),str(etf_stk[xxx]))
    cursor.execute(sql)
    db.commit()
    print("Data are successfully inserted1")

    # 把input_data寫成sql語法
    for i in range(length):
        sql = "INSERT INTO etf_close (`name`,`date`,`close`) VALUES"
        values = "('%s','%s','%s')"
        sql += values % (etf_stk[xxx],data['date'][i],data['close'][i])
        cursor.execute(sql)
        db.commit()
    print("Data are successfully inserted2")

db.close()

# DELETE FROM `etf_close` WHERE close = 'nan'


import yfinance as yf
import pandas as pd
import numpy as np
import pymysql
import datetime


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




db = pymysql.connect("localhost", "root", "esfortest", "etf")
cursor = db.cursor()


sql = "CREATE TABLE close( date date," 

for i in range(len(etf_stk)):
    if i == (len(etf_stk)-1):
        sql = sql + etf_stk[i] + ' double)'
    else:
        sql = sql + etf_stk[i] + ' double,'
print(sql)
cursor.execute(sql)
db.commit()

stk = yf.Ticker(etf_stk[0])
# 取得 2000 年至今的資料
data = stk.history(start='1990-01-01')
# 簡化資料，只取開、高、低、收以及成交量
data = data[['Close']]

for xxx in range(1,len(etf_stk)):
    print(xxx)
    stk = yf.Ticker(etf_stk[xxx])
    # 取得 2000 年至今的資料
    data1 = stk.history(start='1990-01-01')
    # 簡化資料，只取開、高、低、收以及成交量
    data1 = data1[['Close']]
    data = pd.merge(data,data1, left_index=True, right_index=True, how='outer')
    
data.to_csv('C:/Users/User/Downloads/close.csv', encoding='utf_8_sig')




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


etf_stk = stk + etf

db = pymysql.connect("localhost", "root", "esfortest", "etf")
cursor = db.cursor()


sql = "INSERT INTO close (`date`"
value = "("
for i in range(len(etf_stk)):
    sql = sql + ',`' + etf_stk[i] + '`'
    if i ==( len(etf_stk)-1):
        value = value + "'%s'" + ")"
    else:
        value = value + "'%s'" + ","
sql = sql+") VALUES"

# print(sql)
# print(value)

from csv import reader

with open('C:/Users/User/Downloads/close.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    num = 0
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        # print(len(row))
        num += 1
        if num == 1 :
           continue
        temp = str(row)
        temp = temp.replace("'nan'", "NULL")
        temp = temp.replace("[", "(")
        temp = temp.replace("]", ")")
        temp = temp.replace("''", "NULL")
        sql_temp = sql
        sql_temp += temp
        cursor.execute(sql_temp)
        db.commit()


print("Data are successfully inserted2")

db.close()



# CREATE TABLE close_2
# (
# date date,KO varchar(10),PLD varchar(10),CSX varchar(10),MMC varchar(10),AAPL varchar(10),MSFT varchar(10),AMZN varchar(10),FB varchar(10),GOOGL varchar(10),GOOG varchar(10),JNJ varchar(10),V varchar(10),PG varchar(10),NVDA varchar(10),JPM varchar(10),HD varchar(10),MA varchar(10),UNH varchar(10),VZ varchar(10),DIS varchar(10),ADBE varchar(10),CRM varchar(10),PYPL varchar(10),MRK varchar(10),NFLX varchar(10),INTC varchar(10),T varchar(10),CMCSA varchar(10),PFE varchar(10),BAC varchar(10),WMT varchar(10),PEP varchar(10),ABT varchar(10),TMO varchar(10),CSCO varchar(10),MCD varchar(10),ABBV varchar(10),XOM varchar(10),ACN varchar(10),COST varchar(10),NKE varchar(10),AMGN varchar(10),AVGO varchar(10),CVX varchar(10),MDT varchar(10),NEE varchar(10),BMY varchar(10),UNP varchar(10),LIN varchar(10),DHR varchar(10),QCOM varchar(10),PM varchar(10),TXN varchar(10),LLY varchar(10),LOW varchar(10),ORCL varchar(10),HON varchar(10),UPS varchar(10),AMT varchar(10),IBM varchar(10),SBUX varchar(10),C varchar(10),LMT varchar(10),MMM varchar(10),WFC varchar(10),CHTR varchar(10),RTX varchar(10),AMD varchar(10),FIS varchar(10),BA varchar(10),NOW varchar(10),SPGI varchar(10),BLK varchar(10),ISRG varchar(10),GILD varchar(10),CAT varchar(10),MDLZ varchar(10),INTU varchar(10),MO varchar(10),ZTS varchar(10),CVS varchar(10),TGT varchar(10),BKNG varchar(10),AXP varchar(10),BDX varchar(10),VRTX varchar(10),DE varchar(10),D varchar(10),ANTM varchar(10),EQIX varchar(10),CCI varchar(10),APD varchar(10),SYK varchar(10),CL varchar(10),TMUS varchar(10),CI varchar(10),GS varchar(10),DUK varchar(10),MS varchar(10),ATVI varchar(10),SPY varchar(10),IVV varchar(10),VTI varchar(10),VOO varchar(10),QQQ varchar(10),AGG varchar(10),GLD varchar(10),VEA varchar(10),IEFA varchar(10),BND varchar(10),VWO varchar(10),VUG varchar(10),IWF varchar(10),LQD varchar(10),IEMG varchar(10),VTV varchar(10),EFA varchar(10),VIG varchar(10),IJH varchar(10),IJR varchar(10),IWM varchar(10),VCIT varchar(10),IWD varchar(10),VGT varchar(10),XLK varchar(10),VO varchar(10),USMV varchar(10),IAU varchar(10),VCSH varchar(10),BNDX varchar(10),IVW varchar(10),HYG varchar(10),VNQ varchar(10),VB varchar(10),ITOT varchar(10),VYM varchar(10),BSV varchar(10),VXUS varchar(10),VEU varchar(10),EEM varchar(10),XLV varchar(10),TIP varchar(10),IWB varchar(10),DIA varchar(10),SCHX varchar(10),MBB varchar(10),IXUS varchar(10),SHY varchar(10),SHV varchar(10),IWR varchar(10),IGSB varchar(10),IEF varchar(10),SCHF varchar(10),QUAL varchar(10),VV varchar(10),GDX varchar(10),XLF varchar(10),MUB varchar(10),TLT varchar(10),PFF varchar(10),EMB varchar(10),IVE varchar(10),SCHB varchar(10),XLY varchar(10),SDY varchar(10),SLV varchar(10),GOVT varchar(10),MDY varchar(10),BIV varchar(10),XLP varchar(10),VT varchar(10),BIL varchar(10),JPST varchar(10),MINT varchar(10),VBR varchar(10),RSP varchar(10),JNK varchar(10),DVY varchar(10),IWP varchar(10),SCHD varchar(10),VGK varchar(10),ACWI varchar(10),SCHP varchar(10),SCHG varchar(10),XLI varchar(10),XLU varchar(10),DGRO varchar(10),VMBS varchar(10),VHT varchar(10),MTUM varchar(10),IGIB varchar(10),IEI varchar(10),VBK varchar(10),EFAV varchar(10),XLC varchar(10),IWS varchar(10),GSLC varchar(10),EWJ varchar(10),FDN varchar(10),SCHA
# );




























# import numpy as np
# import pandas as pd
# def pla():
#     # TODO: start coding here... 
#     # the first thing is to read `pla.dat`
#     # f  = open('./pla.dat', 'r')
#     # print(f.read())
#     df = pd.read_table("./pla.dat", sep="\s+", header=None)
#     length = df.shape[0]
#     w = np.array([1,df[0][0],df[1][0],df[2][0],df[3][0]]) 
#     counter = 0
#     error = 1
#     while( error != 0):
#         counter = counter +1
#         error = 0
#         for i in range(length):
#             x = np.array([1,df[0][i],df[1][i],df[2][i],df[3][i]]) 
#             y = np.sign(w.T.dot(x))
#             if y != df[4][i]:
#                 error = error + 1
#                 w = w + np.array([df[4][i]])*(x)
#     print('#',counter,w)
        

# if True: # TODO: change `False` to `True` once you finish `pla()`
#     pla()
# else:
#     prepared.demo()


