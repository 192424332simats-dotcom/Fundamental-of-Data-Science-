import pandas as pd

age = [23,25,27,30,32]
fat = [12,14,15,18,20]

df = pd.DataFrame({"Age":age,"Fat":fat})

print("Mean:\n",df.mean())
print("Median:\n",df.median())
print("Std:\n",df.std())
