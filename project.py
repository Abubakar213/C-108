import random
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("project.csv")
Avg = df["Avg Rating"].tolist()

fig1 = ff.create_distplot([Avg],["Result"],show_hist = False)
fig1.show()

