# Story Agent

An AI-powered agentic system that transforms your ideas into vivid narratives and stunning visuals.

## How It Works

The system uses a 3-node pipeline built with LangGraph:

1. **Director Node** - Analyzes your idea and creates a story outline + image description
2. **Writer Node** - Expands the outline into a rich, detailed narrative
3. **Visual Generator Node** - Creates an image based on the story using Stable Diffusion

## Tech Stack
- LangGraph - for building the agentic pipeline
- Groq (Llama 3.3-70b) - for story generation
- HuggingFace Stable Diffusion XL - for image generation
- Streamlit - for the web interface

## Setup

1. Clone the repo
2. Create a virtual environment:
```bash
   python -m venv venv
   venv\Scripts\activate
```
3. Install dependencies:
```bash
   pip install -r requirements.txt
```
4. Create a `.env` file based on `.env.example` and add your API keys
5. Run the app:
```bash
   streamlit run App.py
```

## Required API Keys
- `GROQ_API_KEY` - from console.groq.com (free)
- `HF_TOKEN` - from huggingface.co/settings/tokens (free)

## Example
Input: `a lonely robot exploring an abandoned city`

The system will generate a full narrative + an AI image of the scene!
