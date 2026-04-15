from utils.metadata import get_file_metadata
import os

# Create a temporary file for testing
test_file = "test_metadata.txt"
with open(test_file, "w") as f:
    f.write("test content")

metadata = get_file_metadata(test_file)
print(f"Metadata for {test_file}:", metadata)

# Cleanup
os.remove(test_file)
