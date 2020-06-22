import pandas as pd
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()

def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)
    
links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',\
       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}
       
dt = pd.read_csv(links["unemployment"])
dt1 = dt[dt["unemployment"]>=8.5]

dt2 = pd.read_csv(links["GDP"])
x = dt2["date"]
gdp_change = dt2["change-current"]
unemployment = dt["unemployment"]
title = "My_dashboard"
file_name = "index.html"


make_dashboard(x, gdp_change, unemployment, title, file_name)
