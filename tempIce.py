import numpy as np 
import csv
import pandas as pd 
import plotly.express as px
with open("tempIce.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Temperature", y="Ice-cream Sales")
    fig.show()
def getDataSource(data_path):
    temperature = []
    iceCreamSales = []
    with open(data_path) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            temperature.append(float(row["Temperature"]))
            iceCreamSales.append(float(row["Ice-cream Sales"]))
    return {"x":temperature, "y":iceCreamSales}
def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation Between Temperature vs Ice-cream Sale:- \n---", correlation[0,1])
def setUp():
    data_path = "tempIce.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
setUp()
    
