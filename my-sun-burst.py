# #! ~/.anaconda3/envs/sunburst/bin/python

# This script creates a sunburst chart from a CSV file and saves it as an HTML file.
# >> conda activate sunburst # to activate the conda environment, run command in terminal


import pandas as pd
df = pd.read_csv("sample_data.csv")
print(df.columns)

import plotly.express as px
# fig is commonly used as convention in plotly figures
fig = px.sunburst(df, path=['Category', 'Level 1','Level 2'], values ='Total', title ='Budget Breakdown')
fig.show()

fig.write_html("docs/my-sun-burst.html")
