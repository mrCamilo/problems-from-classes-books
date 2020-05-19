import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

#Plot points
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()

ax.scatter(rw.x_values, rw.y_values, s=15)

plt.show()
