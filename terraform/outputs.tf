output "app_url" {
  description = "The URL where the Streamlit application is hosted locally."
  value       = "http://localhost:${var.host_port}"
}

output "container_name" {
  description = "The Docker container name orchestrated by Terraform."
  value       = docker_container.app_container.name
}
