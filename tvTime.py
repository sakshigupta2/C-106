import numpy as np 
import csv
import pandas as pd 
import plotly.express as px
with open("tvTime.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Size of TV", y="Average time spent watching TV")
    fig.show()
def getDataSource(data_path):
    sizeOfTv = []
    averageTimeSpent = []
    with open(data_path) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            sizeOfTv.append(float(row["Size of TV"]))
            averageTimeSpent.append(float(row["Average time spent watching TV"]))
    return {"x":sizeOfTv, "y":averageTimeSpent}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation Between Size of TV vs Average time spent watching TV:- \n---", correlation[0,1])
def setUp():
    data_path = "tvTime.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
setUp()