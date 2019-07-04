# -*- coding: utf-8 -*-
# @Time     : 2019/6/27 20:14
# @Author   ：Wang Haijun
# @File     : 回购.py
# @Software : PyCharm
from WindPy import w
w.start()
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'
hg=w.wset("stockrepobyevent","startdate=2008-01-01;enddate=2019-07-01")#取回购总账
dir(hg)
hg1=pd.DataFrame(hg.Data,index=hg.Fields,columns=hg.Codes)#wind数据转化为Dataframe数据
hg2=hg1.T#Df数据转置
hg4=hg2[~hg2.process.isin(['失效','停止实施','未完成'])]#去掉三项
yuqihuigoue=hg4['estimatedrepoquantity']*hg4['priceupper']
hg4.insert(16,'yuqihuigoue',yuqihuigoue)
qt_sl=hg4.loc[hg4['repopurpose']=='其他'].repopurpose.count()#计算其他的公司数
qt_je=hg4.loc[hg4['repopurpose']=='其他'].yuqihuigoue.sum()#计算其他的公司数
szgl_sl=hg4.loc[hg4['repopurpose']=='市值管理'].repopurpose.count()
szgl_je=hg4.loc[hg4['repopurpose']=='市值管理'].yuqihuigoue.sum()
ggqjlzx_sl=hg4.loc[hg4['repopurpose']=='股权激励注销'].repopurpose.count()
ggqjlzx_je=hg4.loc[hg4['repopurpose']=='股权激励注销'].yuqihuigoue.sum()
ssgqjl_sl=hg4.loc[hg4['repopurpose']=='实施股权激励'].repopurpose.count()
ssgqjl_je=hg4.loc[hg4['repopurpose']=='实施股权激励'].yuqihuigoue.sum()
ylbc_sl=hg4.loc[hg4['repopurpose']=='盈利补偿'].repopurpose.count()
ylbc_je=hg4.loc[hg4['repopurpose']=='盈利补偿'].yuqihuigoue.sum()
cz_sl=hg4.loc[hg4['repopurpose']=='重组'].repopurpose.count()
cz_je=hg4.loc[hg4['repopurpose']=='重组'].yuqihuigoue.sum()
hg4.to_excel(r'F:\wanghaijun\test\回购\数据\hg4.xlsx')
hg3=hg4[hg4.repopurpose.isin(['其他','市值管理','实施股权激励','重组'])]#去掉被动回购
hg3.to_excel(r'F:\wanghaijun\test\回购\数据\hg3.xlsx')
hg3['planannouncementdate']=pd.to_datetime(hg3['planannouncementdate'])#转换为datetime数据
#分区间统计回购情况
time1=datetime(2008,1,1)
time2=datetime(2008,12,31)
time3=datetime(2009,12,31)
time4=datetime(2010,12,31)
time5=datetime(2011,12,31)
time6=datetime(2012,12,31)
time7=datetime(2013,12,31)
time8=datetime(2014,12,31)
time9=datetime(2015,12,31)
time10=datetime(2016,12,31)
time11=datetime(2017,12,31)
time12=datetime(2018,11,1)
time13=datetime(2019,7,1)
z2008_yuqihuigoue=hg3.loc[(hg3['planannouncementdate']>=time1)&(hg3['planannouncementdate']<=time2)].yuqihuigoue.sum()
z2008_sl=hg3.loc[(hg3['planannouncementdate']>=time1)&(hg3['planannouncementdate']<=time2)].yuqihuigoue.count()
z2009_yuqihuigoue=hg3.loc[(hg3['planannouncementdate']>time2)&(hg3['planannouncementdate']<=time3)].yuqihuigoue.sum()
z2009_sl=hg3.loc[(hg3['planannouncementdate']>time2)&(hg3['planannouncementdate']<=time3)].yuqihuigoue.count()
z2010_yuqihuigoue=hg3.loc[(hg3['planannouncementdate']>time3)&(hg3['planannouncementdate']<=time4)].yuqihuigoue.sum()
z2010_sl=hg3.loc[(hg3['planannouncementdate']>time3)&(hg3['planannouncementdate']<=time4)].yuqihuigoue.count()
z2011_yuqihuigoue=hg3.loc[(hg3['planannouncementdate']>time4)&(hg3['planannouncementdate']<=time5)].yuqihuigoue.sum()
z2011_sl=hg3.loc[(hg3['planannouncementdate']>time4)&(hg3['planannouncementdate']<=time5)].yuqihuigoue.count()
z2012_yuqihuigoue=hg3.loc[(hg3['planannouncementdate']>time5)&(hg3['planannouncementdate']<=time6)].yuqihuigoue.sum()
z2012_sl=hg3.loc[(hg3['planannouncementdate']>time5)&(hg3['planannouncementdate']<=time6)].yuqihuigoue.count()
z2013_yuqihuigoue=hg3.loc[(hg3['planannouncementdate']>time6)&(hg3['planannouncementdate']<=time7)].yuqihuigoue.sum()
z2013_sl=hg3.loc[(hg3['planannouncementdate']>time6)&(hg3['planannouncementdate']<=time7)].yuqihuigoue.count()
z2014_yuqihuigoue=hg3.loc[(hg3['planannouncementdate']>time7)&(hg3['planannouncementdate']<=time8)].yuqihuigoue.sum()
z2014_sl=hg3.loc[(hg3['planannouncementdate']>time7)&(hg3['planannouncementdate']<=time8)].yuqihuigoue.count()
z2015_yuqihuigoue=hg3.loc[(hg3['planannouncementdate']>time8)&(hg3['planannouncementdate']<=time9)].yuqihuigoue.sum()
z2015_sl=hg3.loc[(hg3['planannouncementdate']>time8)&(hg3['planannouncementdate']<=time9)].yuqihuigoue.count()
z2016_yuqihuigoue=hg3.loc[(hg3['planannouncementdate']>time9)&(hg3['planannouncementdate']<=time10)].yuqihuigoue.sum()
z2016_sl=hg3.loc[(hg3['planannouncementdate']>time9)&(hg3['planannouncementdate']<=time10)].yuqihuigoue.count()
z2017_yuqihuigoue=hg3.loc[(hg3['planannouncementdate']>time10)&(hg3['planannouncementdate']<=time11)].yuqihuigoue.sum()
z2017_sl=hg3.loc[(hg3['planannouncementdate']>time10)&(hg3['planannouncementdate']<=time11)].yuqihuigoue.count()
z2018_yuqihuigoue=hg3.loc[(hg3['planannouncementdate']>time11)&(hg3['planannouncementdate']<=time12)].yuqihuigoue.sum()
z2018_sl=hg3.loc[(hg3['planannouncementdate']>time11)&(hg3['planannouncementdate']<=time12)].yuqihuigoue.count()
z2019_yuqihuigoue=hg3.loc[(hg3['planannouncementdate']>time12)&(hg3['planannouncementdate']<=time13)].yuqihuigoue.sum()
z2019_sl=hg3.loc[(hg3['planannouncementdate']>time12)&(hg3['planannouncementdate']<=time13)].yuqihuigoue.count()
data1={'预期回购金额':[z2008_yuqihuigoue,z2009_yuqihuigoue,z2010_yuqihuigoue,z2011_yuqihuigoue,z2012_yuqihuigoue,z2013_yuqihuigoue,z2014_yuqihuigoue,z2015_yuqihuigoue,z2016_yuqihuigoue,z2017_yuqihuigoue,z2018_yuqihuigoue,z2019_yuqihuigoue],'公布预案家数':[z2008_sl,z2009_sl,z2010_sl,z2011_sl,z2012_sl,z2013_sl,z2014_sl,z2015_sl,z2016_sl,z2017_sl,z2018_sl,z2019_sl]}
#年度回购预案图
df_data1=pd.DataFrame(data1,index=['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019'])
df_data1['预期回购金额']=df_data1['预期回购金额']/100000000#化单位为亿元
df_data1_x=df_data1.index
df_data1_y1=df_data1['预期回购金额']
df_data1_y2=df_data1['公布预案家数']
fig_data1=plt.figure()
ax1=fig_data1.add_subplot(1,1,1)
ax1.bar(df_data1_x,df_data1_y1,alpha=.4,color='r',label=u'预期回购金额')
ax1.set_ylabel('单位：亿元')
ax1.set_title('年度回购预案')
ax1.legend()
ax2=ax1.twinx()
ax2.plot(df_data1_x,df_data1_y2,'g',marker='*',label=u'公布预案家数(右轴）')
ax2.set_ylabel('单位：家')
ax2.legend(loc=9)
fig_data1.show()


zs=w.wsd("000300.SH", "close", "2007-12-31", "2019-07-01", "PriceAdj=F")#沪深300时间序列

;froewuitenrwoigew