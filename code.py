import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("E:\WHITEHAT JR\python\P-108\data.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"])
fig.show()