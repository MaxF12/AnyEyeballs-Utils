import matplotlib.pyplot as plt

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = open("NetworkFramework.txt", "r")
    first = f.readline().split(",{")
    intial_ts = first[0][1:]
    ts = [0]
    lines = [first[1:]]
    for line in f:
        line = line.split(",{")
        ts.append(int(line[0][1:])-int(intial_ts))
        lines.append(line[1:])
    totals = []
    for i in range(0,len(lines[0])):
        total = []
        v4 = []
        v6 = []
        for line in lines:
            print(line)
            print(i)
            line = line[i].replace("}","")
            total.append(float(line.split(",")[1]))
            v4.append(float(line.split(",")[2]))
            v6.append(float(1-float(line.split(",")[2])))
        plt.plot(ts, v4, 'r', label="v4")
        totals.append(total)
        plt.plot(ts, v6, 'g', label="v6")
        plt.xlabel("Node " + str(i))
        plt.legend()
        plt.show()
    print(totals)
    plt.plot(ts, totals[1], 'r', label="Oregon")
    plt.plot(ts, totals[2], 'g', label="Sao Paulo")
    plt.plot(ts, totals[5], 'b', label="Singapore")
    plt.plot(ts, totals[4], 'c', label="Frankfurt")
    plt.plot(ts, totals[0], 'm', label="Dublin")
    plt.plot(ts, totals[3], 'y', label="London")
    plt.xlabel("Time in seconds")
    plt.ylabel("Load in percent")
    plt.legend()
    plt.show()
    print(ts)