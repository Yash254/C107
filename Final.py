from numpy import FLOATING_POINT_SUPPORT
import pandas as pd
import csv
import plotly.graph_objects as pgo

df=pd.read_csv("data.csv")
sdf=df.loc[df['student_id']=="TRL_987"]
print(sdf.groupby("level")["attempt"].mean())

fig=pgo.Figure(pgo.Bar(
    x=sdf.groupby("level")["attempt"].mean(),
    y=['level 1','level 2',"level 3",'level 4'],
    orientation='h'
))

fig.show()