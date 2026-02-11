import streamlit as st
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

def main():
    st.set_page_config(page_title="RAG Project AI", page_icon="🎲")
    st.title("🎲 Game Rules Assistant")
    st.markdown("Ask me anything about the rules in your Documents folder.")

    # 1. Initialize Chat History (Chat Memory)
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # 2. User Input
    if prompt := st.chat_input("What would you like to know?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 3. RAG Logic
        with st.spinner("Searching documents..."):
            # Prepare the DB
            embedding_function = OllamaEmbeddings(model="nomic-embed-text")
            db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

            # Search DB for context
            results = db.similarity_search_with_relevance_scores(prompt, k=3)
            
            context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
            prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
            full_prompt = prompt_template.format(context=context_text, question=prompt)

            # Generate response
            model = ChatOllama(model="mistral")
            response_text = model.invoke(full_prompt)

            # 4. Source Highlighting
            sources = [doc.metadata.get("id", None) for doc, _score in results]
            formatted_response = f"{response_text.content}\n\n**Sources:** {', '.join(filter(None, set(sources)))}"

        # Display assistant response
        with st.chat_message("assistant"):
            st.markdown(formatted_response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": formatted_response})

if __name__ == "__main__":
    main()