import pandas as pd
from collections import Counter

data = pd.DataFrame({
    'feedback':["good product", "good quality product", "bad product"]
})

text = " ".join(data["feedback"]).lower()
words = text.split()

freq = Counter(words)

N = int(input("Enter top N: "))
print(freq.most_common(N))
