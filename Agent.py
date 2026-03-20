from typing import Optional, List
from typing_extensions import TypedDict
from langchain_core.messages import SystemMessage, HumanMessage, AnyMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# LLM Setup
creative_llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.8)

# State Definition
class NarrativeState(TypedDict):
    user_input: Optional[str]
    messages: List[AnyMessage]
    narrative: Optional[str]
    visual_url: Optional[str]
    visual_prompt: Optional[str]

# Node 1: Director
director_instructions = """You are a creative director. Given a user idea, your task is to:
1. Write a brief imaginative story (3-4 sentences) inspired by the idea
2. Create a vivid image description (1 sentence) that visually represents the story
Reply strictly in this format:
STORY: [write story here]
IMAGE_PROMPT: [write image prompt here]"""

def director_node(state: NarrativeState) -> NarrativeState:
    messages = [
        SystemMessage(content=director_instructions),
        HumanMessage(content=state["user_input"])
    ]
    response = creative_llm.invoke(messages)
    state["messages"] = messages + [response]
    content = response.content
    narrative = ""
    visual_prompt = ""
    if "STORY:" in content and "IMAGE_PROMPT:" in content:
        narrative = content.split("STORY:")[1].split("IMAGE_PROMPT:")[0].strip()
        visual_prompt = content.split("IMAGE_PROMPT:")[1].strip()
    state["narrative"] = narrative
    state["visual_prompt"] = visual_prompt
    return state

# Node 2: Writer
writer_instructions = """You are a talented fiction writer.
Expand the given story into a more detailed and emotional version.
Keep it to 2 paragraphs only."""

def writer_node(state: NarrativeState) -> NarrativeState:
    messages = [
        SystemMessage(content=writer_instructions),
        HumanMessage(content=state["narrative"])
    ]
    response = creative_llm.invoke(messages)
    state["narrative"] = response.content
    return state

# Node 3: Visual Generator
def visual_node(state: NarrativeState) -> NarrativeState:
    prompt = state["visual_prompt"]
    HF_TOKEN = os.getenv("HF_TOKEN")
    API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    if response.status_code == 200:
        with open("generated_image.png", "wb") as f:
            f.write(response.content)
        state["visual_url"] = "generated_image.png"
    else:
        print(response.status_code)
        print(response.text)
        state["visual_url"] = None
    return state

# Build Graph
def build_graph():
    graph = StateGraph(NarrativeState)
    graph.add_node("director", director_node)
    graph.add_node("writer", writer_node)
    graph.add_node("visual_generator", visual_node)
    graph.add_edge(START, "director")
    graph.add_edge("director", "writer")
    graph.add_edge("writer", "visual_generator")
    graph.add_edge("visual_generator", END)
    return graph.compile()
