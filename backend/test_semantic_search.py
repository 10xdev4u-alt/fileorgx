import asyncio
from ai.embeddings import VectorDBManager
import os

async def test_semantic_search():
    vdb = VectorDBManager(persist_directory="./test_chroma")
    
    # Add sample contents
    documents = [
        {"id": 1, "text": "This is a document about machine learning and artificial intelligence."},
        {"id": 2, "text": "A receipt for a coffee from Starbucks in downtown San Francisco."},
        {"id": 3, "text": "Project roadmap for the next quarter, including frontend and backend tasks."},
        {"id": 4, "text": "Instructions for cooking the perfect Italian pasta carbonara."},
    ]
    
    for doc in documents:
        vdb.add_file_content(doc['id'], doc['text'], {"type": "test"})
    
    # Search
    queries = [
        "How to make pasta?",
        "AI and technology",
        "Coffee receipt",
        "Quarterly project goals"
    ]
    
    for query in queries:
        print(f"\nQuery: {query}")
        results = vdb.search(query, n_results=1)
        if results:
            print(f"Top Result: {results['documents'][0][0]}")
            print(f"Confidence: {results['distances'][0][0]}")

if __name__ == "__main__":
    asyncio.run(test_semantic_search())
