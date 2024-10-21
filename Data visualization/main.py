import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as pg

library = {
    1: 'matplotlib',
    2: 'plotly'
}

with open("DS2.txt", 'r') as dataset_file:
    dataset = dataset_file.read()

dataset = dataset.replace(" ", ",")
dataset_list = [x for x in dataset.split("\n")]
dataset_list.remove("")
X = []
Y = []
for el in dataset_list:
    row = el.split(",")
    X.append(int(row[0]))
    Y.append(int(row[1]))

def figure_plot(lib_num):
    if lib_num == 1:
        plt.figure(figsize=(960/100, 540/100))
        plt.title("Scatter Plot of Points (Matplotlib)")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.scatter(X, Y, c="black")
        plt.show()
    if lib_num == 2:
        fig = pg.Figure(pg.Scatter(x = X, y = Y, mode="markers",
        marker=dict(color=Y, size=5, colorscale="icefire", colorbar=dict(title="Colorbar"))))

        fig.update_layout(
        title='Scatter Plot of Points (Plotly)',
        xaxis_title='X-axis',
        yaxis_title='Y-axis',
        width=960,
        height=540,
        plot_bgcolor='rgba(134, 215, 227, 0.3)',
        margin=dict(l=40, r=40, t=40, b=40),  # Відстані від країв
        )
        fig.show()

def menu():
    while True:
        print('''\nChoose the number of library:
1. Matplotlib
2. plotly
0. Exit.''')

        try:
            choice = int(input("Enter the number of library: "))
            if choice == 1:
                figure_plot(1)
            elif choice == 2:
                figure_plot(2)
            elif choice == 0:
                print('Thank you)')
                break
            else:
                print("Try again!!!")
        except ValueError:
            print("Error!")
menu()
