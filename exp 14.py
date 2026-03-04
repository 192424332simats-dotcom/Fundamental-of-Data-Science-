import pandas as pd

# Sample sales data stored in a DataFrame
data = {
    "Customer_ID": [101,102,103,104,105,106,107,108],
    "Age": [22,25,22,30,28,25,30,22],
    "Purchase_Amount": [250,300,150,400,500,350,450,200]
}

df = pd.DataFrame(data)

# Display DataFrame
print("Sales Data:\n")
print(df)

# Frequency distribution of ages
age_frequency = df["Age"].value_counts().sort_index()

print("\nFrequency Distribution of Customer Ages:\n")
print(age_frequency)
