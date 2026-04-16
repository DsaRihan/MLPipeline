# MLP Project

## Overview

This project is designed for machine learning applications, focusing on data ingestion and storage using a SQLite database.

## Project Structure

- `app.py`: Main application file.
- `ingest.py`: Script for ingesting data into the database.
- `chroma_db/`: Directory containing the SQLite database and related files.
- `data/`: Directory for storing data files.

## Setup

1. Clone the repository.

2. Navigate to the project directory.

3. Create a virtual environment:
   
   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:
   
   ```bash
   source venv/bin/activate
   ```

5. Install required packages:
   
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application locally using Python:

```bash
python app.py
```

## 🚀 Running with Docker
If you want to run the application in an isolated container:

```bash
# Build the image
docker build -t my-ai-resume-app .

# Run the container (connecting to local Ollama)
docker run -p 8501:8501 -e OLLAMA_BASE_URL="http://host.docker.internal:11434" my-ai-resume-app
```

## 🏗️ Infrastructure as Code (Terraform)
This project includes a local Terraform setup to orchestrate the Docker container natively. To deploy using Terraform, ensure you have Docker Desktop running:

```bash
cd terraform
terraform init
terraform apply -auto-approve
```
The Streamlit application will be automatically built and become accessible at `http://localhost:8501`.

## ⚙️ CI/CD Pipeline
This repository uses **GitHub Actions** for Continuous Integration. Every push and pull request to the `main` branch automatically triggers a robust pipeline (`.github/workflows/docker-build.yml`) that verifies the environment and builds the Docker image to ensure the codebase remains stable.
