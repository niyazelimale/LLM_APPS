# build_knowledge_db.py
from langchain.document_loaders import TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def build_chroma_db(doc_folder, persist_dir):
    docs = DirectoryLoader(doc_folder, glob="*.txt").load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    doc_splits = text_splitter.split_documents(docs)
    vector_db = Chroma.from_documents(
        doc_splits,
        embedding,
        persist_directory=persist_dir,
        collection_name="private_docs"
    )
    vector_db.persist()

if __name__ == "__main__":
    build_chroma_db(doc_folder="/Users/niyazea/Documents/Work/train_documents", persist_dir="chroma_db/")
