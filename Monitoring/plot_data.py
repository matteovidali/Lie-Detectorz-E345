import sched
import time
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# get csv file
file = input("filename: ")

# read chunk from csv file

# Set chunk size
CHUNK_SIZE = 100

# set rate in hz to read chunk from file
read_freq = 10


# read and plot that chunk

    

def animate(i):
    data = pd.read_csv(file)
    x = data["index"]
    ecg = data["ecg_value"]
    gsr = data["gsr_value"]


    plt.cla()
    plt.plot(x, ecg, label="ecg")
    plt.plot(x, gsr, label="gsr")

    plt.legend(loc="upper left")
    plt.tight_layout()


fig, axs = plt.subplots(5)

def animate_stacked(i):
    data = pd.read_csv(file)
    x = data["index"]
    ecg = data["ecg_value"]
    gsr = data["gsr_value"]
    q_stat = data["q_status"]
    a_stat = data["a_status"]


    axs[0].cla()
    axs[1].cla()
    axs[2].cla()
    axs[3].cla()
    axs[4].cla()


    axs[0].set_ylim(-0.5,1.5)
    axs[1].set_ylim(0, 0.35)


    starting_point = len(x) - 3000
    axs[0].plot(x[starting_point:], ecg[starting_point:], label="ecg")
    axs[1].plot(x[starting_point:], gsr[starting_point:], label="gsr")
    axs[2].plot(x[starting_point:], ecg[starting_point:], label="stacked")
    axs[2].plot(x[starting_point:], gsr[starting_point:])
    axs[3].plot(x[starting_point:], a_stat[starting_point:], label = "a_stat")
    axs[4].plot(x[starting_point:], q_stat[starting_point:], label = "q_stat")
    
    fig.legend(loc="upper right")

    
    
ani = FuncAnimation(fig, animate_stacked, interval=10)

plt.show()
