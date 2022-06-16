from cmath import exp
import csv
from encodings import utf_8
from stl import mesh # pip install numpy-stl
import numpy as np # installed with numpy-stl
import matplotlib.pyplot as plt # pip install matplotlib # pas necessaire pour prod


def export_to_csv_file(pts, out_filepath):
    with open(out_filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(pts)

def load_points_from_stl(file_path):
    stl_obj = mesh.Mesh.from_file(file_path)
    points = np.around(np.unique(stl_obj.vectors.reshape([int(stl_obj.vectors.size/3), 3]), axis=0),2)

    shift_x = min([pt[0] for pt in points])
    y = points[:,2]
    shift_y = (min(y) + max(y))/2.

    # Adjust shift and keep only top part of ski
    pts = [(pt[0] - shift_x, pt[2] - shift_y) for pt in points if pt[1] == 0.0 and pt[2] >= 0]

    return np.array(pts)

def get_points_intersect_in_mm(points, interval=10):
    const_pts = []
    x = points[:,0]
    y = points[:,1]

    def find_roots(x,y):
        s = np.abs(np.diff(np.sign(x))).astype(bool)
        return y[:-1][s] + np.diff(y)[s]/(np.abs(x[1:][s]/x[:-1][s])+1)

    for xc in range(interval, int(x[-1]), interval):
        yc = find_roots(x - xc, y)
        const_pts.append((xc, yc[0])) 

    return const_pts

def plot_vert_intersection(points, interval=10):
    """Outil de visualisation / non necessaire en prod"""
    x = points[:,0]
    y = points[:,1]

    for (xc, yc) in get_points_intersect_in_mm(points, interval=interval):
        plt.axvline(x=xc, linestyle=':', color='red')
        plt.plot(np.ones_like(yc)*xc, yc, marker="o", ls="", ms=4, color="limegreen")

    plt.plot(x, y, ".", x, y)
    plt.xlim([x[0]-1, x[-1] + 1 ])
    plt.axis('equal')

    plt.show()

def save_csv_from_stl(stl_filename, out_filepath, interval=10):
    original_pts = load_points_from_stl(stl_filename)
    pts = get_points_intersect_in_mm(original_pts, interval)
    export_to_csv_file(pts, out_filepath)

def example():
    pts = load_points_from_stl("BlackSki.stl")
    # plot_vert_intersection(pts, 50)
    get_points_intersect_in_mm(pts, interval=10)

# example()
