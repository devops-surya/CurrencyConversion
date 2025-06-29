terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = ">= 2.27.0"
    }
    helm = {
      source  = "hashicorp/helm"
      version = ">= 2.13.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

############################
# Kubernetes Provider
############################
provider "kubernetes" {
  host                   = data.aws_eks_cluster.eks.endpoint
  cluster_ca_certificate = base64decode(data.aws_eks_cluster.eks.certificate_authority[0].data)
  token                  = data.aws_eks_cluster_auth.eks.token
}

############################
# Helm Provider (Fixed Format for Helm >=2.13.x)
############################
provider "helm" {
  kubernetes = {
    host                   = data.aws_eks_cluster.eks.endpoint
    cluster_ca_certificate = base64decode(data.aws_eks_cluster.eks.certificate_authority[0].data)
    token                  = data.aws_eks_cluster_auth.eks.token
  }
}


data "aws_eks_cluster" "eks" {
  name = var.cluster_name

  depends_on = [
    module.eks
  ]
}

data "aws_eks_cluster_auth" "eks" {
  name = var.cluster_name

  depends_on = [
    module.eks
  ]
}

