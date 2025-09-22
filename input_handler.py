from text_to_3d import generate_3d_from_text
from image_to_3d import generate_3d_from_image
import os

def handle_input(input_data):
    if isinstance(input_data, str):
        if os.path.isfile(input_data):  # Image file
            print(f"Detected image: {input_data}")
            generate_3d_from_image(input_data)
        else:  # Assume text
            print(f"Detected text prompt: '{input_data}'")
            generate_3d_from_text(input_data)
    else:
        raise ValueError("Invalid input. Please provide a text prompt or image path.")
