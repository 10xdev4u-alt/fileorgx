#!/bin/bash

# Check if Ollama is already installed
if command -v ollama &> /dev/null
then
    echo "Ollama is already installed."
    exit 0
fi

echo "Installing Ollama..."

# Install Ollama using the official script
curl -fsSL https://ollama.com/install.sh | sh

echo "Ollama installation complete."
echo "Please start the Ollama service and pull the required model:"
echo "ollama run llama3.2"
