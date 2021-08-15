#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import plotly.express as px


df = px.data.iris()
print (df)
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
fig.show()
fig.write_image('11_plotly.png')

fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="violin",
           marginal_x="box", trendline="ols", template="simple_white")

fig.show()
fig.write_image('11_plotly_trendline.png')