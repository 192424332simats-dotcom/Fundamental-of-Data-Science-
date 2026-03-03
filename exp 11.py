import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

month_numbers = [1,2,3,4,5,6,7,8,9,10,11,12]

temperature = [25, 27, 30, 33, 35, 34, 32, 31, 30, 29, 27, 26]
rainfall = [10, 20, 30, 50, 120, 200, 250, 220, 150, 80, 40, 15]

plt.figure(figsize=(12,4))

# Line Plot
plt.subplot(1,2,1)
plt.plot(months, temperature, marker='o')
plt.title("Monthly Temperature")
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")
plt.grid(True)

# Scatter Plot
plt.subplot(1,2,2)
plt.scatter(month_numbers, rainfall)
plt.title("Monthly Rainfall")
plt.xlabel("Month Number")
plt.ylabel("Rainfall (mm)")

plt.tight_layout()
plt.show()
