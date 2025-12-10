# Local File MCP Server

This repository provides a minimal MCP (Model Context Protocol) server that exposes basic file-system tools for LLMs to read, modify and add files inside a configured root folder.

Quick start

1. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

2. (Optional) Configure environment variables:

```bash
export MCP_ROOT=./files
export MCP_API_KEY=your-secret-key
export MCP_MAX_FILE_SIZE=10485760  # 10 MB
```

3. Run the server:

```bash
python server.py
# or
uvicorn server:app --reload
```

Endpoints

- `GET /tools` - returns the tool manifest
- `GET /files?path=&recursive=` - list files
- `GET /file?path=` - read file (text or base64)
- `POST /file` - write file `{path, content, encoding}`
- `PATCH /file` - append file `{path, content, encoding}`
- `POST /upload?target_path=` - multipart file upload
- `DELETE /file?path=` - delete file or empty directory

Security and safety

- Requests are restricted to the configured `MCP_ROOT` folder to prevent traversal.
- Optionally protect the API using `MCP_API_KEY` header.
- Max file size is enforced by `MCP_MAX_FILE_SIZE`.

If you'd like, I can:
- Add unit tests
- Add a small client helper library for LLM tool usage
- Add OpenAPI examples for each tool
