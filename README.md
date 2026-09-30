# JARVIS AI Assistant

A Python-based AI assistant inspired by JARVIS with:
- voice command input
- OpenAI-powered responses
- text-to-speech output
- startup configuration

## Features
- Speech-to-text via Google Speech Recognition
- AI responses via OpenAI ChatCompletion
- Text-to-speech via pyttsx3
- Easy environment-based configuration

## Prerequisites
- Python 3.10+
- Microphone access for voice input
- OpenAI API key

## Setup

1. Clone the repository
2. Create a virtual environment
3. Install dependencies
4. Create a `.env` file from `.env.example`
5. Run the app

## Install

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Configuration

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Run

```bash
python app.py
```
