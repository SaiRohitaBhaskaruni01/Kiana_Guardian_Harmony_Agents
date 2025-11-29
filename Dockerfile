FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System dependencies for llama-cpp-python
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    curl \
    libomp-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# ---- Download model from HuggingFace (BEST PRACTICE) ----
RUN mkdir -p /app/models && \
    curl -L \
    https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf \
    -o /app/models/tinyllama.gguf

COPY . .

EXPOSE 8000

CMD ["streamlit", "run", "login_app.py", "--server.port=8000", "--server.address=0.0.0.0"]
