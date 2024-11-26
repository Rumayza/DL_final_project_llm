import streamlit as st
from retrieval_models import retrieve_documents
from llm_integration import query_llm

# Define llm_pipeline function
def llm_pipeline(query, retrieval_method, data_dir):
    """
    Combines document retrieval and LLM response generation into a single pipeline.

    Args:
        query (str): The user's question or input.
        retrieval_method (str): The retrieval method to use (e.g., "tfidf", "keybert", "huggingface").
        data_dir (str): The directory where data is stored.

    Returns:
        dict: Contains retrieved documents and the LLM-generated response.
    """
    # Retrieve relevant documents
    retrieved_docs = retrieve_documents(query, method=retrieval_method, data_dir=data_dir)
    if not retrieved_docs:
        return {
            "retrieved_documents": [],
            "llm_response": "No relevant documents were found for the query."
        }

    # Generate LLM response
    llm_response = query_llm(retrieved_docs, query)

    return {
        "retrieved_documents": retrieved_docs,
        "llm_response": llm_response
    }

# Streamlit interface for debugging (optional, for standalone execution)
if __name__ == "__main__":
    st.title("RAG Pipeline")

    st.write("**Ask a question, and the system will retrieve relevant documents and generate a response!**")

    # User Input
    query = st.text_input("Enter your question:", "")

    if st.button("Search"):
        if query.strip() == "":
            st.warning("Please enter a valid question.")
        else:
            st.write("Retrieving documents...")
            # Use default retrieval method and data directory for debugging
            result = llm_pipeline(query, retrieval_method="tfidf", data_dir="data")

            # Display retrieved documents
            st.subheader("Retrieved Documents:")
            for i, doc in enumerate(result["retrieved_documents"]):
                st.write(f"Document {i + 1}: {doc}")

            # Display LLM response
            st.subheader("LLM Response:")
            st.write(result["llm_response"])

    st.sidebar.title("How it works")
    st.sidebar.write("""
    1. **Enter your question**: Type any question you have in the text box.
    2. **Retrieve Documents**: The system fetches the most relevant documents from the database.
    3. **Generate a Response**: The LLM analyzes the documents and provides a coherent answer.
    """)

    st.sidebar.title("About")
    st.sidebar.info("""
    This is a Retrieval-Augmented Generation (RAG) pipeline demo that combines document retrieval and a large language model (LLM) to answer questions intelligently. 
    """)
