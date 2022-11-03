import pandas as pd
import matplotlib.pyplot as plt


##### (1990 ~ 2019) 자연재해 종류별 사망자 수 #####




## csv 파일 불러오기
df_death = pd.read_csv('../CSV/Disaster_Death.csv')
df_WorEms = pd.read_csv('../CSV/World-Carbon-Emission.csv')


## 사용할 데이터 만들기
year = df_death[['Year']]
drought = df_death[['Number of deaths from drought']]
earthquake = df_death[['Number of deaths from earthquakes']]
disaster = df_death[['Number of deaths from disasters']]
volcanic = df_death[['Number of deaths from volcanic activity']]
flood = df_death[['Number of deaths from floods']]
storm = df_death[['Number of deaths from storms']]
wildfire = df_death[['Number of deaths from wildfires']]
ex_temp = df_death[['Number of deaths from extreme temperatures']]
total_death = df_death[['Total_Death']]


Year = df_death['Year']
Drought = df_death['Number of deaths from drought']
Earthquake = df_death['Number of deaths from earthquakes']
Disaster = df_death['Number of deaths from disasters']
Volcanic = df_death['Number of deaths from volcanic activity']
Flood = df_death['Number of deaths from floods']
Storm = df_death['Number of deaths from storms']
Wildfire = df_death['Number of deaths from wildfires']
Ex_temp = df_death['Number of deaths from extreme temperatures']
Totla_Death = df_death['Total_Death']



year_ems = df_WorEms[['Year']]
total_ems = df_WorEms[['Total_Emission']]

Year_Ems = df_WorEms['Year']
Total_Ems = df_WorEms['Total_Emission']


fig = plt.figure(figsize=(20, 12))
plt.rcParams["font.family"] = "Malgun Gothic"



ax01 = fig.add_subplot(2, 2, 1)
ax01.plot(year, total_death , color = "red", marker = 'o')
plt.legend("Total Death")
plt.xlabel("년도")
plt.ylabel("사망자 수")
plt.title("자연재해로 인한 연간 총 사망자 수", fontsize = 20)



ax02 = fig.add_subplot(2,4,3)
ax02.plot(year, drought , color = "tan", marker = 'o')
plt.legend("drought")
plt.xlabel("년도")
plt.ylabel("사망자 수")
plt.title("가뭄으로 인한 사망자 수", fontsize = 15)

ax03 = fig.add_subplot(2,4,4)
ax03.plot(year, earthquake , color = "saddlebrown", marker = 'o')
plt.legend("earthquake")
plt.xlabel("년도")
plt.ylabel("사망자 수")
plt.title("지진으로 인한 사망자 수", fontsize = 15)

''''
ax04 = fig.add_subplot(2,4,5)
ax04.plot(year, volcanic, color = "mediumvioletred", marker = 'o')
plt.legend("volcanic")
plt.xlabel("년도")
plt.ylabel("사망자 수")
plt.title("화산활동으로 인한 사망자 수", fontsize = 10)
'''

ax05 = fig.add_subplot(2,4,5)
ax05.plot(year, flood, color = "deepskyblue", marker = 'o')
plt.legend("flood")
plt.xlabel("년도")
plt.ylabel("사망자 수")
plt.title("홍수로 인한 사망자 수", fontsize = 15)


ax06 = fig.add_subplot(2,4,6)
ax06.plot(year, storm, color = "turquoise", marker = 'o')
plt.legend("storm")
plt.xlabel("년도")
plt.ylabel("사망자 수")
plt.title("태풍으로 인한 사망자 수", fontsize = 15)


ax07 = fig.add_subplot(2,4,7)
ax07.plot(year, wildfire, color = "darkorange", marker = 'o')
plt.legend("wildfire")
plt.xlabel("년도")
plt.ylabel("사망자 수")
plt.title("산불로 인한 사망자 수", fontsize = 15)


ax08 = fig.add_subplot(2,4,8)
ax08.plot(year, ex_temp, color = "lawngreen", marker = 'o')
plt.legend("extreme Temp")
plt.xlabel("년도")
plt.ylabel("사망자 수")
plt.title("폭염/한파로 인한 사망자 수", fontsize = 15)






plt.savefig('../Graph_Img/world_disaster_death_summary.png', dpi = 100)
plt.show()