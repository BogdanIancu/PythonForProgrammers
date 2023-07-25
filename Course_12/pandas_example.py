import pandas as pd

df = pd.read_csv("files/data.csv")
print(df.shape)
print(df.info)
print(df["Price"].describe())
print(df.values[0][0])

filtered_data = df[(df["Price"] > 300) & (df["Price"] < 1000)]
print(filtered_data["Price"])
print(filtered_data.head(2))
copy = filtered_data.loc[1]
sorted_data = filtered_data.sort_values(by="Product Name", ascending=True)
print(sorted_data)
print(sorted_data["Product Name"])