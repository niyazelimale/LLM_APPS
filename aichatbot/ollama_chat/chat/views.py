from django.shortcuts import render

# Create your views here.

# chat/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .llm import ollama_chat
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

class ChatbotAPIView(APIView):
    def post(self, request, format=None):
        question = request.data.get("message")
        embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vector_db = Chroma(
            persist_directory="chat/chroma_db/", collection_name="private_docs", embedding_function=embedding
        )
        retriever = vector_db.as_retriever()
        docs = retriever.get_relevant_documents(question)
        context = "\n".join(doc.page_content for doc in docs)
        aug_prompt = f"Answer this question using the following internal docs:\n{context}\n\nQuestion: {question}"
        answer = ollama_chat(aug_prompt)
        return Response({"response": answer})

def chat_home(request):
    return render(request, "chat/chat.html")
