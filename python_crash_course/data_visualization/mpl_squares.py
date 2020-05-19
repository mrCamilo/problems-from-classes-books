import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
cubes = [1, 8, 27, 64, 125]

#style
plt.style.use('seaborn-bright')

#begin generating plot
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
ax.plot(input_values, cubes, linewidth=3)

#Adds a title and labels
ax.set_title("Square Numbers", fontsize =24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#tick label size
ax.tick_params(axis='both', labelsize=14)

plt.show()
