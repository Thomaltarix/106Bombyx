
import sys
from matplotlib import pyplot
from matplotlib import animation

def update_plot(i, data_list_x, data_list_y, line):
    line.set_data(data_list_x[:i+1], data_list_y[:i+1])
    return line,

def main():
    filepath = sys.argv[1]
    file = open(filepath, "r")
    data_list_x = []
    data_list_y = []
    for data in file.readlines():
        data_list_x.append(float(data.split(" ")[0]))
        data_list_y.append(float(data.split(" ")[1]))


    fig = pyplot.figure()
    line, = pyplot.plot([], [], lw=2)
    pyplot.xlabel("x")
    pyplot.ylabel("y")
    pyplot.title("Data butterfly grapher")

    anim = animation.FuncAnimation(fig, update_plot, frames=len(data_list_x), fargs=(data_list_x, data_list_y, line), interval=200, blit=True)

    pyplot.show()
    file.close()

main();




# import sys
# from matplotlib import pyplot
# from matplotlib import animation


# def main():
#     filepath = sys.argv[1]
#     file = open(filepath, "r")
#     data_list_x = []
#     data_list_y = []
#     for data in file.readlines():
#         data_list_x.append(float(data.split(" ")[0]))
#         data_list_y.append(float(data.split(" ")[1]))

#     print(data_list_x)
#     print(data_list_y)
#     pyplot.plot(data_list_x, data_list_y)
#     pyplot.xlabel("x")
#     pyplot.ylabel("y")
#     pyplot.title("Data buterfly grapher")
#     pyplot.show()
#     file.close()