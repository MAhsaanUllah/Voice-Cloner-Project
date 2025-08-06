FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (including espeak-ng)
RUN apt-get update && \
    apt-get install -y git espeak-ng libespeak-ng1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
