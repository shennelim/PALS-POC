#Use LangChain SemanticChunker
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings

from langchain_chroma import Chroma

def semantic_chunking(documents_loaded, embeddings_model=OpenAIEmbeddings()):

    # Create the text splitter
    text_splitter = SemanticChunker(embeddings_model)

    splitted_documents = []

    for doc in documents_loaded:
        # Split the documents into smaller chunks
        splitted_documents.append(text_splitter.split_documents(doc))

    # Print the number of documents after splitting
    print(f"Number of documents after splitting: {len(splitted_documents)}")


    # Create the vector database
    vectordb = Chroma.from_documents(
        documents=splitted_documents,
        embedding=embeddings_model,
        collection_name="embedding_semantic",
        persist_directory="./vector_db"
    )

    return vectordb