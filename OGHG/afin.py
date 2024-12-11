import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as pg

library = {
    1: 'matplotlib',
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


def rotate_points(X, Y, angle_deg):
    angle_rad = np.radians(angle_deg)
    center = np.array([480, 480])
    points = np.array([X, Y]).T - center
    rotation_matrix = np.array([
        [np.cos(angle_rad), np.sin(angle_rad)],
        [-np.sin(angle_rad), np.cos(angle_rad)]
    ])
    rotated_points = points @ rotation_matrix
    rotated_points += center

    return rotated_points[:, 0], rotated_points[:, 1]

X_new, Y_new = rotate_points(X, Y, 30)

def plot_points(mode, text):
    plt.figure(figsize=(960/100, 960/100))
    plt.title(text)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    if mode == 0 or mode == 2:
        plt.scatter(X_new, Y_new, c="skyblue")
    if mode == 1 or mode == 2:
        plt.scatter(X, Y, c="black")
    plt.show()

def figure_plot():
    # I created 3  different windows with 1st, 2nd and 2 plots together
    plot_points(1, "Default")
    plot_points(0, "Rotated")
    plot_points(2, "Two together")


def menu():
    while True:
        print('''\nMenu:
1. Matplotlib
0. Exit.''')
        try:
            choice = int(input("Enter the number of an action: "))
            if choice == 1:
                figure_plot()
            elif choice == 0:
                print('Thank you)')
                break
            else:
                print("Try again!!!")
        except ValueError:
            print("Error!")
menu()
