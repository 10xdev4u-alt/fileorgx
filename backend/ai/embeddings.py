import chromadb
from chromadb.utils import embedding_functions
from core.config import settings
from utils.logger import logger
import os

class VectorDBManager:
    """Manages semantic search and embeddings using ChromaDB."""
    
    def __init__(self, persist_directory=None):
        if persist_directory is None:
            persist_directory = os.path.join(settings.storage_path, "chroma")
        
        if not os.path.exists(persist_directory):
            os.makedirs(persist_directory)
            
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.embedding_fn = embedding_functions.DefaultEmbeddingFunction()
        self.collection = self.client.get_or_create_collection(
            name="files",
            embedding_function=self.embedding_fn
        )

    def add_file_content(self, file_id, content, metadata=None):
        """Adds file content to the vector database."""
        try:
            self.collection.add(
                documents=[content],
                ids=[str(file_id)],
                metadatas=[metadata] if metadata else None
            )
            return True
        except Exception as e:
            logger.error(f"Error adding to ChromaDB: {str(e)}")
            return False

    def search(self, query, n_results=5):
        """Searches for similar files based on a natural language query."""
        try:
            results = self.collection.query(
                query_texts=[query],
                n_results=n_results
            )
            return results
        except Exception as e:
            logger.error(f"Error searching ChromaDB: {str(e)}")
            return None

if __name__ == "__main__":
    vdb = VectorDBManager(persist_directory="./test_chroma")
    print("Vector storage module initialized.")
