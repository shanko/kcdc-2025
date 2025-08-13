# kcdc-2025

## Prerequisites: 
Laptop with at least 16 GB of RAM and 40 GB of free disk space

## Setup:
1. Signup for Github [Account](https://github.com) and clone the [Repo](https://github.com/shanko/kcdc-2025)
2. Install [Python](https://python.org) version 3.10 or above 
3. Create and activate virtual env for python3 that you installed, in the cloned repo:
```
$ python3 -m venv venv
$ source venv/bin/activate
```
4. Install the following Python packages using pip (e.g. `pip install -r requirements.txt`):
   - langchain 
   - langchain-chroma
   - langchain-community
   - langchain-core
   - langchain-ollama
   - langgraph
   - ollama
   - pandas
   - torch
   - transformers 
5. IF you are on Windows, 
   - EITHER install [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install)
   - OR Install Ollama for [Windows](https://github.com/ollama/ollama/blob/main/docs/windows.md)
   ELSE Install [Ollama](https://ollama.com) and pull the following models:

```
$ ollama pull tinyllama
$ ollama pull mxbai-embed-large
$ ollama pull llama3.2
```

## Optional:
1. Install [Windsurf](https://windsurf.com)
2. Install [ngrok](https://ngrok.com/downloads/mac-os)
3. Signup for [Google Colab](https://colab.research.google.com)
4. Signup for [Lovable](https://lovable.dev)
5. Signup for [Huggingface](https://huggingface.co)
