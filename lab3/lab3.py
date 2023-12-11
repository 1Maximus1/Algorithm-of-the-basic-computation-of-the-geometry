import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

def read_dataset(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        points = [list(map(int, line.split())) for line in lines]
        return np.array(points)

def find_convex_hull(points):
    hull = ConvexHull(points)
    return hull

canvas_size = (960, 540)

def plot_convex_hull(points, hull):
    plt.figure(figsize=(canvas_size[0]/80, canvas_size[1]/80))
    plt.scatter(points[:,1], points[:,0], c='red', label='Data Points')
    for simplex in hull.simplices:
        plt.plot(points[simplex, 1], points[simplex, 0], 'b-')
    plt.title('Convex Hull')
    plt.legend()
    plt.xlim(0, canvas_size[0])
    plt.ylim(0, canvas_size[1])
    plt.savefig('result_DS4.png')
    plt.show()

file_path = 'DS4.txt'
dataset = read_dataset(file_path)

convex_hull_result = find_convex_hull(dataset)

plot_convex_hull(dataset, convex_hull_result)
