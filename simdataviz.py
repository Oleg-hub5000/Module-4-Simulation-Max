from bokeh.plotting import figure, show


def read_file(filename):
    with open(filename, "r") as file:
        data = []
        for line in file:
            if line.strip():
                data.append(float(line.strip()))
    return data


sim1 = read_file("sim_data1.txt")
sim2 = read_file("sim_data2.txt")
sim3 = read_file("sim_data3.txt")

p = figure(
    title="Virus expand",
    # x_range=foods,
    x_axis_label="trial number",
    y_axis_label="time to full infection",
    width=500,
    height=350
)

p.line(list(range(1, len(sim1) + 1)), sim1, legend_label="sim1", line_color="green")
p.line(list(range(1, len(sim2) + 1)), sim2, legend_label="sim2", line_color="gold")
p.line(list(range(1, len(sim3) + 1)), sim3, legend_label="sim3", line_color="Purple")

show(p)
