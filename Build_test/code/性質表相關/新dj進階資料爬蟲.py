

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

#ETF類表
# etf = ['VTI','VOO','VXUS','SPY','BND','IVV','BNDX','VEA','VO',
#        'VUG','VB','VWO','VTV','QQQ','BSV','BIV','VTIP','VOE','IEF',
#        'SHY','TLT','IVE','VT','GOVT']


temp = 'SPY,IVV,VTI,VOO,QQQ,AGG,GLD,VEA,IEFA,BND,VWO,VUG,IWF,LQD,IEMG,VTV,EFA,VIG,IJH,IJR,IWM,VCIT,IWD,VGT,XLK,VO,USMV,IAU,VCSH,BNDX,IVW,HYG,VNQ,VB,ITOT,VYM,BSV,VXUS,VEU,EEM,XLV,TIP,IWB,DIA,SCHX,MBB,IXUS,SHY,SHV,IWR,IGSB,IEF,SCHF,QUAL,VV,GDX,XLF,MUB,TLT,PFF,EMB,IVE,SCHB,XLY,SDY,SLV,GOVT,MDY,BIV,XLP,VT,BIL,JPST,MINT,VBR,RSP,JNK,DVY,IWP,SCHD,VGK,ACWI,SCHP,SCHG,XLI,XLU,DGRO,VMBS,VHT,MTUM,IGIB,IEI,VBK,EFAV,XLC,IWS,GSLC,EWJ,FDN,SCHA'
temp_arr = temp.split(',')
etf = []
for i in range(100):
    etf.append(temp_arr[i])


#輸入Mysql前的資料，並且先都設定為0
area = []
create =[]



headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")



url1 = 'https://www.moneydj.com/ETF/X/Basic/Basic0002.xdjhtm?etfid='

#開啟瀏覽器並進入yahoo網頁
driver = webdriver.Chrome("C:/Users/User/Downloads/安裝檔案/chromedriver.exe", chrome_options = chrome_options)
#根據ETF列表重複執行抓取資料的動作
for i in range(len(etf)):
    raw_data = []

    url = url1 + etf[i]
    driver.get(url)
    time.sleep(3)
    soup = bs(driver.page_source,"html.parser")
    # click
    start_search_btn = driver.find_element_by_id("sshow")
    start_search_btn.click()
    time.sleep(3)
    soup = bs(driver.page_source,"html.parser")
    content = driver.find_elements_by_xpath("//td[@style='text-align: right;']")
    a = 0

    for u in content:
        # print(type(u.text))
        # print(u.text)
        raw_data.append(u.text)

    # print(raw_data)
    
    time.sleep(3)




# UPDATE `detail` SET `總費用率`= 0 WHERE `總費用率` Is Null


# 全名
# ['SPDR標普500指數ETF', 'iShares核心標普500指數ETF', 'Vanguard整體股市ETF', 'Vanguard標普500指數ETF', 'Invesco納斯達克100指數ETF', 'iShares美國核心綜合債券ETF', 'SPDR黃金ETF', 'Vanguard FTSE成熟市場ETF', 'iShares MSCI核心歐澳遠東ETF', 'Vanguard總體債券市場ETF', 'Vanguard FTSE新興市場ETF', 'Vanguard成長股指數', 'iShares羅素1000成長股ETF', 'iShares iBoxx投資等級公司債券ETF', 'iShares MSCI核心新興市場ETF', 'Vanguard價值股ETF', 'iShares MSCI歐澳遠東ETF', 'Vanguard股利增值ETF', 'iShares核心標普中型股指數ETF', 'iShares核心標普小型股指數ETF', 'iShares羅素2000 ETF', 'Vanguard中期公司債券ETF', 'iShares羅素1000價值股ETF', 'Vanguard資訊科技類股ETF', 'SPDR科技類股ETF', 'Vanguard中型股ETF', 'iShares MSCI美國最小波動率因子ETF', 'iShares黃金信託ETF', 'Vanguard短期公司債券ETF', 'Vanguard總體國際債券ETF', 'iShares標普500成長股ETF', 'iShares iBoxx高收益公司債券ETF', 'Vanguard房地產ETF', 'Vanguard小型股ETF', 'iShares核心標普美股總體市場指數ETF', 'Vanguard高股利收益ETF', 'Vanguard短期債券ETF', 'Vanguard總體國際股票ETF', 'Vanguard FTSE美國以外全世界ETF', 'iShares MSCI新興市場ETF', 'SPDR健康照護類股ETF', 'iShares抗通膨債券ETF', 'iShares羅素1000 ETF', 'SPDR道瓊工業平均指數ETF', 'Schwab美國大型股ETF', 'iShares抵押貸款證券化債券ETF', 'iShares MSCI核心總體國際股市ETF', 'iShares 1-3年期美國公債ETF', 'iShares短期美國公債ETF', 'iShares羅素中型股ETF', 'iShares短期公司債券ETF', 'iShares 7-10年期美國公債ETF', 'Schwab國際股票ETF', 'iShares MSCI美國優質因子ETF', 'Vanguard大型股ETF', 'VanEck Vectors黃金礦業ETF', 'SPDR金融類股ETF', 'iShares美國市政債券ETF', 'iShares 20年期以上美國公債ETF', 'iShares優先股與收益證券ETF', 'iShares J.P. Morgan新興市場美元債券ETF', 'iShares標普500價值股ETF', 'Schwab美國整體市場ETF', 'SPDR非必需消費類股ETF', 'SPDR標普高股利ETF', 'iShares白銀信託ETF', 'iShares美國公債ETF', 'SPDR標普400中型股ETF', 'Vanguard美國中期債券ETF', 'SPDR必需性消費類股ETF', 'Vanguard全世界股票ETF', 'SPDR彭博巴克萊1-3月美國國庫券ETF', 'JPMorgan超短收益主動型ETF', 'PIMCO增強短期到期主動型ETF', 'Vanguard小型價值股ETF', 'Invesco標普500平均加權指數ETF', 'SPDR彭博巴克萊高收益債ETF', 'iShares精選高股利指數ETF', 'iShares羅素中型成長股ETF', 'Schwab美國高股利股票型ETF', 'Vanguard FTSE歐洲ETF', 'iShares MSCI全世界ETF', 'Schwab美國抗通膨債券ETF', 'Schwab美國大型成長股ETF', 'SPDR工業類股ETF', 'SPDR公用事業類股ETF', 'iShares核心股息成長ETF', 'Vanguard抵押貸款證券ETF', 'Vanguard健康照護類股ETF', 'iShares MSCI美國動能因子ETF', 'iShares中期公司債券ETF', 'iShares 3-7年期美國公債ETF', 'Vanguard小型成長股ETF', 'iShares MSCI歐澳遠東最小波動率因子ETF', 'SPDR通訊服務類股ETF', 'iShares羅素中型價值股ETF', 'Goldman Sachs積極貝塔美國大型股ETF', 'iShares MSCI日本ETF', 'First Trust道瓊網路指數ETF', 'Schwab美國小型股ETF']
# 投資區域
# ['美國', '美國', '美國', '美國', '美國', '美國', '全球', '全球', '全球', '美國', '新興市場', '美國', '美國', '美國', '新興市場', '美國', '全球', '美國', '美國', '美國', '美國', '美國', '美國', '美國', '美國', '美國', '美國', '美國', '美國', '全球', '美國', '美國', '美國', '美國', '美國', '美國', '美國', '全球', '全球', '新興市場', '美國', '美國', '美國', '美國', '美國', '美國', '全球', '美國', '美國', '美國', '美國', '美國', '全球', '美國', '美國', '全球', '美國', '美國', '美國', '美國', '新興市場', '美國', '美國', '美國', '美國', '全球', '美國', '美國', '美國', '美國', '全球', '美國', '全球', '美國', '美國', '美國', '美國', '美國', '美國', '美國', '歐洲', '全球', '美國', '美國', '美國', '美國', '美國', '美國', '美國', '美國', '美國', '美國', '美國', '全球', '美國', '美國', '美國', '日本', '美國', '美國']
# 投資標的
# ['股票型', '股票型', '股票型', '股票型', '股票型', '中期債券', '貴重金屬', '股票型', '股票型', '債券型', '股票型', '股票型', '股票型', '公司債券', '股票型', '股票型', '股票型', '股票型', '股票型', '股票型', '股票型', '公司債券', '股票型', '資訊科技股', '資訊科技股', '股票型', '股票型', '貴重金屬', '公司債券', '債券型', '股票型', '高收益債', '房地產', '股票型', '股票型', '股票型', '短期債券', '股票型', '股票型', '股票型', '健康護理股', '抗通膨債券', '股票型', '股票型', '股票型', '債券型', '股票型', '短期債券', '短期債券', '股票型', '短期債券', '中期債券', '股票型', '股票型', '股票型', '貴重金屬', '金融股', '市政債券', '長期債券', '股票型', '債券型', '股票型', '股票型', '非必需消費股', '股票型', '貴重金屬', '債券型', '股票型', '中期債券', '必需性消費股', '股票型', '短期債券', '債券型', '短期債券', '股票型', '股票型', '高收益債', '股票型', '股票型', '股票型', '股票型', '股票型', '抗通膨債券', '股票型', '工業類股', '公共事業股', '股票型', '固定收益', '健康護理股', '股票型', '中期債券', '債券型', '股票型', '股票型', '電信股', '股票型', '股票型', '股票型', '電信股', '股票型']
# 投資風格
# ['大型股混合型', '大型股混合型', '大型股混合型', '', '', '', '', '大型股混合型', '大型股混合型', '', '', '大型股成長型', '大型股成長型', '', '大型股混合型', '大型股價值型', '大型股混合型', '', '中型股混合型', '小型股混合型', '小型股混合型', '', '大型股價值型', '', '大型股成長型', '中型股混合型', '', '', '', '', '大型股成長型', '', '中型股混合型', '小型股混合型', '大型股混合型', '大型股價值型', '', '', '大型股混合型', '大型股混合型', '大型股成長型', '', '大型股混合型', '大型股價值型', '大型股混合型', '', '', '', '', '中型股混合型', '', '', '', '', '大型股混合型', '', '大型股價值型', '', '', '大型股混合型', '', '大型股價值型', '大型股混合型', '大型股成長型', '大型股價值型', '', '', '中型股混合型', '', '大型股價值型', '', '', '', '', '小型股價值型', '大型股混合型', '', '中型股價值型', '中型股成長型', '', '', '大型股混合型', '', '大型股成長型', '大型股混合型', '大型股價值型', '大型股混合型', '', '', '', '', '', '小型股成長型', '大型股混合型', '大型股成長型', '中型股價值型', '大型股混合型', '', '', '小型股成長型']
# 殖利率
# ['1.68', '1.86', '1.68', '1.72', '0.59', '2.16', 'N/A', '2.47', '2.55', '2.37', '2.93', '0.76', '0.78', '2.87', '3.04', '2.88', '2.49', '1.71', '1.69', '1.63', '1.31', '2.84', '2.84', '0.99', '1.03', '1.64', '1.98', 'N/A', '2.56', '3.24', '1.20', '4.58', '3.72', '1.36', '1.72', '3.54', '2.01', '2.39', '2.46', '2.57', '2.14', '0.81', '1.54', '2.10', '1.75', '2.32', '2.53', '1.40', '1.23', '1.55', '2.45', '1.28', '2.27', '1.50', '1.64', '0.44', '2.47', '2.23', '1.62', '5.37', '3.76', '2.50', '1.77', '1.03', '2.97', 'N/A', '1.43', '1.46', '2.40', '2.49', '1.98', '0.85', '1.93', '1.72', '2.07', '1.92', '5.46', '4.19', '0.51', '3.23', '2.28', '1.92', '0.85', '0.64', '1.93', '3.23', '2.41', '2.20', '1.25', '1.19', '2.73', '1.33', '0.48', '3.93', '0.75', '2.36', '1.56', '1.95', 'N/A', '1.41']
# 配息頻率
# ['季配', '季配', '季配', '季配', '季配', '月配', '', '季配', '半年配', '月配', '季配', '季配', '季配', '月配', '半年配', '季配', '半年配', '季配', '季配', '季配', '季配', '月配', '季配', '季配', '季配', '季配', '季配', '', '月配', '月配', '季配', '月配', '季配', '季配', '季配', '季配', '月配', '季配', '季配', '半年配', '季配', '月配', '季配', '月配', '季配', '月配', '半年配', '月配', '月配', '季配', '月配', '月配', '年配', '季配', '季配', '年配', '季配', '月配', '月配', '月配', '月配', '季配', '季配', '季配', '季配', '', '月配', '季配', '月配', '季配', '季配', '月配', '月配', '月配', '季配', '季配', '月配', '季配', '季配', '季配', '季配', '半年配', '月配', '季配', '季配', '季配', '季配', '月配', '季配', '季配', '月配', '月配', '季配', '半年配', '季配', '季配', '季配', '半年配', '半年配', '季配']
# 總費用率
# ['0.0945 (含 0.0451 非管理費用)', '0.03', '0.03 (含 0.01 非管理費用)', '0.03 (含 0.01 非管理費用)', '0.2', '0.04', '0.4', '0.05 (含 0.01 非管理費用)', '0.07', '0.035 (含 0.010 非管理費用)', '0.1 (含 0.02 非管理費用)', '0.04 (含 0.01 非管理費用)', '0.19', '0.15', '0.13', '0.04 (含 0.01 非管理費用)', '0.32', '0.06 (含 0.01 非管理費用)', '0.05', '0.06', '0.19', '0.05 (含 0.01 非管理費用)', '0.19', '0.1 (含 0.01 非管理費用)', '0.13 (含 0.10 非管理費用)', '0.04 (含 0.01 非管理費用)', '0.15', '0.25', '0.05 (含 0.01 非管理費用)', '0.08 (含 0.02 非管理費用)', '0.18', '0.49', '0.12 (含 0.01 非管理費用)', '0.05 (含 0.01 非管理費用)', '0.03', '0.06 (含 0.01 非管理費用)', '0.05 (含 0.01 非管理費用)', '0.08 (含 0.01 非管理費用)', '0.08 (含 0.02 非管理費用)', '0.68', '0.13 (含 0.10 非管理費用)', '0.19', '0.15', '0.16 (含 0.10 非管理費用)', '0.03', '0.07 (含 0.01 非管理費用)', '0.09', '0.15', '0.15', '0.19', '0.06', '0.15', '0.06', '0.15', '0.04 (含 0.01 非管理費用)', '0.52 (含 0.02 非管理費用)', '0.13 (含 0.10 非管理費用)', '0.07', '0.15', '0.46', '0.39', '0.18', '0.03', '0.13 (含 0.10 非管理費用)', '0.35', '0.5', '0.15', '0.23 (含 0.13 非管理費用)', '0.05 (含 0.01 非管理費用)', '0.13 (含 0.10 非管理費用)', '0.08 (含 0.01 非管理費用)', '0.1359 (含 0.0014 非管理費用)', '0.28 (含 0.13 非管理費用)', '0.36 (含 0.01 非管理費用)', '0.07 (含 0.01 非管理費用)', '0.2', '0.4', '0.39', '0.24', '0.06', '0.08 (含 0.01 非管理費用)', '0.33 (含 0.01 非管理費用)', '0.05', '0.04', '0.13 (含 0.10 非管理費用)', '0.13 (含 0.10 非管理費用)', '0.08', '0.05 (含 0.02 非管理費用)', '0.1 (含 0.01 非管理費用)', '0.15', '0.06', '0.15', '0.07 (含 0.01 非管理費用)', '0.32', '0.13 (含 0.10 非管理費用)', '0.24', '0.09', '0.49', '0.52 (含 0.12 非管理費用)', '0.04']
# 追蹤指數
# ['S&P 500 Index', 'S&P 500 Index', 'CRSP US Total Market Index', 'S&P 500 Index', 'Nasdaq-100 Index', 'Bloomberg Barclays US Aggregate Bond Index', 'Gold Price', 'FTSE Developed All Cap ex US Index', 'MSCI EAFE IMI Index', 'Bloomberg Barclays U.S. Aggregate Float Adjusted Index.', 'FTSE Emerging Markets All Cap China A Inclusion Index', 'CRSP US Large Cap Growth Index', 'Russell 1000 Growth Index', 'Markit iBoxx USD Liquid Investment Grade Index', 'MSCI Emerging Markets Investable Market Index', 'CRSP US Large Cap Value Index', 'MSCI EAFE Index', 'NASDAQ US Dividend Achievers Select Index', 'S&P MidCap 400 Index', 'S&P SmallCap 600 Index', 'Russell 2000 Index', 'Barclays U.S. 5-10 Year Corporate Bond Index', 'Russell 1000 Value index', 'MSCI US Investable Market Information Technology 25/50 Index', 'Technology Select Sector Index', 'CRSP US Mid Cap Index', 'MSCI USA Minimum Volatility (USD) Index', 'gold bullion', 'Barclays U.S. 1-5 Year Corporate Bond Index', 'Barclays Global Aggregate ex-USD Float Adjusted RIC Capped Index', 'S&P 500 Growth Index', 'Markit iBoxx USD Liquid High Yield Index', 'MSCI US Investable Market Real Estate 25/50 Transition Index', 'CRSP US Small Cap Index', 'S&P Total Market Index(TM)', 'FTSE High Dividend Yield Index', 'Bloomberg Barclays U.S. 1-5 Year Government/Credit Float Adjusted Index', 'FTSE Global All Cap ex US Index', 'FTSE All-World ex US Index', 'MSCI Emerging Markets Index', 'Health Care Select Sector Index', 'Bloomberg Barclays U.S. Treasury Inflation Protected Securities (TIPS) Index (Series-L)', 'Russell 1000 Index', 'Dow Jones Industrial Average', 'Dow Jones U.S. Large-Cap Total Stock Market Index', 'Barclays U.S. MBS Index', 'MSCI ACWI ex USA Investable Market Index', 'ICE U.S. Treasury 1-3 Year Bond Index', 'ICE Short US Treasury Securities Index', 'Russell Midcap index', 'ICE BofAML 1-5 Year US Corporate Index', 'ICE U.S. Treasury 7-10 Year Bond Index', 'FTSE Developed ex-US Index', 'MSCI USA Sector Neutral Quality Index', 'CRSP US Large Cap Index', 'NYSE Arca Gold Miners Index (Total Return)', 'Financial Select Sector Index', 'S&P National AMT-Free Municipal Bond Index', 'ICE U.S. Treasury 20+ Year Bond Index', 'ICE Exchange-Listed Preferred & Hybrid Securities Transition Index', 'J.P. Morgan EMBI Global Core Index', 'S&P 500 Value Index', 'Dow Jones U.S. Broad Stock Market Index', 'Consumer Discretionary Select Sector Index', 'S&P High Yield Dividend Aristocrats index', 'London Silver Fix Price(LBMA silver price)', 'ICE U.S. Treasury Core Bond Index', 'S&P MidCap 400 Index', 'Bloomberg Barclays U.S. 5-10 Yr Government/Credit Float Adjusted Index', 'Consumer Staples Select Sector Index', 'FTSE Global All Cap Index', 'Bloomberg Barclays 1-3 Month U.S. Treasury Bill Index', '', '', 'CRSP US Small Cap Value Index', 'S&P 500 Equal Weight Index', 'Bloomberg Barclays High Yield Very Liquid Index', 'Dow Jones U.S. Select Dividend Index', 'Russell Midcap Growth index', 'Dow Jones U.S. Dividend 100 Index', 'FTSE Developed Europe All Cap Index', 'MSCI ACWI Index', 'Bloomberg Barclays US Treasury Inflation-Linked Bond Index', 'Dow Jones U.S. Large-Cap Growth Total Stock Market Index', 'Industrial Select Sector Index', 'Utilities Select Sector Index', 'Morningstar US Dividend Growth Index', 'Barclays U.S. Mortgage Backed Securities Float Adjusted Index', 'MSCI US Investable Market Health Care 25/50 Index', 'MSCI USA Momentum Index', 'ICE BofAML 5-10 Year US Corporate Index', 'ICE U.S. Treasury 3-7 Year Bond Index', 'CRSP US Small Cap Growth Index', 'MSCI EAFE Minimum Volatility (USD) Index', 'Communication Services Select Sector Index', 'Russell Midcap Value index', 'Goldman Sachs ActiveBeta U.S. Large Cap Equity Index', 'MSCI Japan Index', 'Dow Jones Internet Composite Index', 'Dow Jones U.S. Small-Cap Total Stock Market Index']
# 基準指數
# ['S&P500 (SPY.US)', 'S&P500 (SPY.US)', '道瓊指數', 'S&P500 (SPY.US)', '那斯達克 100', 'Bloomberg Barclays US Aggregate Bond Index', 'gold bullion', '道瓊全球指數', '道瓊全球指數', 'Bloomberg Barclays US Aggregate Bond Index', 'NASDAQ Emerging Markets Index', '道瓊指數', 'Russell 1000 Growth Index', 'iBoxx $ Liquid Investment Grade Index', 'NASDAQ Emerging Markets Index', '道瓊指數', '道瓊全球指數', 'Dividend Achievers Select Index', '道瓊指數', '道瓊指數', 'RUSSELL 2000 INDEX', 'Bloomberg Barclays US Aggregate Bond Index', 'Russell 1000 Value Index', 'Dow Jones U.S. Technology Index', 'Dow Jones U.S. Technology Index', '道瓊指數', '道瓊指數', 'gold bullion', 'ICE BofAML 1-5 Year US Corporate Index', 'Bloomberg Barclays US Aggregate Bond Index', '道瓊指數', 'iBoxx $ Liquid High Yield Index', 'FTSE NAREIT Real Estate 50 Index', '道瓊指數', '道瓊指數', 'Fidelity High Dividend Index PR', 'Bloomberg Barclays U.S. Universal 1-5 Year Index', '道瓊全球指數', 'International Dividend Achievers Index', 'NASDAQ Emerging Markets Index', '道瓊指數', 'Bloomberg Barclays U.S. Treasury Inflation Protect', 'Russell 1000 Index', 'Dow Jones Industrial Average', 'Dow Jones U.S. Large Cap Total Stock Market Index', 'Barclays U.S. MBS Index', '道瓊全球指數', 'ICE U.S. Treasury 1-3 Year Bond Index', 'ICE U.S. Treasury Short Bond Index', 'Russell Midcap index', 'ICE BofAML 1-5 Year US Corporate Index', 'ICE U.S. Treasury 7-10 Year Bond Index', '道瓊全球指數', '道瓊指數', '道瓊指數', 'NYSE Arca Gold Miners Index (NTR)', '道瓊金融指數', 'OMRX Municipal Bond Index', 'ICE U.S. Treasury 20+ Year Bond Index', 'ICE Exchange-Listed Preferred & Hybrid Securities', 'J.P. Morgan EMBI Global Core Index', '道瓊指數', '道瓊指數', 'Dow Jones U.S. Consumer Goods Index', '道瓊指數', 'LBMA Silver Price', 'ICE U.S. Treasury Core Bond Index', '道瓊指數', 'Bloomberg Barclays US Universal 5-10 Years Index', 'CONSUMER STAPLES SELECT SECTOR INDEX', '道瓊全球指數', 'ICE U.S. Treasury Short Bond Index', 'Bloomberg Barclays U.S. Government/Credit Bond Ind', 'OMRX Treasury Bill 90 day Index', '道瓊指數', '道瓊指數', 'iBoxx $ Liquid High Yield Index', 'Dow Jones U.S. Select Dividend Index', 'Russell Midcap Growth index', '道瓊指數', '道瓊歐洲指數', '道瓊全球指數', 'Bloomberg Barclays U.S. Government/Credit Bond Ind', 'Dow Jones U.S. Large-Cap Growth Total Stock Market', 'Industrial Select Sector Index', 'Dow Jones U.S. Utilities Index', '道瓊指數', 'Barclays U.S. MBS Index', '道瓊指數', '道瓊指數', 'ICE BofAML 5-10 Year US Corporate Index', 'ICE U.S. Treasury 3-7 Year Bond Index', 'CRSP US Small Cap Growth Index', '道瓊全球指數', 'Dow Jones U.S. Select Telecommunications Total Ret', 'Russell Midcap Value index', '道瓊指數', '日經指數', 'Dow Jones Internet Composite Index', 'Dow Jones U.S. Small Cap Total Stock Market Index']