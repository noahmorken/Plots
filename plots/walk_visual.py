from plotly.graph_objs import Bar, Layout
from plotly import offline
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    frequencies = []
    north = 0
    northeast = 0 
    east = 0
    southeast = 0
    south = 0
    southwest = 0
    west = 0
    northwest = 0

    for path in range(1, rw.num_points):
        horizontal = rw.x_values[path] - rw.x_values[path-1]
        vertical = rw.y_values[path] - rw.y_values[path-1]

        if horizontal == 0 and vertical > 0:
            south += 1
        elif horizontal == 0 and vertical < 0:
            north += 1
        elif horizontal > 0 and vertical == 0:
            west += 1
        elif horizontal < 0 and vertical == 0:
            east += 1
        elif horizontal > 0 and vertical < 0:
            northeast += 1
        elif horizontal > 0 and vertical > 0:
            southeast += 1
        elif horizontal < 0 and vertical > 0:
            southwest += 1
        elif horizontal < 0 and vertical < 0:
            northwest += 1

    frequencies.append(north)
    frequencies.append(northeast)
    frequencies.append(east)
    frequencies.append(southeast)
    frequencies.append(south)
    frequencies.append(southwest)
    frequencies.append(west)
    frequencies.append(northwest)

    # Visualize the results.
    x_values = ["North", "Northeast", "East", "Southeast", "South", "Southwest",
            "West", "Northwest"]
    data = [Bar(x=x_values, y=frequencies)]

    x_axis_config = {'title': 'Direction'}
    y_axis_config = {'title': 'Frequency of Direction'}
    my_layout = Layout(title='Path Chosen By Random Walk',
            xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='walk_direction.html')

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break