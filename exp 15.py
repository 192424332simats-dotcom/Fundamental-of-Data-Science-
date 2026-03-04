import pandas as pd

# Sample dataset
data = {
    "Post_ID": [1,2,3,4,5],
    "Likes": [100,150,100,200,150]
}

df = pd.DataFrame(data)

print("User Interaction Data:\n")
print(df)

# Calculate frequency distribution
likes_frequency = df["Likes"].value_counts().sort_index()

print("\nFrequency Distribution of Likes:\n")
print(likes_frequency)
