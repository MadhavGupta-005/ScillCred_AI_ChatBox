import streamlit as st
import google.generativeai as genai

# genai configuration of API
api_key = "AIzaSyBUl7SuqejCdRJrygGOg44Y7cnePqniktU"
genai.configure(api_key=api_key)

# define a function to generate the response from llm
def get_gemini_response(question):
    response = genai.generate_text(prompt=question)  # Use generate_text method
    print(response)  # Print the response object for debugging
    # Extract the output from the response
    output = response.candidates[0]['output'] if response.candidates else "No candidates found."
    return output  # Return the extracted output

# setting up streamlit app
st.set_page_config(
    page_title="Gemini_pro",
    layout="wide",
    initial_sidebar_state="expanded"
)

# setting up header
st.header("My_Gemini_Pro_Q & A")

# input
question = st.text_input("Ask your Question")

# submit
if st.button("Submit Your Question"):
    response = get_gemini_response(question)
    st.write("YOU:", question)
    st.write("GEMINI:", response)  # Display the generated response
