
from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import pymysql
import datetime
from selenium.webdriver.chrome.options import Options
import requests
import datetime
from dateutil.parser import parse 

# temp = 'AAPL,MSFT,AMZN,FB,GOOGL,GOOG,BRK.B,JNJ,V,PG,NVDA,JPM,HD,MA,UNH,VZ,DIS,ADBE,CRM,PYPL,MRK,NFLX,INTC,T,CMCSA,PFE,BAC,KO,WMT,PEP,ABT,TMO,CSCO,MCD,ABBV,XOM,ACN,COST,NKE,AMGN,AVGO,CVX,MDT,NEE,BMY,UNP,LIN,DHR,QCOM,PM,TXN,LLY,LOW,ORCL,HON,UPS,AMT,IBM,SBUX,C,LMT,MMM,WFC,CHTR,RTX,AMD,FIS,BA,NOW,SPGI,BLK,ISRG,GILD,CAT,MDLZ,INTU,MO,ZTS,CVS,PLD,TGT,BKNG,AXP,BDX,VRTX,DE,D,ANTM,EQIX,CCI,APD,TJX,SYK,CL,TMUS,CI,GS,DUK,MS,ATVI'
temp = 'KO,PLD,CSX,MMC,AAPL,MSFT,AMZN,FB,GOOGL,GOOG,JNJ,V,PG,NVDA,JPM,HD,MA,UNH,VZ,DIS,ADBE,CRM,PYPL,MRK,NFLX,INTC,T,CMCSA,PFE,BAC,WMT,PEP,ABT,TMO,CSCO,MCD,ABBV,XOM,ACN,COST,NKE,AMGN,AVGO,CVX,MDT,NEE,BMY,UNP,LIN,DHR,QCOM,PM,TXN,LLY,LOW,ORCL,HON,UPS,AMT,IBM,SBUX,C,LMT,MMM,WFC,CHTR,RTX,AMD,FIS,BA,NOW,SPGI,BLK,ISRG,GILD,CAT,MDLZ,INTU,MO,ZTS,CVS,TGT,BKNG,AXP,BDX,VRTX,DE,D,ANTM,EQIX,CCI,APD,SYK,CL,TMUS,CI,GS,DUK,MS,ATVI'
temp_arr = temp.split(',')
stk = []
for i in range(100):
    stk.append(temp_arr[i])

# temp = 'VTI,VOO,VXUS,SPY,BND,IVV,BNDX,QQQ,VUG,VEA,VO,1306,VB,VWO,VTV,AGG,GLD,2840,VXF,IEFA,IWF,VNQ,1321,LQD,BSV,IEMG,VIG,EFA,IJH,IJR,IWM,VCIT,VEU,VGT,BIV,XLK,IWD,VCSH,VTIP,USMV,VYM,IVW,IAU,HYG,ITOT,VV,VBR,VBK,IWB,XLV,EEM,TIP,DIA,SCHX,MBB,SHY,IWR,IXUS,IGSB,SCHF,QUAL,SHV,IEF,VT,XLF,GDX,TLT,VOE,MUB,VOT,PFF,SCHB,VGK,EMB,IVE,XLY,SLV,SDY,MDY,GOVT,MINT,XLP,JPST,BIL,IWP,JNK,RSP,VHT,DVY,SCHD,BLV,VGSH,SCHG,ACWI,VMBS,XLU,MTUM,SCHP,DGRO,XLI'
# temp = 'SPY,IVV,VTI,VOO,QQQ,AGG,GLD,VEA,IEFA,BND,VWO,VUG,IWF,LQD,IEMG,VTV,EFA,VIG,IJH,IJR,IWM,VCIT,IWD,VGT,XLK,VO,USMV,IAU,VCSH,BNDX,IVW,HYG,VNQ,VB,ITOT,VYM,BSV,VXUS,VEU,EEM,XLV,TIP,IWB,DIA,SCHX,MBB,IXUS,SHY,SHV,IWR,IGSB,IEF,SCHF,QUAL,VV,GDX,XLF,MUB,TLT,PFF,EMB,IVE,SCHB,XLY,SDY,SLV,GOVT,MDY,BIV,XLP,VT,BIL,JPST,MINT,VBR,RSP,JNK,DVY,IWP,SCHD,VGK,ACWI,SCHP,SCHG,XLI,XLU,DGRO,VMBS,VHT,MTUM,IGIB,IEI,VBK,EFAV,XLC,IWS,GSLC,EWJ,FDN,SCHA'
# temp_arr = temp.split(',')
# etf = []
# for i in range(100):
#     etf.append(temp_arr[i])


etf = stk

url1 = 'https://finance.yahoo.com/quote/'
url2 = '?p='
url3 = '/key-statistics?p='




# url4 = '?p='
# url5 = '/profile?p='
# url6 = '/risk?p='

Avg_Volume = []
Market_Cap = []
Beta = []
EPS = []
PE_Ratio = []



driver = webdriver.Chrome("C:/Users/User/Downloads/安裝檔案/chromedriver.exe")
i = 0
while i < len(etf):   
    print(i) 
    print(etf[i])
    #根據ETF列表重複執行抓取資料的動作
    url = url1 + etf[i] + url2 + etf[i] + '&.tsrc=fin-srch'
    driver.get(url)
    time.sleep(5)
    soup = bs(driver.page_source,"html.parser")
    # click
    try :
        raw_data = [data.text for data in soup.find('td',{'class':['Ta(end) Fw(600) Lh(14px)'],'data-test':["AVERAGE_VOLUME_3MONTH-value"]})]
        Avg_Volume.append(raw_data[0])
        print('Avg_Volume')
        print(Avg_Volume[i])

        raw_data = [data.text for data in soup.find('td',{'class':['Ta(end) Fw(600) Lh(14px)'],'data-test':["MARKET_CAP-value"]})]
        Market_Cap.append(raw_data[0])
        print('Market_Cap')
        print(Market_Cap[i])

        raw_data = [data.text for data in soup.find('td',{'class':['Ta(end) Fw(600) Lh(14px)'],'data-test':["BETA_5Y-value"]})]
        Beta.append(raw_data[0])
        print('Beta')
        print(Beta[i])

        raw_data = [data.text for data in soup.find('td',{'class':['Ta(end) Fw(600) Lh(14px)'],'data-test':["EPS_RATIO-value"]})]
        EPS.append(raw_data[0])
        print('EPS')
        print(EPS[i])

        raw_data = [data.text for data in soup.find('td',{'class':['Ta(end) Fw(600) Lh(14px)'],'data-test':["PE_RATIO-value"]})]
        PE_Ratio.append(raw_data[0])
        print('PE_Ratio')
        print(PE_Ratio[i])
        i = i + 1
    except:
        print("problem")
        driver.close()
        driver = webdriver.Chrome("C:/Users/User/Downloads/安裝檔案/chromedriver.exe")

    time.sleep(2)


# close the driver
driver.close()


print(Avg_Volume)
print(Market_Cap)
print(Beta)
print(EPS)
print(PE_Ratio)


# ['15,504,100', '2,901,482', '3,606,384', '1,606,592', '171,525,540', '34,883,515', '4,910,821', '26,373,128', '1,802,903', '1,808,960', '6,093,221', '8,113,006', '6,592,990', '12,261,015', '18,557,926', '3,618,032', '3,703,814', '2,831,303', '14,155,679', '11,654,262', '2,992,473', '7,993,460', '7,797,107', '8,139,043', '7,417,185', '33,851,618', '34,487,070', '17,940,193', '28,328,825', '61,876,489', '10,364,714', '4,108,392', '5,313,260', '1,337,957', '23,106,420', '3,093,050', '6,984,414', '22,727,739', '1,831,300', '2,081,867', '6,202,953', '2,586,443', '1,985,354', '8,973,531', '4,835,715', '1,788,259', '11,072,012', '2,881,064', '1,885,009', '2,128,445', '9,285,357', '4,326,056', '4,422,334', '2,928,200', '3,985,801', '14,620,423', '3,400,037', '4,305,107', '1,629,818', '4,591,432', '8,427,989', '23,100,395', '1,269,143', '2,587,201', '43,129,839', '928,007', '8,829,303', '61,303,992', '3,377,664', '34,860,071', '1,684,600', '900,885', '625,490', '612,490', '8,745,329', '3,157,965', '5,837,329', '1,229,542', '7,429,753', '1,482,532', '7,547,582', '4,290,267', '361,585', '4,193,751', '1,562,112', '1,378,131', '1,555,943', '4,290,865', '1,156,239', '379,073', '1,947,551', '1,100,784', '1,392,623', '3,295,014', '7,072,276', '1,898,632', '3,384,790', '3,513,732', '10,053,406', '6,669,817']
# ['217.134B', '74.689B', '60.822B', '59.71B', '1.887T', '1.536T', '1.507T', '725.936B', '1.014T', '1.014T', '387.472B', '450.658B', '342.373B', '307.955B', '300.371B', '301.366B', '339.79B', '289.833B', '250.394B', '235.315B', '227.505B', '222.522B', '206.254B', '216.604B', '207.365B', '214.011B', '207.124B', '211.634B', '209.101B', '219.635B', '387.345B', '184.433B', '188.845B', '171.262B', '170.904B', '165.622B', '158.182B', '159.827B', '150.877B', '149.624B', '181.509B', '145.299B', '148.015B', '147.124B', '144.92B', '136.866B', '133.883B', '136.888B', '131.545B', '146.954B', '129.616B', '123.758B', '134.018B', '145.833B', '123.774B', '180.971B', '119.542B', '144.697B', '113.059B', '111.251B', '101.411B', '95.616B', '110.682B', '99.294B', '103.665B', '127.101B', '97.749B', '89.874B', '92.203B', '94.562B', '87.039B', '84.767B', '87.794B', '79.679B', '81.542B', '83.322B', '81.715B', '80.435B', '75.934B', '76.247B', '76.441B', '73.896B', '73.184B', '84.268B', '66.032B', '74.532B', '70.983B', '67.06B', '66.146B', '70.18B', '68.259B', '69.653B', '79.467B', '65.771B', '145.684B', '62.057B', '67.036B', '62.471B', '79.232B', '60.8B']
# ['0.55', '0.91', '1.16', '0.83', '1.28', '0.89', '1.32', '1.26', '1.08', '1.08', '0.68', '0.90', '0.41', '1.53', '1.14', '1.09', '1.10', '0.69', '0.43', '1.08', '0.94', '1.24', '1.14', '0.47', '0.97', '0.71', '0.64', '0.96', '0.66', '1.55', '0.29', '0.58', '0.95', '1.01', '0.82', '0.68', '0.72', '1.26', '1.02', '0.69', '0.84', '0.85', '0.95', '1.22', '0.69', '0.21', '0.68', '1.03', '0.74', '0.86', '1.39', '0.79', '1.13', '0.18', '1.49', '0.82', '1.08', '1.00', '0.38', '1.17', '0.81', '1.74', '0.93', '0.97', '1.08', '1.06', '0.82', '2.28', '0.73', '1.37', '1.29', '1.03', '1.24', '0.97', '0.58', '1.11', '0.63', '0.95', '0.50', '0.75', '0.65', '0.87', '1.13', '1.14', '0.86', '0.85', '1.00', '0.38', '0.91', '0.38', '0.34', '0.93', '0.84', '0.56', '0.31', '0.67', '1.42', '0.28', '1.44', '0.68']
# ['2.12', '2.54', '3.72', '3.96', '3.30', '5.76', '26.04', '8.18', '45.49', '45.49', '5.68', '5.26', '4.96', '5.44', '7.47', '10.92', '7.23', '17.79', '4.62', '-0.61', '7.58', '2.59', '2.18', '4.10', '5.92', '5.44', '1.64', '2.49', '2.53', '2.08', '6.27', '4.90', '1.73', '9.24', '2.64', '6.33', '4.52', '1.68', '7.64', '8.36', '1.60', '12.24', '5.32', '-4.66', '3.26', '7.24', '-0.28', '8.06', '4.23', '4.68', '2.36', '4.67', '5.33', '6.15', '7.50', '3.18', '8.14', '5.03', '4.31', '8.81', '1.13', '5.86', '22.82', '8.81', '0.93', '10.45', 'N/A', '0.51', '0.05', '-5.03', '3.55', '10.60', '28.42', '9.50', '-0.20', '7.49', '2.33', '6.92', '-0.50', '3.37', '6.29', '6.92', '60.94', '4.86', '2.84', '7.92', '8.58', '0.56', '22.99', '5.76', '1.74', '8.56', '4.21', '2.99', '2.80', '14.04', '13.26', '2.80', '5.52', '2.34']
# ['23.84', '39.77', '21.35', '29.78', '33.48', '35.23', '115.56', '31.16', '32.69', '32.87', '25.89', '39.01', '27.72', '91.58', '13.20', '25.64', '46.97', '17.14', '13.11', 'N/A', '62.58', '94.38', '80.67', '20.87', '79.40', '9.24', '17.73', '18.31', '14.58', '12.20', '21.81', '27.17', '61.62', '46.86', '15.29', '35.18', '19.82', '22.51', '30.99', '40.54', '72.72', '20.27', '68.72', 'N/A', '33.07', '38.61', 'N/A', '25.03', '59.19', '44.24', '48.78', '17.02', '26.36', '24.79', '21.83', '18.92', '20.93', '31.76', '58.19', '14.18', '77.04', '7.77', '17.35', '19.56', '27.06', '59.33', 'N/A', '148.93', '2,861.73', 'N/A', '127.98', '33.17', '19.30', '71.69', 'N/A', '20.55', '24.52', '44.40', 'N/A', '47.60', '9.28', '21.33', '29.33', '21.53', '80.35', '34.26', '25.64', '141.52', '11.44', '131.10', '93.58', '35.30', '50.25', '25.66', '40.03', '12.04', '14.70', '30.24', '9.10', '33.65']








from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import pymysql
import datetime
from selenium.webdriver.chrome.options import Options
import requests
import datetime
from dateutil.parser import parse 

# temp = 'AAPL,MSFT,AMZN,FB,GOOGL,GOOG,BRK.B,JNJ,V,PG,NVDA,JPM,HD,MA,UNH,VZ,DIS,ADBE,CRM,PYPL,MRK,NFLX,INTC,T,CMCSA,PFE,BAC,KO,WMT,PEP,ABT,TMO,CSCO,MCD,ABBV,XOM,ACN,COST,NKE,AMGN,AVGO,CVX,MDT,NEE,BMY,UNP,LIN,DHR,QCOM,PM,TXN,LLY,LOW,ORCL,HON,UPS,AMT,IBM,SBUX,C,LMT,MMM,WFC,CHTR,RTX,AMD,FIS,BA,NOW,SPGI,BLK,ISRG,GILD,CAT,MDLZ,INTU,MO,ZTS,CVS,PLD,TGT,BKNG,AXP,BDX,VRTX,DE,D,ANTM,EQIX,CCI,APD,TJX,SYK,CL,TMUS,CI,GS,DUK,MS,ATVI'
temp = 'KO,PLD,CSX,MMC,AAPL,MSFT,AMZN,FB,GOOGL,GOOG,JNJ,V,PG,NVDA,JPM,HD,MA,UNH,VZ,DIS,ADBE,CRM,PYPL,MRK,NFLX,INTC,T,CMCSA,PFE,BAC,WMT,PEP,ABT,TMO,CSCO,MCD,ABBV,XOM,ACN,COST,NKE,AMGN,AVGO,CVX,MDT,NEE,BMY,UNP,LIN,DHR,QCOM,PM,TXN,LLY,LOW,ORCL,HON,UPS,AMT,IBM,SBUX,C,LMT,MMM,WFC,CHTR,RTX,AMD,FIS,BA,NOW,SPGI,BLK,ISRG,GILD,CAT,MDLZ,INTU,MO,ZTS,CVS,TGT,BKNG,AXP,BDX,VRTX,DE,D,ANTM,EQIX,CCI,APD,SYK,CL,TMUS,CI,GS,DUK,MS,ATVI'
temp_arr = temp.split(',')
stk = []
for i in range(100):
    stk.append(temp_arr[i])

# temp = 'VTI,VOO,VXUS,SPY,BND,IVV,BNDX,QQQ,VUG,VEA,VO,1306,VB,VWO,VTV,AGG,GLD,2840,VXF,IEFA,IWF,VNQ,1321,LQD,BSV,IEMG,VIG,EFA,IJH,IJR,IWM,VCIT,VEU,VGT,BIV,XLK,IWD,VCSH,VTIP,USMV,VYM,IVW,IAU,HYG,ITOT,VV,VBR,VBK,IWB,XLV,EEM,TIP,DIA,SCHX,MBB,SHY,IWR,IXUS,IGSB,SCHF,QUAL,SHV,IEF,VT,XLF,GDX,TLT,VOE,MUB,VOT,PFF,SCHB,VGK,EMB,IVE,XLY,SLV,SDY,MDY,GOVT,MINT,XLP,JPST,BIL,IWP,JNK,RSP,VHT,DVY,SCHD,BLV,VGSH,SCHG,ACWI,VMBS,XLU,MTUM,SCHP,DGRO,XLI'
# temp = 'SPY,IVV,VTI,VOO,QQQ,AGG,GLD,VEA,IEFA,BND,VWO,VUG,IWF,LQD,IEMG,VTV,EFA,VIG,IJH,IJR,IWM,VCIT,IWD,VGT,XLK,VO,USMV,IAU,VCSH,BNDX,IVW,HYG,VNQ,VB,ITOT,VYM,BSV,VXUS,VEU,EEM,XLV,TIP,IWB,DIA,SCHX,MBB,IXUS,SHY,SHV,IWR,IGSB,IEF,SCHF,QUAL,VV,GDX,XLF,MUB,TLT,PFF,EMB,IVE,SCHB,XLY,SDY,SLV,GOVT,MDY,BIV,XLP,VT,BIL,JPST,MINT,VBR,RSP,JNK,DVY,IWP,SCHD,VGK,ACWI,SCHP,SCHG,XLI,XLU,DGRO,VMBS,VHT,MTUM,IGIB,IEI,VBK,EFAV,XLC,IWS,GSLC,EWJ,FDN,SCHA'
# temp_arr = temp.split(',')
# etf = []
# for i in range(100):
#     etf.append(temp_arr[i])


etf = stk

url1 = 'https://finance.yahoo.com/quote/'
url2 = '?p='
url3 = '/key-statistics?p='


Profit_Margin = []
ROA = []
ROE = []
Held_by_Insiders = []
Held_by_Institutions = []


driver = webdriver.Chrome("C:/Users/User/Downloads/安裝檔案/chromedriver.exe")
i=0
while i < len(etf):  
    try :
        print(i) 
        print(etf[i])
        #根據ETF列表重複執行抓取資料的動作
        url = url1 + etf[i] + url3 + etf[i] + '&.tsrc=fin-srch'
        driver.get(url)
        time.sleep(5)
        soup = bs(driver.page_source,"html.parser")

        raw_data = [data.text for data in soup.find_all('td',{'class':['Fw(500) Ta(end) Pstart(10px) Miw(60px)']})]
        # raw_data1 = [data for data in soup.find_all('td',{'class':['Fw(500) Ta(end) Pstart(10px) Miw(60px)']})]

        # for i in range(len(raw_data1)):
        #     print(i)
        #     print(raw_data1[i])
        # click

        # raw_data = [data for data in soup.find('td',{'class':['Fw(500) Ta(end) Pstart(10px) Miw(60px)'],'data-reactid':["463"]})]
        Profit_Margin.append(raw_data[30])
        print('Profit_Margin')
        print(Profit_Margin[i])

        # raw_data = [data for data in soup.find('td',{'class':['Fw(500) Ta(end) Pstart(10px) Miw(60px)'],'data-reactid':["484"]})]
        ROA.append(raw_data[32])
        print('ROA')
        print(ROA[i])

        # raw_data = [data for data in soup.find('td',{'class':['Fw(500) Ta(end) Pstart(10px) Miw(60px)'],'data-reactid':["491"]})]
        ROE.append(raw_data[33])
        print('ROE')
        print(ROE[i])

        # raw_data = [data for data in soup.find('td',{'class':['Fw(500) Ta(end) Pstart(10px) Miw(60px)'],'data-reactid':["305"]})]
        Held_by_Insiders.append(raw_data[11])
        print('Held_by_Insiders')
        print(Held_by_Insiders[i])

        # raw_data = [data for data in soup.find('td',{'class':['Fw(500) Ta(end) Pstart(10px) Miw(60px)'],'data-reactid':["312"]})]
        Held_by_Institutions.append(raw_data[12])
        print('Held_by_Institutions')
        print(Held_by_Institutions[i])

        time.sleep(2)
        i = i + 1
    except:
        print("problem")
        driver.close()
        driver = webdriver.Chrome("C:/Users/User/Downloads/安裝檔案/chromedriver.exe")


# close the driver
driver.close()




print(Profit_Margin)
print(ROA)
print(ROE)
print(Held_by_Insiders)
print(Held_by_Institutions)


# ['26.77%', '40.85%', '26.39%', '11.83%', '21.33%', '30.96%', '4.10%', '31.30%', '18.99%', '18.99%', '18.86%', '51.37%', '18.36%', '25.93%', '25.86%', '9.91%', '45.12%', '6.90%', '14.76%', '-1.58%', '30.71%', '12.21%', '13.44%', '22.20%', '11.85%', '29.97%', '6.84%', '10.91%', '28.81%', '26.53%', '3.30%', '10.13%', '9.89%', '14.12%', '22.75%', '24.95%', '19.20%', '3.35%', '11.11%', '2.31%', '6.79%', '30.04%', '10.70%', '-7.57%', '15.80%', '18.71%', '-1.61%', '27.54%', '8.37%', '18.35%', '13.72%', '24.98%', '36.88%', '24.48%', '7.12%', '26.13%', '16.94%', '5.66%', '24.70%', '10.43%', '5.56%', '23.24%', '10.25%', '16.37%', '9.19%', '4.85%', '-2.03%', '7.96%', '0.25%', '-4.27%', '18.42%', '36.20%', '29.55%', '26.07%', '-1.16%', '8.90%', '13.06%', '23.78%', '-4.50%', '25.51%', '3.14%', '4.16%', '22.52%', '11.89%', '5.37%', '38.51%', '7.61%', '3.24%', '5.24%', '8.81%', '14.51%', '21.58%', '11.38%', '16.13%', '5.18%', '3.40%', '14.48%', '8.97%', '21.25%', '25.94%']
# ['6.59%', '2.10%', '7.19%', '7.56%', '13.12%', '11.26%', '4.65%', '13.58%', '7.78%', '7.78%', '8.05%', '12.73%', '8.57%', '11.67%', '0.85%', '18.09%', '19.79%', '8.46%', '6.72%', '1.97%', '11.44%', '0.15%', '3.27%', '11.19%', '6.97%', '11.63%', '3.35%', '4.80%', '5.49%', '0.79%', '6.62%', '7.93%', '4.01%', '4.87%', '9.16%', '9.41%', '8.23%', '0.65%', '12.93%', '6.82%', '7.07%', '9.30%', '3.42%', '-0.20%', '2.83%', '3.15%', '5.16%', '8.18%', '2.69%', '3.31%', '6.56%', '17.35%', '19.11%', '9.90%', '11.80%', '8.29%', '7.12%', '6.13%', '4.66%', '3.62%', '4.70%', '0.65%', '10.60%', '9.93%', '0.30%', '3.14%', '3.69%', '9.46%', '1.67%', '-1.44%', '2.21%', '21.98%', '2.03%', '7.56%', '4.37%', '4.93%', '3.86%', '15.80%', '13.19%', '11.78%', '3.82%', '7.37%', '9.65%', '2.11%', '2.84%', '15.25%', '3.30%', '3.60%', '6.56%', '2.61%', '2.50%', '6.38%', '6.31%', '16.30%', '3.29%', '3.66%', '0.52%', '2.23%', '1.02%', '7.12%']
# ['46.64%', '6.06%', '23.69%', '24.50%', '69.25%', '40.14%', '20.79%', '23.61%', '15.79%', '15.79%', '24.54%', '33.34%', '27.74%', '27.94%', '9.53%', 'N/A', '125.61%', '27.62%', '32.25%', '-0.87%', '35.55%', '8.51%', '15.27%', '37.85%', '34.73%', '30.15%', '6.80%', '14.19%', '22.81%', '7.56%', '22.90%', '51.81%', '9.86%', '12.65%', '31.37%', 'N/A', '225.62%', '3.65%', '32.82%', '23.51%', '29.70%', '68.05%', '11.02%', '-6.02%', '8.76%', '7.66%', '-1.65%', '32.14%', '4.67%', '8.60%', '62.58%', 'N/A', '62.60%', '157.61%', '163.64%', '70.30%', '32.62%', '99.49%', '34.56%', '40.97%', 'N/A', '7.07%', '193.03%', '48.81%', '3.11%', '6.62%', '1.13%', '23.40%', '0.13%', 'N/A', '38.95%', '108.32%', '13.44%', '14.31%', '-1.40%', '28.92%', '12.99%', '41.24%', '-9.13%', '59.87%', '12.73%', '28.78%', '54.67%', '18.45%', '3.99%', '33.06%', '21.58%', '2.11%', '18.13%', '5.20%', '7.84%', '16.58%', '12.96%', '756.79%', '5.25%', '11.59%', '5.86%', '4.21%', '11.17%', '14.13%']
# ['0.70%', '0.52%', '0.12%', '0.19%', '0.07%', '1.42%', '15.12%', '0.66%', '0.14%', '5.75%', '0.08%', '0.20%', '0.11%', '4.15%', '0.88%', '0.12%', '11.30%', '0.71%', '0.03%', '0.20%', '0.29%', '3.80%', '0.13%', '0.08%', '1.62%', '0.05%', '0.08%', '0.69%', '0.04%', '0.10%', '50.91%', '0.14%', '0.73%', '0.21%', '0.04%', '0.12%', '0.11%', '0.08%', '0.19%', '0.23%', '1.17%', '0.22%', '2.53%', '0.05%', '0.07%', '0.18%', '0.11%', '0.14%', '0.12%', '11.47%', '0.12%', '0.22%', '0.24%', '0.15%', '0.17%', '36.36%', '0.16%', '0.01%', '0.34%', '0.11%', '0.23%', '0.25%', '0.07%', '0.18%', '0.13%', '27.05%', '0.11%', '0.60%', '0.33%', '0.13%', '0.77%', '0.12%', '3.32%', '0.96%', '0.41%', '0.19%', 'N/A', '3.49%', '0.10%', '0.25%', '0.19%', '0.26%', '0.35%', '0.10%', '0.17%', '0.14%', '0.23%', '0.28%', '0.17%', '0.50%', '0.43%', '0.25%', '7.45%', '0.24%', '44.09%', '1.45%', '0.60%', '0.10%', '24.24%', '1.37%']
# ['70.00%', '88.99%', '76.04%', '90.66%', '62.12%', '74.09%', '57.69%', '79.41%', '82.29%', '70.62%', '70.25%', '98.06%', '65.03%', '69.23%', '76.08%', '72.20%', '78.61%', '89.92%', '68.43%', '66.29%', '89.10%', '85.16%', '86.62%', '78.55%', '83.49%', '69.04%', '57.41%', '85.05%', '72.56%', '73.24%', '30.95%', '73.53%', '77.18%', '93.01%', '73.98%', '68.79%', '76.76%', '56.77%', '74.68%', '71.54%', '85.83%', '78.93%', '84.85%', '68.96%', '85.82%', '81.04%', '79.09%', '83.46%', '84.26%', '82.13%', '79.91%', '75.22%', '88.83%', '79.61%', '78.30%', '52.78%', '78.18%', '71.23%', '94.05%', '58.56%', '70.28%', '81.98%', '80.38%', '69.95%', '77.48%', '65.63%', '46.73%', '78.19%', '92.30%', '66.60%', '98.93%', '86.82%', '84.87%', '91.32%', '80.77%', '70.02%', 'N/A', '89.81%', '64.19%', '95.03%', '79.64%', '84.60%', '96.71%', '87.09%', '89.53%', '97.83%', '80.91%', '72.79%', '92.52%', '96.65%', '93.22%', '86.04%', '76.43%', '80.93%', '48.69%', '92.71%', '76.20%', '65.29%', '62.93%', '92.22%']











from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import pymysql
import datetime
from selenium.webdriver.chrome.options import Options
import requests
import datetime
from dateutil.parser import parse 

# temp = 'AAPL,MSFT,AMZN,FB,GOOGL,GOOG,BRK.B,JNJ,V,PG,NVDA,JPM,HD,MA,UNH,VZ,DIS,ADBE,CRM,PYPL,MRK,NFLX,INTC,T,CMCSA,PFE,BAC,KO,WMT,PEP,ABT,TMO,CSCO,MCD,ABBV,XOM,ACN,COST,NKE,AMGN,AVGO,CVX,MDT,NEE,BMY,UNP,LIN,DHR,QCOM,PM,TXN,LLY,LOW,ORCL,HON,UPS,AMT,IBM,SBUX,C,LMT,MMM,WFC,CHTR,RTX,AMD,FIS,BA,NOW,SPGI,BLK,ISRG,GILD,CAT,MDLZ,INTU,MO,ZTS,CVS,PLD,TGT,BKNG,AXP,BDX,VRTX,DE,D,ANTM,EQIX,CCI,APD,TJX,SYK,CL,TMUS,CI,GS,DUK,MS,ATVI'
temp = 'KO,PLD,CSX,MMC,AAPL,MSFT,AMZN,FB,GOOGL,GOOG,JNJ,V,PG,NVDA,JPM,HD,MA,UNH,VZ,DIS,ADBE,CRM,PYPL,MRK,NFLX,INTC,T,CMCSA,PFE,BAC,WMT,PEP,ABT,TMO,CSCO,MCD,ABBV,XOM,ACN,COST,NKE,AMGN,AVGO,CVX,MDT,NEE,BMY,UNP,LIN,DHR,QCOM,PM,TXN,LLY,LOW,ORCL,HON,UPS,AMT,IBM,SBUX,C,LMT,MMM,WFC,CHTR,RTX,AMD,FIS,BA,NOW,SPGI,BLK,ISRG,GILD,CAT,MDLZ,INTU,MO,ZTS,CVS,TGT,BKNG,AXP,BDX,VRTX,DE,D,ANTM,EQIX,CCI,APD,SYK,CL,TMUS,CI,GS,DUK,MS,ATVI'
temp_arr = temp.split(',')
stk = []
for i in range(100):
    stk.append(temp_arr[i])

# temp = 'VTI,VOO,VXUS,SPY,BND,IVV,BNDX,QQQ,VUG,VEA,VO,1306,VB,VWO,VTV,AGG,GLD,2840,VXF,IEFA,IWF,VNQ,1321,LQD,BSV,IEMG,VIG,EFA,IJH,IJR,IWM,VCIT,VEU,VGT,BIV,XLK,IWD,VCSH,VTIP,USMV,VYM,IVW,IAU,HYG,ITOT,VV,VBR,VBK,IWB,XLV,EEM,TIP,DIA,SCHX,MBB,SHY,IWR,IXUS,IGSB,SCHF,QUAL,SHV,IEF,VT,XLF,GDX,TLT,VOE,MUB,VOT,PFF,SCHB,VGK,EMB,IVE,XLY,SLV,SDY,MDY,GOVT,MINT,XLP,JPST,BIL,IWP,JNK,RSP,VHT,DVY,SCHD,BLV,VGSH,SCHG,ACWI,VMBS,XLU,MTUM,SCHP,DGRO,XLI'
# temp = 'SPY,IVV,VTI,VOO,QQQ,AGG,GLD,VEA,IEFA,BND,VWO,VUG,IWF,LQD,IEMG,VTV,EFA,VIG,IJH,IJR,IWM,VCIT,IWD,VGT,XLK,VO,USMV,IAU,VCSH,BNDX,IVW,HYG,VNQ,VB,ITOT,VYM,BSV,VXUS,VEU,EEM,XLV,TIP,IWB,DIA,SCHX,MBB,IXUS,SHY,SHV,IWR,IGSB,IEF,SCHF,QUAL,VV,GDX,XLF,MUB,TLT,PFF,EMB,IVE,SCHB,XLY,SDY,SLV,GOVT,MDY,BIV,XLP,VT,BIL,JPST,MINT,VBR,RSP,JNK,DVY,IWP,SCHD,VGK,ACWI,SCHP,SCHG,XLI,XLU,DGRO,VMBS,VHT,MTUM,IGIB,IEI,VBK,EFAV,XLC,IWS,GSLC,EWJ,FDN,SCHA'
# temp_arr = temp.split(',')
# etf = []
# for i in range(100):
#     etf.append(temp_arr[i])


etf = stk

url1 = 'https://finance.yahoo.com/quote/'
url2 = '?p='
url3 = '/key-statistics?p='


Profit_Margin = []
ROA = []
ROE = []
Held_by_Insiders = []
Held_by_Institutions = []


driver = webdriver.Chrome("C:/Users/User/Downloads/安裝檔案/chromedriver.exe")
i=0
while i < len(etf):  
    try :
        print(i) 
        print(etf[i])
        #根據ETF列表重複執行抓取資料的動作
        url = url1 + etf[i] + url3 + etf[i] + '&.tsrc=fin-srch'
        driver.get(url)
        time.sleep(5)
        soup = bs(driver.page_source,"html.parser")

        raw_data = [data.text for data in soup.find_all('td',{'class':['Fw(500) Ta(end) Pstart(10px) Miw(60px)']})]
        # raw_data1 = [data for data in soup.find_all('td',{'class':['Fw(500) Ta(end) Pstart(10px) Miw(60px)']})]

        # for i in range(len(raw_data1)):
        #     print(i)
        #     print(raw_data1[i])
        # click

        # raw_data = [data for data in soup.find('td',{'class':['Fw(500) Ta(end) Pstart(10px) Miw(60px)'],'data-reactid':["463"]})]
        Profit_Margin.append(raw_data[30])
        print('Profit_Margin')
        print(Profit_Margin[i])

        # raw_data = [data for data in soup.find('td',{'class':['Fw(500) Ta(end) Pstart(10px) Miw(60px)'],'data-reactid':["484"]})]
        ROA.append(raw_data[32])
        print('ROA')
        print(ROA[i])

        # raw_data = [data for data in soup.find('td',{'class':['Fw(500) Ta(end) Pstart(10px) Miw(60px)'],'data-reactid':["491"]})]
        ROE.append(raw_data[33])
        print('ROE')
        print(ROE[i])

        # raw_data = [data for data in soup.find('td',{'class':['Fw(500) Ta(end) Pstart(10px) Miw(60px)'],'data-reactid':["305"]})]
        Held_by_Insiders.append(raw_data[11])
        print('Held_by_Insiders')
        print(Held_by_Insiders[i])

        # raw_data = [data for data in soup.find('td',{'class':['Fw(500) Ta(end) Pstart(10px) Miw(60px)'],'data-reactid':["312"]})]
        Held_by_Institutions.append(raw_data[12])
        print('Held_by_Institutions')
        print(Held_by_Institutions[i])

        time.sleep(2)
        i = i + 1
    except:
        print("problem")
        driver.close()
        driver = webdriver.Chrome("C:/Users/User/Downloads/安裝檔案/chromedriver.exe")


# close the driver
driver.close()

from itertools import combinations, permutations
from scipy.special import comb, perm
print(comb(50,8))


print(Profit_Margin)
print(ROA)
print(ROE)
print(Held_by_Insiders)
print(Held_by_Institutions)


# ['26.77%', '40.85%', '26.39%', '11.83%', '21.33%', '30.96%', '4.10%', '31.30%', '18.99%', '18.99%', '18.86%', '51.37%', '18.36%', '25.93%', '25.86%', '9.91%', '45.12%', '6.90%', '14.76%', '-1.58%', '30.71%', '12.21%', '13.44%', '22.20%', '11.85%', '29.97%', '6.84%', '10.91%', '28.81%', '26.53%', '3.30%', '10.13%', '9.89%', '14.12%', '22.75%', '24.95%', '19.20%', '3.35%', '11.11%', '2.31%', '6.79%', '30.04%', '10.70%', '-7.57%', '15.80%', '18.71%', '-1.61%', '27.54%', '8.37%', '18.35%', '13.72%', '24.98%', '36.88%', '24.48%', '7.12%', '26.13%', '16.94%', '5.66%', '24.70%', '10.43%', '5.56%', '23.24%', '10.25%', '16.37%', '9.19%', '4.85%', '-2.03%', '7.96%', '0.25%', '-4.27%', '18.42%', '36.20%', '29.55%', '26.07%', '-1.16%', '8.90%', '13.06%', '23.78%', '-4.50%', '25.51%', '3.14%', '4.16%', '22.52%', '11.89%', '5.37%', '38.51%', '7.61%', '3.24%', '5.24%', '8.81%', '14.51%', '21.58%', '11.38%', '16.13%', '5.18%', '3.40%', '14.48%', '8.97%', '21.25%', '25.94%']
# ['6.59%', '2.10%', '7.19%', '7.56%', '13.12%', '11.26%', '4.65%', '13.58%', '7.78%', '7.78%', '8.05%', '12.73%', '8.57%', '11.67%', '0.85%', '18.09%', '19.79%', '8.46%', '6.72%', '1.97%', '11.44%', '0.15%', '3.27%', '11.19%', '6.97%', '11.63%', '3.35%', '4.80%', '5.49%', '0.79%', '6.62%', '7.93%', '4.01%', '4.87%', '9.16%', '9.41%', '8.23%', '0.65%', '12.93%', '6.82%', '7.07%', '9.30%', '3.42%', '-0.20%', '2.83%', '3.15%', '5.16%', '8.18%', '2.69%', '3.31%', '6.56%', '17.35%', '19.11%', '9.90%', '11.80%', '8.29%', '7.12%', '6.13%', '4.66%', '3.62%', '4.70%', '0.65%', '10.60%', '9.93%', '0.30%', '3.14%', '3.69%', '9.46%', '1.67%', '-1.44%', '2.21%', '21.98%', '2.03%', '7.56%', '4.37%', '4.93%', '3.86%', '15.80%', '13.19%', '11.78%', '3.82%', '7.37%', '9.65%', '2.11%', '2.84%', '15.25%', '3.30%', '3.60%', '6.56%', '2.61%', '2.50%', '6.38%', '6.31%', '16.30%', '3.29%', '3.66%', '0.52%', '2.23%', '1.02%', '7.12%']
# ['46.64%', '6.06%', '23.69%', '24.50%', '69.25%', '40.14%', '20.79%', '23.61%', '15.79%', '15.79%', '24.54%', '33.34%', '27.74%', '27.94%', '9.53%', 'N/A', '125.61%', '27.62%', '32.25%', '-0.87%', '35.55%', '8.51%', '15.27%', '37.85%', '34.73%', '30.15%', '6.80%', '14.19%', '22.81%', '7.56%', '22.90%', '51.81%', '9.86%', '12.65%', '31.37%', 'N/A', '225.62%', '3.65%', '32.82%', '23.51%', '29.70%', '68.05%', '11.02%', '-6.02%', '8.76%', '7.66%', '-1.65%', '32.14%', '4.67%', '8.60%', '62.58%', 'N/A', '62.60%', '157.61%', '163.64%', '70.30%', '32.62%', '99.49%', '34.56%', '40.97%', 'N/A', '7.07%', '193.03%', '48.81%', '3.11%', '6.62%', '1.13%', '23.40%', '0.13%', 'N/A', '38.95%', '108.32%', '13.44%', '14.31%', '-1.40%', '28.92%', '12.99%', '41.24%', '-9.13%', '59.87%', '12.73%', '28.78%', '54.67%', '18.45%', '3.99%', '33.06%', '21.58%', '2.11%', '18.13%', '5.20%', '7.84%', '16.58%', '12.96%', '756.79%', '5.25%', '11.59%', '5.86%', '4.21%', '11.17%', '14.13%']
# ['0.70%', '0.52%', '0.12%', '0.19%', '0.07%', '1.42%', '15.12%', '0.66%', '0.14%', '5.75%', '0.08%', '0.20%', '0.11%', '4.15%', '0.88%', '0.12%', '11.30%', '0.71%', '0.03%', '0.20%', '0.29%', '3.80%', '0.13%', '0.08%', '1.62%', '0.05%', '0.08%', '0.69%', '0.04%', '0.10%', '50.91%', '0.14%', '0.73%', '0.21%', '0.04%', '0.12%', '0.11%', '0.08%', '0.19%', '0.23%', '1.17%', '0.22%', '2.53%', '0.05%', '0.07%', '0.18%', '0.11%', '0.14%', '0.12%', '11.47%', '0.12%', '0.22%', '0.24%', '0.15%', '0.17%', '36.36%', '0.16%', '0.01%', '0.34%', '0.11%', '0.23%', '0.25%', '0.07%', '0.18%', '0.13%', '27.05%', '0.11%', '0.60%', '0.33%', '0.13%', '0.77%', '0.12%', '3.32%', '0.96%', '0.41%', '0.19%', 'N/A', '3.49%', '0.10%', '0.25%', '0.19%', '0.26%', '0.35%', '0.10%', '0.17%', '0.14%', '0.23%', '0.28%', '0.17%', '0.50%', '0.43%', '0.25%', '7.45%', '0.24%', '44.09%', '1.45%', '0.60%', '0.10%', '24.24%', '1.37%']
# ['70.00%', '88.99%', '76.04%', '90.66%', '62.12%', '74.09%', '57.69%', '79.41%', '82.29%', '70.62%', '70.25%', '98.06%', '65.03%', '69.23%', '76.08%', '72.20%', '78.61%', '89.92%', '68.43%', '66.29%', '89.10%', '85.16%', '86.62%', '78.55%', '83.49%', '69.04%', '57.41%', '85.05%', '72.56%', '73.24%', '30.95%', '73.53%', '77.18%', '93.01%', '73.98%', '68.79%', '76.76%', '56.77%', '74.68%', '71.54%', '85.83%', '78.93%', '84.85%', '68.96%', '85.82%', '81.04%', '79.09%', '83.46%', '84.26%', '82.13%', '79.91%', '75.22%', '88.83%', '79.61%', '78.30%', '52.78%', '78.18%', '71.23%', '94.05%', '58.56%', '70.28%', '81.98%', '80.38%', '69.95%', '77.48%', '65.63%', '46.73%', '78.19%', '92.30%', '66.60%', '98.93%', '86.82%', '84.87%', '91.32%', '80.77%', '70.02%', 'N/A', '89.81%', '64.19%', '95.03%', '79.64%', '84.60%', '96.71%', '87.09%', '89.53%', '97.83%', '80.91%', '72.79%', '92.52%', '96.65%', '93.22%', '86.04%', '76.43%', '80.93%', '48.69%', '92.71%', '76.20%', '65.29%', '62.93%', '92.22%']



# Ta(end) Fw(600) Lh(14px) 76
# span Fl(end) 29
# span W(39%) Fl(start) C($negativeColor) 35
# span W(39%) Fl(start) 50
# span W(39%) Fl(start) 125









from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import pymysql
import datetime
from selenium.webdriver.chrome.options import Options
import requests
import datetime
from dateutil.parser import parse 


temp = 'KO,PLD,CSX,MMC,AAPL,MSFT,AMZN,FB,GOOGL,GOOG,JNJ,V,PG,NVDA,JPM,HD,MA,UNH,VZ,DIS,ADBE,CRM,PYPL,MRK,NFLX,INTC,T,CMCSA,PFE,BAC,WMT,PEP,ABT,TMO,CSCO,MCD,ABBV,XOM,ACN,COST,NKE,AMGN,AVGO,CVX,MDT,NEE,BMY,UNP,LIN,DHR,QCOM,PM,TXN,LLY,LOW,ORCL,HON,UPS,AMT,IBM,SBUX,C,LMT,MMM,WFC,CHTR,RTX,AMD,FIS,BA,NOW,SPGI,BLK,ISRG,GILD,CAT,MDLZ,INTU,MO,ZTS,CVS,TGT,BKNG,AXP,BDX,VRTX,DE,D,ANTM,EQIX,CCI,APD,SYK,CL,TMUS,CI,GS,DUK,MS,ATVI'
temp_arr = temp.split(',')
stk = []
for i in range(100):
    stk.append(temp_arr[i])

# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")


# driver = webdriver.Chrome("C:/Users/User/Downloads/安裝檔案/chromedriver.exe", chrome_options = chrome_options)
driver = webdriver.Chrome("C:/Users/User/Downloads/安裝檔案/chromedriver.exe")



db = pymysql.connect("localhost", "root", "esfortest", "etf")
cursor = db.cursor()


url1 = 'https://www.nasdaq.com/market-activity/stocks/'
url2 = '/dividend-history'


for i in range(len(stk)):    
    url = url1 + stk[i] + url2
    driver.get(url)
    time.sleep(2)
    soup = bs(driver.page_source,"html.parser")
    raw_data = [data.text for data in soup.find_all('span',{'class':['dividend-history__summary-item__value']})]
    print(raw_data)
    try:
        temp = str(raw_data[1]).split('%')
        temp_sql = float(temp[0])*0.01
        sql= "UPDATE detail SET `配息率` ='%s' WHERE `name` ='%s'" % (str(temp_sql),str(stk[i]))
        print(stk[i])
        print(temp_sql)
        cursor.execute(sql)
        db.commit()
        print("Data are successfully inserted")
    except:
        print("算了")

db.close()






# temp = 'AAPL,MSFT,AMZN,FB,GOOGL,GOOG,BRK.B,JNJ,V,PG,NVDA,JPM,HD,MA,UNH,VZ,DIS,ADBE,CRM,PYPL,MRK,NFLX,INTC,T,CMCSA,PFE,BAC,KO,WMT,PEP,ABT,TMO,CSCO,MCD,ABBV,XOM,ACN,COST,NKE,AMGN,AVGO,CVX,MDT,NEE,BMY,UNP,LIN,DHR,QCOM,PM,TXN,LLY,LOW,ORCL,HON,UPS,AMT,IBM,SBUX,C,LMT,MMM,WFC,CHTR,RTX,AMD,FIS,BA,NOW,SPGI,BLK,ISRG,GILD,CAT,MDLZ,INTU,MO,ZTS,CVS,PLD,TGT,BKNG,AXP,BDX,VRTX,DE,D,ANTM,EQIX,CCI,APD,TJX,SYK,CL,TMUS,CI,GS,DUK,MS,ATVI'
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



temp = 'NVDA,NFLX,XLK,IWF,EQIX,CAT,COST,SPY,VT,SBUX,XLV,VZ,VEA,BIV,EFA,KO,PFE,VMBS,XLF,BDX'
temp_arr = temp.split(',')
test = []
for i in range(len(temp_arr)):
    test.append(temp_arr[i])

for i in range(len(test)):
    if test[i] in stk:
        print('STK',test[i])
    else :
        print('ETF',test[i])



