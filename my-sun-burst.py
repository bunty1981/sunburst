import pandas as pd
df = pd.read_csv("sample_data.csv")
print(df.columns)

import plotly.express as px
# fig is commonly used as convention in plotly figures
fig = px.sunburst(df, path=['Category', 'Level 1','Level 2'], values ='Total', title ='Budget Breakdown')

fig.show()
