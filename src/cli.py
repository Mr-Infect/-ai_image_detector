import argparse
from detector import load_model, preprocess_image, analyze_image

def main():
    parser = argparse.ArgumentParser(description="AI Image Detection Tool")
    parser.add_argument('--image', type=str, required=True, help='Path to the image to analyze')
    args = parser.parse_args()

    model = load_model()
    image_tensor = preprocess_image(args.image)
    confidence, classification, reasons = analyze_image(model, image_tensor)

    print(f"\nClassification Result: {classification}")
    print(f"Confidence Score: {confidence:.2f}")
    print("Reasons:")
    for reason in reasons:
        print(f" - {reason}")

if __name__ == '__main__':
    main()
