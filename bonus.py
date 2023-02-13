
import sys
from matplotlib import pyplot

def main():
    filepath = sys.argv[1]
    file = open(filepath, "r")
    data_list_x = []
    data_list_y = []
    for data in file.readlines():
        data_list_x.append(int(data.split(" ")[0]))
        data_list_y.append(int(data.split(" ")[1]))

    print(data_list_x)
    print(data_list_y)
    pyplot.plot(data_list_x, data_list_y)
    pyplot.xlabel("x")
    pyplot.ylabel("y")
    pyplot.title("Data buterfly grapher")
    pyplot.show()
    file.close()

main();
