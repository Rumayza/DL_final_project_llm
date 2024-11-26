from transformers import pipeline

def query_llm(documents, question):
    """
    Query an LLM to generate a response based on retrieved documents.

    Args:
        documents (list of str): Retrieved documents to base the answer on.
        question (str): The user's question.

    Returns:
        str: The LLM's response.
    """
    # Combine the documents into a single context
    context = "\n".join(documents)
    input_text = f"Based on the following context: {context}\nAnswer the question: {question}"

    # Initialize the LLM (using Hugging Face's pipeline)
    qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-small")

    # Generate a response
    response = qa_pipeline(input_text, max_length=200, truncation=True)

    return response[0]['generated_text']

# Example for testing
if __name__ == "__main__":
    docs = ["Artificial Intelligence (AI) is a branch of computer science.", "AI involves creating intelligent machines."]
    question = "What is AI?"
    print(query_llm(docs, question))
