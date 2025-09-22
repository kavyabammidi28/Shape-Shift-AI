# text_to_3d.py

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def text_to_3d(text):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Generate coordinates for each letter
    x = []
    y = []
    z = []
    c = []

    for i, char in enumerate(text):
        # Spread letters along X-axis
        x.append(i)
        y.append(ord(char) % 10)  # create variation from ASCII
        z.append(ord(char) % 7)
        c.append(ord(char))       # color mapping

    # 3D scatter plot
    img = ax.scatter(x, y, z, c=c, cmap=cm.viridis, s=200)

    # Add labels
    for i, char in enumerate(text):
        ax.text(x[i], y[i], z[i], char, fontsize=12, color='red')

    ax.set_title("3D Visualization of Text")
    plt.colorbar(img)
    plt.show()

if __name__ == "__main__":
    text = input("Enter text to convert into 3D: ")
    text_to_3d(text)
