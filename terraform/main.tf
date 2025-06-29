module "vpc" {
  source     = "./modules/vpc"
  vpc_name   = var.vpc_name
  aws_region = var.aws_region
}

module "iam" {
  source        = "./modules/iam"
  cluster_name  = var.cluster_name
}

module "eks" {
  source           = "./modules/eks"
  cluster_name     = var.cluster_name
  node_group_name  = var.node_group_name
  desired_capacity = var.desired_capacity
  max_size         = var.max_size
  min_size         = var.min_size
  vpc_id           = module.vpc.vpc_id
  subnet_ids       = module.vpc.public_subnet_ids
  cluster_role_arn = module.iam.cluster_role_arn
  node_role_arn    = module.iam.node_role_arn
}

module "helm" {
  source            = "./modules/helm"
  helm_release_name = var.helm_release_name
  cluster_name      = module.eks.cluster_name
}


