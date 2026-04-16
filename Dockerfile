FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
# build-essential and some other common libs usually help for libraries like PyMuPDF and Chroma
# if they don't have pre-built wheels for the target arch.
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the Streamlit default port
EXPOSE 8501

# Run the Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
