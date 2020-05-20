import matplotlib.pyplot as mpl
from die import Die

#d6
die = Die()

#Roll and store in list
results = []

for roll_num in range(100):
    result=die.roll()
    results.append(result)

# Analyze results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Bar graph here!! Show frequencies ^_^
mpl.hist(results, 50)

mpl.xlabel("Result")
mpl.ylabel("Frequency of Result")
mpl.title("Rolling a Die One Hundred times")

mpl.show()
