from input_handler import handle_input

def main():
    # Try text input
    text_prompt = "A small toy car"
    print("Handling text input...")
    handle_input(text_prompt)

    # Try image input
    image_path = "examples/sample.jpg"
    print("Handling image input...")
    handle_input(image_path)

if __name__ == "__main__":
    main()
 
