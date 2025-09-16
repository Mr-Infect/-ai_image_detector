#!/bin/bash
echo "[*] Setting up virtual environment..."
python3 -m venv env
source env/bin/activate

echo "[*] Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "[*] Setup complete. Run the tool using:"
echo "python src/cli.py --image images/sample.jpg"
