variable "app_name" {
  description = "The name of the Docker container"
  type        = string
  default     = "my-ai-resume-app-tf"
}

variable "host_port" {
  description = "The port exposed on your local machine"
  type        = number
  default     = 8501
}
