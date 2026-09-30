# JARVIS AI Assistant (Free with Ollama)

A Python-based AI assistant inspired by JARVIS using Ollama — completely free, runs locally on your computer.

## Features
- 100% FREE (no API costs)
- Runs locally on your machine
- No internet needed after setup
- Voice commands optional
- Text-based chat by default
- Uses Llama 3.2 (open-source AI model)

## Prerequisites
- Python 3.10+
- Ollama installed
- 4GB+ RAM recommended

## Setup

### Step 1: Install Ollama

1. Go to: https://ollama.com/download
2. Download and install for your OS
3. Open terminal and run:

```bash
ollama pull llama3.2
```

This downloads the AI model (takes 5-10 minutes).

### Step 2: Start Ollama Server

Open a terminal and run:

```bash
ollama serve
```

Leave this running. You should see:
```
listening on 127.0.0.1:11434
```

### Step 3: Setup Python Project

In another terminal, go to your project folder:

```bash
cd path/to/JARVIS-AI-Assistant
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate it:

**Windows:**
```bash
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Step 4: Run JARVIS

```bash
python app.py
```

You should see:
```
JARVIS online. Type your commands (type 'exit' to quit):

You:
```

Type a question and press Enter!

## Example

```
You: What is Python?
JARVIS: Python is a high-level programming language...

You: Tell me a joke
JARVIS: Why don't scientists trust atoms? Because they make up everything!

You: exit
JARVIS: Goodbye.
```

## How it Works

1. You type a question
2. Python sends it to Ollama (running locally)
3. Ollama uses Llama 3.2 AI model to generate a response
4. Response appears in your terminal

## Cost

**$0** — Everything runs on your computer, no API fees!

## Optional: Add Voice

To add voice input/output later:
- Install pyaudio and pyttsx3
- Uncomment voice functions in src/assistant.py

## Troubleshooting

**Error: "Connection refused"**
- Make sure `ollama serve` is running in another terminal

**Model not found**
- Run: `ollama pull llama3.2`

**Slow responses**
- Ollama runs on your CPU. Upgrade to GPU if possible.

## Next Steps

- Add voice commands
- Add smart home integration
- Customize AI personality
- Add more models (llama2, mistral, etc.)

## Models Available

Try these models with Ollama:
- `llama3.2` (default, best balance)
- `llama2` (smaller, faster)
- `mistral` (good for coding)
- `neural-chat` (conversational)

Change model in code by editing: `model="llama3.2"` to `model="llama2"`
