import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Avocado.csv")

df=df.copy()[df["type"]=='organic']

df["Date"]=pd.to_datetime(df["Date"])# This was written to tell pandas that date is an attribure which should't be overlapped

df.sort_values(by="Date", ascending=True, inplace=True) #this command sorts the data values rather than based on index

graph_df=pd.DataFrame()
colors = plt.cm.tab20.colors

for region in df["region"].unique():
    print(region)
    region_df = df[df["region"] == region].copy() 
    region_df.set_index("Date", inplace=True)
    region_df.sort_index(inplace=True)
    region_df[f"{region}_price25ma"]=region_df["AveragePrice"].rolling(25).mean()
    if graph_df.empty:
        graph_df=region_df[[f"{region}_price25ma"]]
        
    else:
        graph_df=graph_df.join(region_df[f"{region}_price25ma"])
#print(graph_df.tail(5))
#graph_df.plot() plt.show()
plt.figure(figsize=(14, 8))  # Set the figure size
for i, column in enumerate(graph_df.columns):
    plt.plot(graph_df.index, graph_df[column], label=column.split('_')[0], color=colors[i % len(colors)], linewidth=1.5)

plt.title("25-Day Moving Average of Organic Avocado Prices for Various Regions", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("25-Day Moving Average Price", fontsize=14)
plt.legend(loc='upper left', fontsize=10, ncol=2)  # Adjust legend location and font size
plt.grid(True, linestyle='--', alpha=0.7)  # Add grid lines

# Show the plot
plt.show()