#! bash
curl -s http://localhost:11434/api/generate \
-d '{"model": "llama3.2", "format": "json", "prompt": "What  is the meaning of life, the universe and everything?","stream": false,"options": { "temperature": 2.0 } }'
