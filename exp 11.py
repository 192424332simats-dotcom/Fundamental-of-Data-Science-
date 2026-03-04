import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [1200, 1500, 1700, 1600, 2000, 2200]

plt.figure(figsize=(12,4))

# Line Plot
plt.subplot(1,3,1)
plt.plot(months, sales)
plt.title("Line")

# Scatter Plot
plt.subplot(1,3,2)
plt.scatter(range(1,7), sales)
plt.title("Scatter")

# Bar Plot
plt.subplot(1,3,3)
plt.bar(months, sales)
plt.title("Bar")

plt.tight_layout()
plt.show()
