# Voice To Image AI Generator

## Overview

Voice To Image AI Generator is a Python-based artificial intelligence application that converts spoken voice input into AI-generated images. The project uses speech recognition to capture and transcribe the user's speech, enhances the text into a detailed image prompt, and generates high-quality images using Hugging Face inference models.

This project demonstrates the integration of:

* Speech Recognition
* Natural Language Prompt Engineering
* AI Image Generation APIs
* Python-based Automation

---

# Features

* Voice input using microphone
* Speech-to-text conversion
* AI prompt enhancement
* AI image generation from spoken description
* Direct image preview
* Modular and beginner-friendly Python implementation

---

# Technologies Used

* Python
* SpeechRecognition
* Hugging Face Inference API
* Pillow (PIL)
* python-dotenv

---

# Project Workflow

```text
Voice Input
    ↓
Speech Recognition
    ↓
Prompt Enhancement
    ↓
Hugging Face AI Model
    ↓
Generated Image
```

---

# Installation


---

## Install Required Libraries

```bash
pip install speechrecognition huggingface_hub pillow python-dotenv
```

---

# Hugging Face API Setup

## Create Access Token

1. Login to Hugging Face
2. Open Settings → Access Tokens
3. Create a new token
4. Enable:

   * Make calls to Inference Providers

---

## Create `.env` File

```env
apikey=your_huggingface_api_token
```

---

# Running the Project

Execute the following command:

```bash
python main.py
```

---

# Example Usage

## Voice Input

```text
"A futuristic cyberpunk city floating above the clouds"
```

---

## Enhanced Prompt

```text
Create a highly detailed cinematic image of a futuristic cyberpunk city floating above the clouds, ultra realistic, dramatic lighting, 4k quality.
```

---

## Generated Output

The application generates and previews an AI-created image based on the spoken description.

---
# Screenshots
---

## Generated AI Image

<p align="center">
  <img width="700" alt="image" src="https://github.com/user-attachments/assets/032f4f4d-46dc-4db5-b39b-db31b999e02d" />
</p>

---



# Important Notes

* Internet connection is required
* Hugging Face API token is required
