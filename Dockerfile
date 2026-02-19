# Use the full Python 3.10 image which has build tools pre-installed
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Create necessary directories for storage
RUN mkdir -p data/documents

# Expose ports for FastAPI (8000) and Streamlit (8501)
EXPOSE 8000
EXPOSE 8501

# Create a start script to launch both services simultaneously
RUN echo '#!/bin/bash\n\
    uvicorn app.main:app --host 0.0.0.0 --port 8000 & \n\
    streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0\n\
    wait -n\n\
    exit $?' > start.sh

# Make start script executable
RUN chmod +x start.sh

# Entry point triggers the start script
CMD ["./start.sh"]
