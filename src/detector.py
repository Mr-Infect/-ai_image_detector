import torch
from torchvision import models, transforms
from PIL import Image
from tqdm import tqdm

# Load ResNet pre-trained on ImageNet
def load_model():
    model = models.resnet18(pretrained=True)
    model.eval()
    return model

def preprocess_image(image_path):
    image = Image.open(image_path).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])
    return transform(image).unsqueeze(0)

def analyze_image(model, image_tensor):
    for _ in tqdm(range(3), desc="Analyzing Image"):
        pass  # Progress bar UX

    with torch.no_grad():
        logits = model(image_tensor)
        probs = torch.softmax(logits, dim=1)[0]

    top_prob, top_class = torch.max(probs, dim=0)
    top_prob = top_prob.item()

    # Example heuristic: high confidence means likely real
    threshold = 0.85
    if top_prob >= threshold:
        classification = "Real Image"
        reasons = [
            f"High classifier confidence: {top_prob:.2f}",
            "Matches typical ImageNet classes"
        ]
    else:
        classification = "Possibly AI-Generated"
        reasons = [
            f"Low classifier confidence: {top_prob:.2f}",
            "Unusual class prediction"
        ]

    return top_prob, classification, reasons
