# AI Image Detector CLI

A simple Command-Line Interface (CLI) tool to detect whether an image is AI-generated or real using a ResNet-based classifier.  
Designed for offline use in WSL environments with fast inference and progress reporting.

---

## 🚀 Overview

This tool uses a pre-trained ResNet18 model (from ImageNet) to perform basic image analysis and classify input images into two categories:
- ✅ Real Image  
- ⚠️ Possibly AI-Generated Image  

It provides confidence scores and reasons for the classification decision.

---

## ⚙️ How It Works

1. **Model Loading**  
   The tool loads a pre-trained ResNet18 model from `torchvision.models` with weights trained on ImageNet.

2. **Image Preprocessing**  
   Input images are resized to 224x224 pixels and normalized with standard ImageNet mean/std.

3. **Inference & Analysis**  
   The image tensor is passed through the ResNet model to compute softmax probabilities over 1000 ImageNet classes.  
   A simple heuristic determines the output:
   - If the top class probability ≥ 0.85 → Classified as Real Image.
   - Otherwise → Classified as Possibly AI-Generated.

4. **Progress Bar**  
   Displays a progress bar during image analysis using `tqdm` for a better user experience.

---

## ⚡ Usage

```bash
source env/bin/activate
python src/cli.py --image images/test17.jpg
````

**Example Output:**

```plaintext
Classification Result: Possibly AI-Generated
Confidence Score: 0.07
Reasons:
 - Low classifier confidence: 0.07
 - Unusual class prediction
```

---

## ✅ Project Structure

```plaintext
ai_image_detector/
├── model/
│   └── forensic_model.pth  # (Optional pre-trained model)
├── images/
│   └── test17.jpg          # Test image
├── results/
├── src/
│   ├── detector.py         # Core image analysis logic
│   └── cli.py              # CLI interface
├── requirements.txt
├── setup.sh
├── README.md
└── .gitignore
```

---

## ⚠️ Important Disclaimers & Disadvantages

This tool is a **prototype** and should NOT be used for mission-critical forensic investigations.
⚠️ The current model (ResNet18 pretrained on ImageNet) is NOT designed for AI-generated vs real image classification.

### Key Disadvantages:

* ❌ Model is trained for general object classification (ImageNet), not forensic detection.
* ❌ No learned features specific to AI artifacts (e.g., texture inconsistencies, frequency artifacts).
* ❌ High false positives / false negatives expected.
* ✅ Suitable for demonstration and prototyping only.

---

## ✅ Future Improvements

* Train a dedicated forensic classifier (ResNet/Xception) on a real dataset like FaceForensics++.
* Use data augmentation techniques to simulate AI-generated artifacts during training.
* Build a proper custom threshold and confidence calibration system.
