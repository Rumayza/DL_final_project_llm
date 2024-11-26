import streamlit as st
from retrieval_models import retrieve_documents
from llm_pipeline import query_llm

# Streamlit App Title
st.title("RAG Pipeline")

# Introduction and Description
st.markdown("""
Welcome to the **Retrieval-Augmented Generation (RAG) Pipeline** demo! 
This application combines document retrieval and a Large Language Model (LLM) to answer your queries.
You can ask questions about:
- **AI Topics**: e.g., "What is AI?", "What are the ethical concerns of AI?", "How does AI impact the job market?"
- **Books**: e.g., "What is 'Pride and Prejudice' about?", "Who is Alice in 'Alice's Adventures in Wonderland'?"
- **Articles**: e.g., "How is AI being used in education?", "What are the advancements in healthcare with AI?"
Select your desired retrieval method, type your question, and let the system provide relevant documents and responses!
""")

# Sidebar Description
st.sidebar.title("Topics Covered")

st.sidebar.write("This application uses **document retrieval** and a **Large Language Model (LLM)** to provide insights and answers. It works with the following sources:")

# Books Section
st.sidebar.subheader("Books")
st.sidebar.write("""
- **Pride and Prejudice** by Jane Austen
- **Frankenstein** by Mary Shelley
- **Alice's Adventures in Wonderland** by Lewis Carroll
- **A Modest Proposal** by Jonathan Swift
- **The Adventures of Tom Sawyer** by Mark Twain
""")

# Articles Section
st.sidebar.subheader("Articles")
st.sidebar.write("""
Explore articles on topics such as:
- AI in Education
- Ethical Concerns of AI
- AI in Healthcare
- Automation and Jobs
- AI and Climate Change
""")

# Wikipedia Topics Section
st.sidebar.subheader("Wikipedia Topics")
st.sidebar.write("""
Dive into topics like:
- Artificial Intelligence
- Machine Learning
- Neural Networks
- Philosophy of AI
- Robotics
- Quantum Computing
- Blockchain Technology
- Space Exploration
- Internet of Things (IoT)
""")

st.sidebar.title("How It Works")
st.sidebar.write("""
1. **Select Retrieval Method**: Choose between TF-IDF, KeyBERT, or Hugging Face.
2. **Enter Your Question**: Type a question or phrase to explore.
3. **Search and Discover**: Retrieve relevant documents and responses.
""")


# User Input
st.subheader("Enter your Query")
user_query = st.text_input("Enter your question:", "")

st.subheader("Select a Retrieval Method")
retrieval_method = st.selectbox(
    "Choose a retrieval method:",
    options=["TF-IDF", "KeyBERT", "Hugging Face"],
    help="Select the method to retrieve relevant documents."
)

if st.button("Search"):
    if user_query.strip() == "":
        st.warning("Please enter a valid question.")
    else:
        st.write("Retrieving documents...")

        try:
            method_mapping = {
                "TF-IDF": "tfidf",
                "KeyBERT": "keybert",
                "Hugging Face": "huggingface",
            }

            retrieved_docs = retrieve_documents(user_query, method=method_mapping[retrieval_method])

            if not retrieved_docs:
                st.error("No documents were found for the given query. Please try another question.")
            else:
                st.subheader("Retrieved Documents:")
                for i, doc in enumerate(retrieved_docs):
                    st.markdown(f"**Document {i + 1}:**")
                    
                    with st.expander(f"Preview Document {i + 1}"):
                        preview = ' '.join(doc.split('.')[:4]) + "..."  # Preview of first 4 sentences
                        st.write(preview)
                        st.write(doc)  # Full document in expander

                # Query the LLM
                st.write("Querying LLM...")
                llm_response = query_llm(retrieved_docs, user_query)
                st.subheader("LLM Response:")
                st.write(llm_response)
        except ValueError as e:
            st.error(str(e))
