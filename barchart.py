import pandas as pd 
import plotly.express as px
df = pd.read_csv("data.csv")
pic = px.bar(df,x = "Country", y ="InternetUsers" )
pic.show()