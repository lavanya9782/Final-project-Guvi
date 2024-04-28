import streamlit as st
from transformers import pipeline

def main():
    st.title("Question Answering Demo")

    # Choose a Hugging Face model
    #model_name = st.selectbox("Select a model:", ["distilbert-base-cased", "bert-base-uncased", "LavanyaM/lavan"])

    # Load the selected model
    qa_model = pipeline("question-answering", model="LavanyaM/lavan")
    st.write("Model used : LavanyaM/lavan")
    question = st.text_input("Enter your question:")
    context = st.text_area("Enter the context:")

    # Button to trigger question answering
    if st.button("Get Answer"):
        if question and context:
            # Get the answer using the loaded model
            answer = qa_model(question=question, context=context)
            st.write(f"Answer: {answer['answer']}")
        else:
            st.error("Please enter both question and context.")

if __name__ == "__main__":
    main()
