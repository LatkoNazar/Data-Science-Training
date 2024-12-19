import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def load_dataset(file_path):
    try:
        return pd.read_csv(file_path).values
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

def central_projection_matrix(d):
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 1 / d],
        [0, 0, 1 / d, 0]
    ])

def project_points(points, matrix):
    homogeneous_points = np.hstack((points, np.full((points.shape[0], 1), 100), np.ones((points.shape[0], 1))))
    projected_points = homogeneous_points @ matrix.T
    with np.errstate(divide='ignore', invalid='ignore'):
        projected_points[:, :3] /= projected_points[:, 3][:, np.newaxis]
        projected_points[:, :3] = np.nan_to_num(projected_points[:, :3])
    return projected_points[:, :3]

def visualize_and_save(points, output_file, canvas_size):
    plt.figure(figsize=(canvas_size[0] / 100, canvas_size[1] / 100))
    plt.scatter(points[:, 0], points[:, 1], c='blue', s=10)
    plt.savefig(output_file, bbox_inches='tight', dpi=100)
    plt.show()

if __name__ == "__main__":
    input_file = "./lab4/lab3_data.csv"
    output_file = "./lab4/projected_points.png"
    canvas_size = (960, 540)
    points = load_dataset(input_file)
    if points is None:
        exit()
    while True:
        try:
            choice = int(input("Enter 'd': "))
            break
        except ValueError:
            print("Error!")
    d = choice
    matrix = central_projection_matrix(d)
    projected_points = project_points(points, matrix)
    visualize_and_save(projected_points, output_file, canvas_size)
    print(f"Проєкція завершена. Результат збережено у файл {output_file}.")
