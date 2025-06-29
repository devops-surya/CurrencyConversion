variable "helm_release_name" {
  description = "Name of the Helm release"
  type        = string
}

variable "cluster_name" {
  description = "EKS Cluster name for targeting Kubernetes"
  type        = string
}

