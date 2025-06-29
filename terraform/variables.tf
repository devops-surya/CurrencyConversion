variable "aws_region" {
  description = "AWS Region"
  type        = string
  default     = "us-east-1"
}

variable "vpc_name" {
  description = "Name for the VPC"
  type        = string
  default     = "prod-vpc"
}

variable "cluster_name" {
  description = "EKS Cluster name"
  type        = string
  default     = "prod-eks-cluster"
}

variable "node_group_name" {
  description = "EKS Node group name"
  type        = string
  default     = "prod-node-group"
}

variable "desired_capacity" {
  description = "Desired capacity for node group"
  type        = number
  default     = 2
}

variable "min_size" {
  description = "Minimum node count"
  type        = number
  default     = 1
}

variable "max_size" {
  description = "Maximum node count"
  type        = number
  default     = 3
}

variable "helm_release_name" {
  description = "Helm release name"
  type        = string
  default     = "currency-converter"
}

