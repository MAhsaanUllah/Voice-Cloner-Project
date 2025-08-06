# Force rebuild - v2

FROM python:3.10-slim

WORKDIR /app

# Install espeak-ng and git
RUN apt-get update && \
    apt-get install -y git espeak-ng libespeak-ng1 && \
    apt-get clean

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
