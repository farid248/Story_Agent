# Story_Agent 
# StoryStream AI

An agentic AI system built with LangGraph that takes your idea and generates a creative story with an AI image.

## How it works
1. You enter an idea
2. Orchestra node analyzes it and plans the output
3. Story Writer node writes a vivid creative story
4. Image Generator node creates an image using HuggingFace Stable Diffusion

## Tech Stack
- LangGraph for orchestration
- Groq (Llama 3.1) for LLM
- HuggingFace Stable Diffusion XL for image generation
- Streamlit for UI

## Setup
1. Clone the repo
2. Create a `.env` file based on `.env.example`
3. Fill in your API keys
4. Install dependencies: `pip install -r requirements.txt`
5. Run the app: `streamlit run app.py`

## Required API Keys
- `GROQ_API_KEY` - from console.groq.com
- `HF_TOKEN` - from huggingface.co/settings/tokens

## Example
Input: `a dragon who loves coffee`

Output: A full story + AI generated image of the dragon!
