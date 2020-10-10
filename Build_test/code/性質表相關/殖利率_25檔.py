from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import pymysql
import datetime
from selenium.webdriver.chrome.options import Options


# etf = ['GLD','VTI']


temp = 'SPY,IVV,VTI,VOO,QQQ,AGG,GLD,VEA,IEFA,BND,VWO,VUG,IWF,LQD,IEMG,VTV,EFA,VIG,IJH,IJR,IWM,VCIT,IWD,VGT,XLK,VO,USMV,IAU,VCSH,BNDX,IVW,HYG,VNQ,VB,ITOT,VYM,BSV,VXUS,VEU,EEM,XLV,TIP,IWB,DIA,SCHX,MBB,IXUS,SHY,SHV,IWR,IGSB,IEF,SCHF,QUAL,VV,GDX,XLF,MUB,TLT,PFF,EMB,IVE,SCHB,XLY,SDY,SLV,GOVT,MDY,BIV,XLP,VT,BIL,JPST,MINT,VBR,RSP,JNK,DVY,IWP,SCHD,VGK,ACWI,SCHP,SCHG,XLI,XLU,DGRO,VMBS,VHT,MTUM,IGIB,IEI,VBK,EFAV,XLC,IWS,GSLC,EWJ,FDN,SCHA'
temp_arr = temp.split(',')
etf = []
for i in range(100):
    etf.append(temp_arr[i])


year = ["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010",
               "2011","2012","2013","2014","2015","2016","2017","2018","2019","2020"]

#driver = webdriver.Chrome("D:/Alia/Downloads/108-1/project/chromedriver_win32/chromedriver.exe")

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


avg_div = np.zeros(len(etf))
print(avg_div)
a=0
while a<len(etf) :
#while a<1 :
    print(etf[a])
    #配息爬蟲
    driver = webdriver.Chrome("C:/Users/User/Downloads/安裝檔案/chromedriver.exe", chrome_options = chrome_options)
    url = "https://www.moneydj.com/ETF/X/Basic/Basic0005.xdjhtm?etfid="
    url += etf[a]
    print(url)
    driver.get(url)
    
    soup = bs(driver.page_source,"html.parser")
    raw_data = [data.text for data in soup.find_all("td",["col01","col02","col03","col07"])]
    
    sql = "INSERT INTO 配息紀錄 (`配息基準日`, `除息日`, `發放日`, `配息總額` ) VALUES"
    							
    values = "('%s','%s','%s','%s')"
    
    #print(len(raw_data))
    i = 0
    while(i < len(raw_data)):
        if (i < len(raw_data)-5):
            sql += values % (raw_data[i], raw_data[i + 1], raw_data[i + 2], raw_data[i + 3]) + ","
        else:
            sql += values % (raw_data[i], raw_data[i + 1], raw_data[i + 2], raw_data[i + 3]) 
        i += 4
    
    #print(sql)
    # print()
    driver.close()
    
    # 抓到的配息入資料庫
    db = pymysql.connect("localhost", "root", "esfortest", "etf")
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        print("Data are successfully inserted")
    except Exception as e:
        db.rollback()
        print("Exception Occured : ", e)
        a+=1
        continue
    #配息爬蟲結束
    
    
    
    #計算每次的配息率
    sql="SELECT * FROM `配息紀錄`"
    cursor.execute(sql)
    result_select_div = cursor.fetchall()
    db.commit()
    
    sql3 = "INSERT INTO 配息率 (`date`, `配息率` ) VALUES"
    values = "('%s','%s')"
    
    i=0
    k=1
    #每筆找相對應日期的市價並相除
    while i<len(result_select_div):
        sql2 = "select * from etf_close where (name = '"+etf[a]+"' and date = '"#從yahoo匯入的找市價
        sql2 += (str(result_select_div[i][k]) +"')")
        print(sql2)
        cursor.execute(sql2)
        result_select_close = cursor.fetchall()
        db.commit()
        print(result_select_close)
        if len(result_select_close)==0:
            dividend = 0
            close = 0
        else:
            close = float(result_select_close[0][2])
            dividend = float(result_select_div[i][3])
        # print(result_select_div[i][k])
        # print(close)
        # print(dividend)
        if close!=0:
            div_percent = dividend/close
        else:
            div_percent = 0
        # print(div_percent)
        if(i<len(result_select_div)-1):
            sql3 += values % (result_select_div[i][k], div_percent) +","
        else:
            sql3 += values % (result_select_div[i][k], div_percent)
        #print(sql3)
        i+=1
    
    print(sql3)
    
    #每次配息率入資料庫
    try:
        cursor.execute(sql3)
        db.commit()
        print("Div_percent are successfully inserted")
    except Exception as e:
        db.rollback()
        print("Exception Occured : ", e)
    #db.close
    #計算每次配息率結束
    
    
    #計算年平均配息率
    now_year = 2019
    now_year -= 2000
    i = 0
    dividend = np.empty(now_year+1)
    freq = np.empty(now_year+1)
    
    #每年分別抓出來算總和與配息次數
    while i<=now_year :
        sql = "select * from 配息率 where date like '" + year[i]+"%'"
        cursor.execute(sql)
        result_select = cursor.fetchall()
        db.commit()
        # print(i)
        # print(result_select)
        dividend[i] = 0
        j=0
        freq[i] = len(result_select)
        while j<len(result_select) :
            dividend[i] += float(result_select[j][1])
            j+=1
        # print(dividend[i])
        # print(freq[i])
        i+=1
    #db.close()
    
    # print(dividend)
    # print(freq)
    
    #算平均
    count = 0
    total = 0.0 
    i=0
    freq_year = freq[now_year-1]
    # print(freq_year)
    # print(dividend[i] *freq_year /freq[i])
    while i < len(dividend):
        #total += (dividend[i] *freq_year /freq[i])
        if(dividend[i]!=0):
            total += (dividend[i] *freq_year /freq[i])
            count+=1
        i+=1
    # print(total)
    # print(count)
    avg_dividend = total/count
    print(avg_dividend)
    avg_div[a] = avg_dividend
    
    #計算年平均配息率結束
    
    
    #清空資料庫
    #db = pymysql.connect("localhost", "root", "esfortest", "etf")
    #cursor = db.cursor()
    
    sql_del1 = "TRUNCATE TABLE `配息率`"
    try:
        cursor.execute(sql_del1)
        db.commit()
        print("delete1 successful")
    except Exception as e:
        db.rollback()
        print("Exception Occured : ", e)
    sql_del2 = "TRUNCATE TABLE `配息紀錄`"
    try:
        cursor.execute(sql_del2)
        db.commit()
        print("delete2 successful")
    except Exception as e:
        db.rollback()
        print("Exception Occured : ", e)
    db.close()
    print(etf[a]+' end')
    print()
    a+=1

print(avg_div)
#[0.0168106  0.02033887 0.04343551 0.01860585 0.031083   0.01811477 0.01843766 0.0444699  0.02534931 0.01579987 0.0122712  0.02636138
# 0.05635492 0.0276834  0.00949157 0.02104849 0.03353616 0.02008875 0.0364111  0.03023534 0.01915196 0.03689285 0.02206909 0.03907675 0.01410118]
# [0.02124299 0.01981818 0.04267185 0.01837447 0.03090534 0.01811477
#  0.01830685 0.0439066  0.02509347 0.01211015 0.02612884 0.05580605
#  0.02719655 0.00937193 0.02090058 0.03335623 0.019201   0.03604143
#  0.03013608 0.01915196 0.03689285 0.02206909 0.03860267 0.01389153]
db = pymysql.connect("localhost", "root", "esfortest", "etf")
cursor = db.cursor()
i=0
while i<len(etf):
    sql = 'UPDATE detail SET 配息率 = '+ str(avg_div[i]) +" WHERE name = '"+etf[i]+"'"
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print("Data are successfully update")
    except Exception as e:
        db.rollback()
        print("Exception Occured : ", e)
    i+=1
db.close


# 0.02522597



