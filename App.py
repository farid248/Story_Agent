import streamlit as st
from Agent import build_graph, NarrativeState

st.title("Story Agent")
st.write("Enter an idea and get a narrative with an image!")

user_input = st.text_input("Your idea:")

if st.button("Generate"):
    if user_input:
        with st.spinner("Generating..."):
            graph = build_graph()
            state = NarrativeState(
                user_input=user_input,
                messages=[],
                narrative=None,
                visual_url=None,
                visual_prompt=None
            )
            result = graph.invoke(state)
            
            st.subheader("Narrative:")
            st.write(result["narrative"])

            st.subheader("Generated Image:")
            if result["visual_url"]:
                st.image(result["visual_url"], width=500)
            else:
                st.error("Image generation failed, try again!")
    else:
        st.warning("Please enter an idea first!")
