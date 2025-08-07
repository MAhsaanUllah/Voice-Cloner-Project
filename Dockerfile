FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install git and espeak-ng
RUN apt-get update && \
    apt-get install -y git espeak-ng && \
    apt-get clean

# Copy project files
COPY . .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]

ENV REBUILD_TRIGGER="2025-08-06-05-35PM"
