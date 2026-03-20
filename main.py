 
from Agent import build_graph, NarrativeState

def run():
    graph = build_graph()
    state = NarrativeState(
        user_input="",
        messages=[],
        narrative=None,
        visual_url=None,
        visual_prompt=None
    )
    
    user_input = input("Enter your idea: ")
    state["user_input"] = user_input
    result = graph.invoke(state)
    
    print("\nNarrative:")
    print(result["narrative"])
    print("\nGenerated Image:")
    print(result["visual_url"])

if __name__ == "__main__":
    run()