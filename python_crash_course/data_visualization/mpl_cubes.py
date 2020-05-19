import matplotlib.pyplot as plt

x_values = range(1, 100)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-dark')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

ax.set_title("Cubed Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Value Cubed", fontsize =14)

plt.show()

#ax.axis([0, 1100, 0, 110000])
