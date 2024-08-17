import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Avocado.csv")

df["Date"]=pd.to_datetime(df["Date"])# This was written to tell pandas that date is an attribure which should't be overlapped

#print(df.head())

albany_df=df[df["region"]=="Albany"].copy() #with this command we call only those places that are in reagion albany in the csv

albany_df.set_index("Date", inplace=True) 

#print(df)

albany_df.sort_index(inplace=True) #with this command we will sort the index of the csv which is not sorted

#albany_df["AveragePrice"].plot() #this is tp plot a graph to plot the graph of the average price in albany

albany_df["AveragePrice"].rolling(25).mean().plot()#with this we will calculate the mean of the .25   

#plt.show()
###With this we xan plot the graph of the albany region, but there are other regions so what if we want to compare all the regions with one another.
#for this to happen we need to know all the unique locations we have.

#print(df["region"].unique())#With this we now know all the unique locations 

graph_df=pd.DataFrame()

for region in df["region"].unique()[:16]:
    print(region)
    region_df = df[df["region"] == region].copy() 
    region_df.set_index("Date", inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f"{region}_price25ma"]=albany_df["AveragePrice"].rolling(25).mean()
    
    if graph_df.empty:
        graph_df=region_df[[f"{region}_price25ma"]]

    else:
        graph_df=graph_df.join(region_df[f"{region}_price25ma"])
#the problem with this is that is requires a lot of ram to process making the whole thing slow

