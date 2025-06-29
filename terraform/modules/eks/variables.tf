variable "cluster_name" {
  description = "EKS cluster name"
  type        = string
}

variable "node_group_name" {
  description = "Node group name"
  type        = string
}

variable "desired_capacity" {
  description = "Desired capacity for node group"
  type        = number
}

variable "max_size" {
  description = "Maximum node count"
  type        = number
}

variable "min_size" {
  description = "Minimum node count"
  type        = number
}

variable "vpc_id" {
  description = "VPC ID for EKS cluster networking"
  type        = string
}

variable "subnet_ids" {
  description = "Subnet IDs for worker nodes"
  type        = list(string)
}

variable "cluster_role_arn" {
  description = "IAM Role ARN for EKS control plane"
  type        = string
}

variable "node_role_arn" {
  description = "IAM Role ARN for EKS worker nodes"
  type        = string
}

