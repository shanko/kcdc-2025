#! bash
curl -s http://localhost:11434/api/generate \
-d '{"model": "llama3.2", "format": "json", "prompt": "What  is 2 + 2?","stream": true,"options": { "temperature": 0 } }'
