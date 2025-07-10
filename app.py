import streamlit as st
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = Ollama(model="llama3")

st.title("🛠 Zero-Cost Artifact Generator")
user_prompt = st.text_area("Describe your idea (e.g. Build a to-do app):")

if st.button("Generate Artifact"):
    if user_prompt.strip() == "":
        st.warning("Please enter a prompt first.")
    else:
        template = PromptTemplate(
            input_variables=["user_prompt"],
            template="You are a professional developer. {user_prompt}"
        )
        chain = LLMChain(llm=llm, prompt=template)

        with st.spinner("Generating..."):
            result = chain.run(user_prompt)

        st.subheader("🔧 Generated Artifact Code:")
        st.code(result, language="python")
