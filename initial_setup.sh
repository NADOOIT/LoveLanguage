#!/bin/bash

# Create a new virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install Whisper
pip install -U openai-whisper

# Install ffmpeg
# For Ubuntu or Debian
sudo apt update && sudo apt install -y ffmpeg

# Print success message
echo "Setup completed successfully!"
