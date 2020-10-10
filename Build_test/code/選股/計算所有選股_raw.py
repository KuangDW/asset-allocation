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

www=[[ 0.3 ,0.3 ,0.3 ,0.1  ],
     [ 0.3 ,0.3 ,0.3 ,0.05,0.05 ],
     [ 0.3 ,0.3 ,0.25,0.05,0.05,0.05 ],
     [ 0.3 ,0.3 ,0.2 ,0.05,0.05,0.05,0.05 ],
     [ 0.3 ,0.3 ,0.15,0.05,0.05,0.05,0.05,0.05 ],
     [ 0.3 ,0.3 ,0.1 ,0.05,0.05,0.05,0.05,0.05,0.05 ],
     [ 0.3 ,0.3 ,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05 ],
     [ 0.3 ,0.25,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05 ],
     [ 0.3 ,0.2 ,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05 ],
     [ 0.3 ,0.15,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05 ],
     [ 0.3 ,0.1 ,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05 ],
     [ 0.3 ,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05 ],
     [ 0.25,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05 ],
     [ 0.2 ,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05 ],
     [ 0.15,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05 ],
     [ 0.1 ,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05 ],
     [ 0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05 ] ]

# year = sys.argv[1]
# goal_money = sys.argv[2]
# in_per_year = sys.argv[3]
# mode = sys.argv[4]#1:投資 2:圓夢 3:退休
# year = int(year)
# goal_money = round(float(goal_money))
# in_per_year = int(in_per_year)
# mode = int(mode)

# 退休
# mode = 3
# in_per_year = 180000
# goal_money = 5*15*12*10000*(1.0172**40)
# year = 40

# 圓夢
# mode = 2
# in_per_year = 110000
# goal_money = 150*10000
# year = 10

#投資
# mode = 1
# in_per_year = 110000 #input_money
# goal_money = 190000
# year = 10


use_year_input=0

mode = 3
# expect_reward = 0.05
# expect_reward_y = expect_reward

def becomezero(x):
    for o in range(len(x)):
        x[o] = 0
def becomehundred(y):
    for h in range(len(y)):
        y[h] = 100

today = datetime.date.today()



#ETF類表
v1 = ['VTI','VOO','VXUS','SPY','BND','IVV','BNDX','VEA','VO',
       'VUG','VB','VWO','VTV','QQQ','BSV','BIV','VTIP','VOE','IEF',
       'SHY','TLT','IVE','VT','GOVT']
record_v1 = np.zeros(len(v1))

#相關性的表([1][1]開始喔)
db = pymysql.connect("localhost", "root", "esfortest", "etf")
cursor = db.cursor()
sql = "select * from close"
cursor.execute(sql)
result_select = cursor.fetchall()
db.commit()
df = pd.DataFrame(list(result_select))

df = df.drop([0],axis=1)
# print(df)
corr_pd1 = df.corr()
# print(corr_pd1)

reward = []
reward_yin = []
reward_min = []
reward_nodiv = []
div = []
std = []
std_find_too_high = []
sharp = []
code = []
names = []
wwws=[]
rw=[]
rsk=[]
exp_rw=[]
y_in=[]
nd_rw=[]
f_div=[]
# choose_code = []
for i in range(len(v1)):
    reward.append(0)
    reward_yin.append(0)
    reward_min.append(0)
    std.append(0)
    std_find_too_high.append(0)
    sharp.append(0)
    code.append(0)
    reward_nodiv.append(0)
    div.append(0)

a=0
for a in range(len(v1)):
    sql = "select `年化報酬率` from `性質表` where name = '"+v1[a] +"'"
    cursor.execute(sql)
    result_select = cursor.fetchall()
    reward_min[a] = result_select[0][0]
    if mode!=1:
        reward[a] = result_select[0][0]
    

a=0
for a in range(len(v1)):
    sql = "select `年化報酬率_年入` from `性質表` where name = '"+v1[a] +"'"
    cursor.execute(sql)
    result_select = cursor.fetchall()
    reward_yin[a] = result_select[0][0]
    if mode==1:
        reward[a] = result_select[0][0]

a=0
for a in range(len(v1)):
    sql = "select `年化報酬率_無配息` from `性質表` where name = '"+v1[a] +"'"
    cursor.execute(sql)
    result_select = cursor.fetchall()
    reward_nodiv[a] = result_select[0][0]

a=0
for a in range(len(v1)):
    sql = "select `殖利率` from `性質表` where name = '"+v1[a] +"'"
    cursor.execute(sql)
    result_select = cursor.fetchall()
    div[a] = result_select[0][0]
    

a=0
for a in range(len(v1)):
    sql = "select `年化標準差` from `性質表` where name = '"+v1[a] +"'"
    cursor.execute(sql)
    result_select = cursor.fetchall()
    std[a] = result_select[0][0]
    std_find_too_high[a] = std[a]

a=0
for a in range(len(v1)):
    sql = "select `夏普值` from `性質表` where name = '"+v1[a] +"'"
    cursor.execute(sql)
    result_select = cursor.fetchall()
    sharp[a] = result_select[0][0]

db.close()


# print(reward_yin)



v=len(v1)
expect_reward = 0.07
while(expect_reward>=0.03):
    print(expect_reward)
    expect_reward_y = expect_reward
    v=24
    choose_code = []   
    for i in range(int(comb(v,4))):
        choose_code.append(0)
    db = pymysql.connect("localhost", "root", "esfortest", "etf")
    cursor = db.cursor()
    code = []
    for produce in range(0,len(v1)):
        # if record_v1[produce] ==0:
            # code[a] = produce
        code.append(produce)
            # a+=1
    
    # v-=1
    # w:比例 name:名稱 min_risk:風險
    w = []
    w_code = []
    ub = []
    final_w=[]
    calc_reward = []
    calc_sharp = []
    calc_std = []
    
    upstd = []
    name = []
    final_name =[]
    min_risk = 100
    min_risk1 = 100
    max_reward = 0
    calc = 0
    add = 0.03
    
    for i in range(20):
        w.append(0)
        w_code.append(0)
        ub.append(0)
        upstd.append(0)
        calc_reward.append(0)
        calc_sharp.append(0)
        calc_std.append(0)
        name.append(0)
        final_w.append(0)
        final_name.append(0)
    
    skip_flag=0
    
    coef_check = 0
    final_coef_check = 100
    
    # v-=1
    hundred = 100
    

    #以5%到25%(30%)當作選股檔數的上下界-->4~20檔
    for num in range(20,21):
        # print("go")
        #各種組合的產出
        choose_code = list(combinations(code,num))  
        # print(choose_code)
    
        #跑每個組合的迴圈
        for i in range(int(comb(v,num))):
            
            
            becomezero(calc_reward)
            becomezero(calc_sharp)
            becomezero(calc_std)
            becomezero(name)
            becomehundred(upstd)
            becomehundred(w_code)
            becomezero(w)
            coef_check = 0
            final_coef_check = 100
            # print("123")
            #把組合裡面的ETF的年化報酬率和夏普值存進calc_reward,calc_sharp，等等計算加權平均出來的報酬率以及調整
            for j in range(num):
                calc_reward[j] = reward[choose_code[i][j]]
                calc_sharp[j] =  sharp[choose_code[i][j]]
                calc_std[j] = std[choose_code[i][j]]
                name[j] = v1[choose_code[i][j]]
            # print(name)
            #如果組合裡面沒有一個比預期的報酬率大就跳出，可以跑另外一個組合了
            if (np.max(calc_reward)) < expect_reward:
                continue
            
            # max_reward_index = calc_reward.index(np.max(calc_reward))
            sort_reward = sorted(calc_reward)
            sort_reward2=[]
            for j in range(len(sort_reward)):
                if sort_reward[j]>0:
                    sort_reward2.append(sort_reward[j])
            
            # print(sort_reward2)
            first_cal_reward = 0
            for j in range(num):
                first_cal_reward+=sort_reward2[j]*www[num-4][j]
                # if j == max_reward_index:
                #     first_cal_reward += calc_reward[j]*0.3
                # else:
                #     first_cal_reward += calc_reward[j]*0.7/(num-1)
            # print(first_cal_reward)
    # break
    # expect_reward-=0.002

            if first_cal_reward < expect_reward:
                continue
            
            for j in range(num):
                if calc_reward[j]>expect_reward:
                    upstd[j] = std[choose_code[i][j]]
            
            for j in range(num):
                if calc_reward[j]>expect_reward:
                    w_code[j] = choose_code[i][j]
    
            
    
            #先算各檔都是一樣的比例，在依照一樣的比例做調整=>每檔遵守5%~30%的原則
            ratio = 1/num
            
            for l in range(num):
                w[l] = ratio
    
            skip = upstd.index(min(upstd))
            upstd[skip]= hundred
            skip_partner = hundred
    
            coef_check = 0
            final_coef_check = 100
    
            
    
            #找跟 標準差最小的ETF 相關性最小的
            for j in range(num):
                if w_code[j] == hundred:
                    continue
                else:
                    a = (w_code[skip]+1)
                    b = (w_code[j]+1)
                    coef_check = corr_pd1[a][b]
                    if coef_check < final_coef_check:
                        final_coef_check = coef_check
                        skip_partner = j
            
            minus = 0
            if final_coef_check >= 0.7 :
                minus = minus + 1
                while (w[skip]<=0.29):
                    for m in range(num):
                        if (m != skip):
                            adjust = w[m] - (add/(num-minus))
                            if (adjust<0.05):
                               skip_flag = 1
                               break
                            else:
                                w[m] = adjust
                    if (skip_flag==1):
                        skip_flag = 0
                        break
                    w[skip] = w[skip]+ add
            else:
                # print("ya")
                upstd[skip_partner]= hundred
                minus = minus + 2
                while (w[skip]<=0.29 and w[skip_partner]<=0.29 ):
                    for m in range(num):
                        if (m != skip and m != skip_partner):
                            adjust = w[m] - (add/(num-minus))
                            if (adjust<0.05):
                                skip_flag = 1
                                break
                            else:
                                w[m] = adjust
                    if (skip_flag==1):
                        skip_flag = 0
                        break
                    w[skip] = w[skip]+ add
                    w[skip_partner] = w[skip_partner]+ add
    
            
            calc = 0
            for j in range(num):
                calc = calc + calc_reward[j]*w[j]
            
            
            
            #找出夏普值最大的那一個ETF代號
            while (calc<expect_reward):
                #已經無比預期報酬高的ETF
                if np.min(upstd)==hundred:
                    break
                
                #標準差最小的ETF
                skip = upstd.index(min(upstd))
                upstd[skip]= hundred
                coef_check = 0
                final_coef_check = 100
    
                #找跟 標準差最小的ETF 相關性最小的
                for j in range(num):
                    if w_code[j] == hundred:
                        continue
                    else:
                        a = (w_code[skip]+1)
                        b = (w_code[j]+1)
                        coef_check = corr_pd1[a][b]
                        if coef_check < final_coef_check:
                            final_coef_check = coef_check
                            skip_partner = j
    
                if final_coef_check >= 0.7 :
                    minus = minus+1
                    while (w[skip]<=0.29):
                        for m in range(num):
                            if (m != skip and upstd[m] != hundred):
                                adjust = w[m] - (add/(num-minus))
                                if (adjust<0.05):
                                   skip_flag = 1
                                   break
                                else:
                                    w[m] = adjust
                        if (skip_flag==1):
                            skip_flag = 0
                            break
                        w[skip] = w[skip]+ add
                    if np.min(upstd)==hundred:
                        break
                else:
                    # print("ya")
                    minus = minus + 2
                    upstd[skip_partner]= hundred
                    while (w[skip]<=0.29 and w[skip_partner]<=0.29 ):
                        for m in range(num):
                            if (m != skip and m != skip_partner and upstd[m]!=hundred ):
                                adjust = w[m] - (add/(num-minus))
                                if (adjust<0.05):
                                    skip_flag = 1
                                    break
                                else:
                                    w[m] = adjust
                        if (skip_flag==1):
                            skip_flag = 0
                            break
                        w[skip] = w[skip]+ add
                        w[skip_partner] = w[skip_partner]+ add
                    if np.min(upstd)==hundred:
                        break
    
                calc =0
                for j in range(num):
                    calc = calc + calc_reward[j]*w[j]
            # print(name)
            if (calc>expect_reward):
                
    
                w_d = 0
                for g in range(num): 
                    w_d += (w[g] ** 2) * (calc_std[g] ** 2)
                w_cov = 0
                w_cov1 = 0
                for g in range(num): 
                    for j in range(num):
                        # w_cov += (w[g] * calc_std[g]) * (w[g] * calc_std[j]) * corr_pd[name[g]][name[j]]
                        w_cov1 += (w[g] * calc_std[g]) * (w[g] * calc_std[j]) * corr_pd1[choose_code[i][g]+1][choose_code[i][j]+1]
    
                # risk = (w_d + w_cov) ** (1/2)
                risk = (w_d + w_cov1) ** (1/2)
            
                # if risk<min_risk:
                #     # min_risk1 = risk1
                #     min_risk = risk
                #     max_reward = calc
                #     for j in range(20):
                #         final_w[j] = w[j]
                #         final_name[j] = name[j]
                #     # print(final_w)
                #     # print(final_name)
                
            # print(name)
            # print(w)
            # print(risk)
            # print(calc)
    
                #######################歷史回測########################
                choose = []
                weight = []
                for x in range(20):
                    if name[x]!=0:
                        choose.append(name[x])
                        weight.append(w[x])
                # print(choose)
                # print(weight)
                # print(risk)
                # print(calc)
        
                    
                # db = pymysql.connect("localhost", "root", "esfortest", "etf")
                # cursor = db.cursor()
                
                # y = 999
                # for a in range(len(choose)):
                #     sql = "select 成立年限 from 性質表 where name = '"+choose[a]+"'"
                #     # print(sql)
                #     cursor.execute(sql)
                #     result_select = cursor.fetchall()
                #     db.commit()
                #     # print(result_select)
                #     if(result_select[0][0] < y ):
                #         y = result_select[0][0]-1
            
                # rewards = np.zeros(y)#放每年的報酬率
                    
                # for b in range(y):
                #     for c in range(len(choose)):
                #         sql = "select value from 各年報酬率 where (name = '"+choose[c]+"' and year = "+str(today.year-b-1) + ")"
                #         # print(sql)
                #         cursor.execute(sql)
                #         result_select = cursor.fetchall()
                #         db.commit()
                #         if len(result_select) >0:
                #             rewarddd = result_select[0][0]
                #         rewards[b] += rewarddd * weight[c]
                
            
                # db.close()
                 
                # result = []
                # rewards2 = []
                # for x in range(len(rewards)):
                #     result.append(str(rewards[len(rewards)-1-x]))
                #     rewards2.append(rewards[len(rewards)-1-x])
                    
                # result1 = ' '.join(result)
                
                
                # his_total_money = np.zeros(len(rewards)+1)
                # final_reward = 0
                # final_div = 0
                # for j in range(len(choose)):
                #     final_reward += reward_nodiv[v1.index(choose[j])]*weight[j]
                #     final_div += div[v1.index(choose[j])]*weight[j]
    
                # for i in range(1,len(rewards)+1):
                #     his_total_money[i] = his_total_money[i-1] * (rewards2[i-1]+1) * (float(final_div)+1) +1
                # # print(choose)
                # # print(weight)
                # # print(risk)
                # # print(calc)
                # if his_total_money[len(his_total_money)-1]>len(his_total_money)-1:
                #     # print("yes") #通過回測
                # final_name1 = []
                # final_w1 = []
                # for x in range(len(name)):
                #     if name[x]!=0:
                #         final_name1.append(str(final_name[x]))
                #         final_w1.append(str(final_w[x]))
            
                final_reward = 0
                final_div = 0
                for j in range(len(choose)):
                    final_reward += reward_nodiv[v1.index(choose[j])]*weight[j]
                    final_div += div[v1.index(choose[j])]*weight[j]
                final_w = []
                for i in range(len(choose)):
                    final_w.append(format(weight[i], '0.5f') ) 

                
                final_name2 = ' '.join(choose)
                # final_w2 = ' '.join(str(weight))
                final_w2 = ' '.join(final_w)
                final_div /=100
                final_div = format(final_div , '0.5f')
                final_reward = format(final_reward , '0.5f')
                max_reward = format(calc, '0.5f')
                min_risk = format(risk , '0.3f')
                
                # print(final_name2) #組合代號
                # print(final_w2) #比例
                # print(max_reward) #報酬率
                # print(min_risk) #標準差
                # # print(result1) #歷年報酬率
                # print(use_year_input) #0:月入 1:年入
                # print(final_reward) #不考慮配息的報酬率
                # print(final_div) #殖利率
                names.append(final_name2)
                wwws.append(final_w2)
                rw.append(max_reward)
                rsk.append(min_risk)
                exp_rw.append(expect_reward)
                y_in.append(use_year_input)
                nd_rw.append(final_reward)
                f_div.append(final_div)
                
    
                db = pymysql.connect("localhost", "root", "esfortest", "etf")
                cursor = db.cursor()

                sql2="insert into `選股結果` (`expect_reward`,`name`, `weight`,`reward`,`risk`,`y_input`,`nodiv_reward`, `dividend`  ) VALUES"
                # values = "('%s','%s',%f,'%s','%s','%s')"
                values = "(%f,'%s','%s',%f,%f,%d,%f,%f)"
                sql2 += values % (expect_reward,final_name2,final_w2,float(max_reward),float(min_risk),use_year_input,float(final_reward),float(final_div))
                # print(sql2)

                # try:
                #     cursor.execute(sql2)
                #     db.commit()
                #     # print("Data are successfully inserted")
                # except Exception as e:
                #     db.rollback()
                #     print("Exception Occured : ", e)


                # db.close()
    # break
    expect_reward-=0.003


        

endtime = datetime.datetime.now()

# print(expect_reward)
# print(names)
# print(wwws)
# print(rw)
# print(rsk)
# print(exp_rw)
total = pd.DataFrame(names,columns=['name'])
total = pd.concat([total, pd.DataFrame(wwws,columns=['w'])],axis=1)
total = pd.concat([total, pd.DataFrame(rw,columns=['reward'])],axis=1)
total = pd.concat([total, pd.DataFrame(rsk,columns=['risk'])],axis=1)
total = pd.concat([total, pd.DataFrame(exp_rw,columns=['expect_r'])],axis=1)
total = pd.concat([total, pd.DataFrame(y_in,columns=['y_in'])],axis=1)
total = pd.concat([total, pd.DataFrame(nd_rw,columns=['nodiv_r'])],axis=1)
total = pd.concat([total, pd.DataFrame(f_div,columns=['div'])],axis=1)

# print(total['expect_r'])
print(exp_rw[-1])
total.to_csv('C:/Users/User/Downloads/選股結果20檔_2.csv', index= False)

print((endtime-starttime).seconds)
