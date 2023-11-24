import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pandas as pd
# 转换 "totals" 列的数据类型

font = FontProperties(fname=r'NotoSansTC-VariableFont_wght.ttf')
df = pd.read_csv('外包_Homework _ (鍾旭哲).csv', encoding='utf-8')


# 品牌銷售額比較
brand_sales = df.groupby('Brand')['totals'].sum()
plt.figure(figsize=(15, 8))
brand_sales.plot(kind='bar', color='skyblue')
plt.xticks(range(len(brand_sales.index)), brand_sales.index, rotation=45, ha='right', fontproperties=font)
plt.title('品牌銷售額比較', fontproperties=font, fontsize=20)
plt.xlabel('品牌', fontproperties=font, fontsize=15)
plt.ylabel('總銷售額(百萬)', fontproperties=font, fontsize=15)
plt.show()



# 不同頻道銷售額比較
channel_sales = df.groupby('channel')['totals'].sum()
plt.figure(figsize=(15, 8))
channel_sales.plot(kind='bar', color='lightcoral')
plt.title('通路銷售額比較', fontproperties=font, fontsize=20)
plt.xlabel('通路', fontproperties=font, fontsize=15)
plt.xticks(range(len(channel_sales.index)), channel_sales.index, rotation=45, ha='right', fontproperties=font)
plt.ylabel('總銷售額(百萬)', fontproperties=font, fontsize=15)
plt.show()



# 商品總銷售額排名
brand_ranking = df.groupby('Brand')['totals'].sum().sort_values(ascending=True)
plt.figure(figsize=(15, 8))
plt.barh(brand_ranking.index, brand_ranking, color='skyblue')
plt.yticks(range(len(brand_ranking.index)), brand_ranking.index, ha='right', fontproperties=font, fontsize=12)
plt.ylabel('品牌', fontproperties=font, fontsize=15)
plt.xlabel('總銷售額(百萬)', fontproperties=font, fontsize=15)
plt.title('品牌銷售額排名', fontproperties=font, fontsize=20)
plt.show()