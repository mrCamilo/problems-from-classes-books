from die import Die

#d6
die = Die()

#Roll and store in list
results = []

for roll_num in range(100):
    result=die.roll()
    results.append(result)

print (results)
