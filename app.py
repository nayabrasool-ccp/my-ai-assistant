import streamlit as st
import google.generativeai as genai

# Securely fetching your API Key from Streamlit Secrets
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("API Key missing! Please add GEMINI_API_KEY to your Streamlit advanced settings.")

st.set_page_config(page_title="My AI Assistant", page_icon="🤖")
st.title("🤖 Personal AI Assistant")
st.write("Ask me anything about coding, college, or tech!")

user_input = st.text_input("Type your question here:", placeholder="e.g., Explain what DevOps is")

if st.button("Ask Assistant"):
    if user_input:
        with st.spinner("Thinking..."):
            try:
                # Using the super fast and smart gemini-2.5-flash model
                model = genai.GenerativeModel("gemini-3.6-flash")
                response = model.generate_content(user_input)
                st.success("Response:")
                st.write(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please type a question first!")
