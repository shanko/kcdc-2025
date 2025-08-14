# Ollama API Examples

This folder contains examples demonstrating different ways to interact with the Ollama API for running local language models. The examples show how to use both direct HTTP requests and the official Ollama Python client library.

## Overview

Ollama is a tool that allows you to run large language models locally on your machine. These examples demonstrate various approaches to interact with Ollama's API:

1. **Shell Script (cURL)** - Direct HTTP API calls using cURL
2. **Python with requests** - HTTP API calls using Python's requests library
3. **Python with ollama library** - Using the official Ollama Python client

## Files Description

### `curl_ollama_api.sh`
A simple bash script that demonstrates how to make a direct HTTP request to the Ollama API using cURL.

**Features:**
- Uses the `llama3.2` model
- Requests JSON format response
- Enables streaming
- Sets temperature to 0 for deterministic responses

### `ollama_example_0.py`
An interactive Python script that creates a simple chat interface using the requests library.

**Features:**
- Interactive command-line chat interface
- Non-streaming responses
- Simple loop that continues until user types "q"
- Direct HTTP API calls to Ollama

### `ollama_example_1.py`
A basic Python script demonstrating a single API call using the requests library.

**Features:**
- Simple one-time API call
- Basic error handling
- Uses JSON serialization for the request payload

### `ollama_example_2.py`
A more advanced example using the official Ollama Python library with complex prompts.

**Features:**
- Uses the official `ollama` Python client
- Demonstrates structured prompting techniques
- Shows how to handle complex, multi-part prompts
- Examples include business consulting scenarios

## Prerequisites

### 1. Install Ollama
First, you need to install Ollama on your system:

```bash
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows
# Download from https://ollama.ai/download
```

### 2. Pull the Required Model
```bash
ollama pull llama3.2
```

### 3. Start Ollama Server
```bash
ollama serve
```
The server will start on `http://localhost:11434` by default.

### 4. Install Python Dependencies
For the Python examples, install the required packages:

```bash
# For examples using requests library
pip install requests

# For example using ollama library
pip install ollama
```

## How to Test

### Testing the Shell Script
1. Make sure Ollama is running (`ollama serve`)
2. Make the script executable:
   ```bash
   chmod +x curl_ollama_api.sh
   ```
3. Run the script:
   ```bash
   ./curl_ollama_api.sh
   ```

### Testing Python Examples

#### Example 0 (Interactive Chat)
```bash
python ollama_example_0.py
```
- Type your questions at the prompt
- Type "q" to quit

#### Example 1 (Single Request)
```bash
python ollama_example_1.py
```

#### Example 2 (Advanced Prompting)
```bash
python ollama_example_2.py
```

## Expected Output

### Shell Script
You should see a streaming JSON response with the model's answer to "What is 2 + 2?"

### Python Examples
- **Example 0**: Interactive chat session where you can ask questions
- **Example 1**: A response object (may need modification to see actual content)
- **Example 2**: Detailed business consulting advice for website development

## Troubleshooting

### Common Issues

1. **Connection Refused Error**
   - Make sure Ollama is running: `ollama serve`
   - Check if the service is running on port 11434

2. **Model Not Found Error**
   - Pull the required model: `ollama pull llama3.2`
   - Verify available models: `ollama list`

3. **Python Import Errors**
   - Install required packages: `pip install requests ollama`

4. **Slow Responses**
   - This is normal for local LLM inference
   - Response time depends on your hardware capabilities

## API Reference

### HTTP Endpoint
- **URL**: `http://localhost:11434/api/generate`
- **Method**: POST
- **Content-Type**: application/json

### Key Parameters
- `model`: The model to use (e.g., "llama3.2")
- `prompt`: The input text/question
- `stream`: Boolean for streaming responses
- `format`: Response format ("json" for structured output)
- `options.temperature`: Controls randomness (0 = deterministic)

## Next Steps

- Experiment with different models available in Ollama
- Try different temperature settings for varied response creativity
- Explore streaming vs non-streaming responses
- Build more complex applications using these examples as a foundation

## Resources

- [Ollama Official Documentation](https://ollama.ai/)
- [Ollama Python Library](https://github.com/ollama/ollama-python)
- [Available Models](https://ollama.ai/library)
