import matplotlib.pyplot as plt

months = ['Jan','Feb','Mar','Apr','May','Jun',
          'Jul','Aug','Sep','Oct','Nov','Dec']

temperature = [25,27,30,33,35,34,32,31,30,29,27,26]
rainfall = [10,20,30,50,120,200,250,220,150,80,40,15]

plt.figure(figsize=(10,4))

# 1️⃣ Line Plot – Temperature
plt.subplot(1,2,1)
plt.plot(months, temperature)
plt.title("Monthly Temperature")
plt.xticks(rotation=45)

# 2️⃣ Scatter Plot – Rainfall
plt.subplot(1,2,2)
plt.scatter(range(1,13), rainfall)
plt.title("Monthly Rainfall")

plt.tight_layout()
plt.show()
