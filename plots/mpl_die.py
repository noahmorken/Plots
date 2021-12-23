import matplotlib.pyplot as plt

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Make list of all possible sums.
sums = list(range(2, max_result+1))

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(sums, frequencies, linewidth=3)

# Set chart title and label axes.
ax.set_title("D6 Dice Rolls", fontsize=24)
ax.set_xlabel("Sum", fontsize=14)
ax.set_ylabel("Number of Occurrences", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()