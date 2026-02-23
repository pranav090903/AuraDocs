# # Use the full Python 3.10 image
# FROM python:3.10-slim

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # Install system dependencies (CRITICAL for FAISS)
# RUN apt-get update && apt-get install -y \
#     libgomp1 \
#     && rm -rf /var/lib/apt/lists/*

# # Set working directory
# WORKDIR /app

# # Copy requirements and install dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application code
# COPY . .

# # Create necessary directories for storage
# RUN mkdir -p data/documents

# # Expose ports
# EXPOSE 8000
# EXPOSE 8501

# # Create a start script to launch both services
# # Added 'python -m' to uvicorn and streamlit for better compatibility
# RUN echo '#!/bin/bash\n\
#     python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 & \n\
#     python -m streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0\n\
#     wait -n\n\
#     exit $?' > start.sh

# RUN chmod +x start.sh

# CMD ["./start.sh"]
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies (for FAISS)
RUN apt-get update && apt-get install -y \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# HF Spaces requires port 7860
EXPOSE 7860

CMD ["streamlit", "run", "streamlit_app.py", "--server.port=7860", "--server.address=0.0.0.0"]