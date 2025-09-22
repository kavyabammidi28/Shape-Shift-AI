import cv2
from rembg import remove
import os
from PIL import Image
import numpy as np

def generate_3d_from_image(image_path):
    print(f"Processing image: {image_path}")

    # Load and remove background
    with open(image_path, "rb") as img_file:
        result = remove(img_file.read())
    
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    bg_removed_path = os.path.join(output_dir, "bg_removed.png")
    with open(bg_removed_path, "wb") as out_file:
        out_file.write(result)

    print(f"Background removed image saved to {bg_removed_path}")

    # Optional: convert to grayscale or edge map
    img = cv2.imread(bg_removed_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    edge_path = os.path.join(output_dir, "edges.png")
    cv2.imwrite(edge_path, edges)
    print(f"Edge-detected image saved to {edge_path}")
