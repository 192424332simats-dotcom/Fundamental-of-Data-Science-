import pandas as pd

# Sample user interaction data
data = {
    "Post_ID": [1, 2, 3, 4, 5, 6, 7, 8],
    "Likes": [100, 150, 100, 200, 150, 300, 200, 100]
}

df = pd.DataFrame(data)

print("User Interaction Data:\n")
print(df)

# Calculate frequency distribution of likes
likes_frequency = df["Likes"].value_counts()

print("\nFrequency Distribution of Likes:\n")
print(likes_frequency)
