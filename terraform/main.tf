terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

# Configure the Docker provider to connect to the local Docker daemon
provider "docker" {}

# Use Terraform to build the Docker image locally
resource "docker_image" "app_image" {
  name = "my-ai-resume-app:latest"
  
  build {
    context    = "${path.module}/.."
    dockerfile = "Dockerfile" # Relative to the build context
  }
}

# Use Terraform to run the container
resource "docker_container" "app_container" {
  name  = var.app_name
  image = docker_image.app_image.name

  ports {
    internal = 8501
    external = var.host_port
  }

  # Ensure it can communicate with Ollama hosted locally on the Mac
  env = [
    "OLLAMA_BASE_URL=http://host.docker.internal:11434"
  ]
}
