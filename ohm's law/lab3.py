import random
import matplotlib.pyplot as plt
import time

try:
    temp = []

    for t in range(10):
        value = 25 + random.uniform(-1, 1)
        temp.append(value)

        with open("temp.csv", "a") as f:
            f.write(f"{t},{value}\n")

        time.sleep(0.5)

    plt.plot(temp)
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (C)")
    plt.title("Temperature Log")
    plt.show()

    csv_file = open("data.csv", "w")
    txt_file = open("log.txt", "w")

    csv_file.write("Timestamp,Temperature,Humidity\n")
    txt_file.write("Log Data\n")
    txt_file.write("--------------------\n")

    Temp_list = []
    hum_list = []
    time_list = []

    for i in range(10):
        t = time.strftime("%H:%M:%S")
        temperature = 25 + random.uniform(-1, 1)
        hum = 50 + random.uniform(-5, 5)

        Temp_list.append(temperature)
        hum_list.append(hum)
        time_list.append(i)

        csv_line = str(t) + "," + str(temperature) + "," + str(hum) + "\n"
        csv_file.write(csv_line)

        txt_line = "Time: " + str(t) + " | Temp: " + str(temperature) + " | Hum: " + str(hum) + "\n"
        txt_file.write(txt_line)

        time.sleep(1)

    csv_file.close()
    txt_file.close()

except Exception:
    print("An error occurred")
