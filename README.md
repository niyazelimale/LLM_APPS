# LLM_APPS

All the codes are tested using Ollama llama 3.18B LLM in a "MacBook Air M4 24GB RAM".

**RAG**
```
- RAG is a  technique that can be implemented in framework like LangChain to enhance the performance of LLM particularly for factual accuracy and contextual relevance.
- RAG makes LLMs smarter and more reliable by giving them access to specific knowledge, reducing mistakes, improving the quality. 
- User query is query is converted as “vector embedding” and used to search the “knowledge base”. And it adds as a context to the original query. LLM receives the combined augmented prompt.
- (knowledge base to be created first by chunking the large documents into smaller pieces and creating embeddings for each chunk)
```

**LangChain**
```
- LangChain is a framework that provides the building blocks and orchestration capabilities to create LLM applications
- It makes the development, iteration, deployment of RAG systems significantly easier and more structured.
- It supports Document Loader, Text splitters, Embeddings, Vector stores. It also supports Retrievers.
```
