resource "aws_security_group" "node_group_sg" {
  name        = "${var.cluster_name}-node-group-sg"
  description = "Security group for EKS Node Group SSH and application traffic"
  vpc_id      = var.vpc_id

  ingress {
    description = "Allow All Traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]  # Open to world. Restrict to your IP in production.
  }

  egress {
    description = "Allow all outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.cluster_name}-node-group-sg"
  }
}

resource "aws_eks_cluster" "eks" {
  name     = var.cluster_name
  role_arn = var.cluster_role_arn

  vpc_config {
    subnet_ids         = var.subnet_ids
    security_group_ids = [aws_security_group.node_group_sg.id]
  }

  depends_on = [aws_security_group.node_group_sg]
}

resource "aws_eks_node_group" "node_group" {
  cluster_name    = aws_eks_cluster.eks.name
  node_group_name = var.node_group_name
  node_role_arn   = var.node_role_arn
  subnet_ids      = var.subnet_ids

  scaling_config {
    desired_size = var.desired_capacity
    max_size     = var.max_size
    min_size     = var.min_size
  }

  remote_access {
    ec2_ssh_key               = "EKS-NODE"  # ✅ Your EC2 Key Pair name in AWS (without .pem)
    source_security_group_ids = [aws_security_group.node_group_sg.id]
  }

  depends_on = [aws_eks_cluster.eks]
}

output "cluster_endpoint" {
  value = aws_eks_cluster.eks.endpoint
}

output "cluster_name" {
  value = aws_eks_cluster.eks.name
}

output "kubeconfig" {
  value = <<EOT
apiVersion: v1
clusters:
- cluster:
    server: ${aws_eks_cluster.eks.endpoint}
  name: ${aws_eks_cluster.eks.name}
contexts:
- context:
    cluster: ${aws_eks_cluster.eks.name}
    user: aws
  name: ${aws_eks_cluster.eks.name}
current-context: ${aws_eks_cluster.eks.name}
kind: Config
preferences: {}
users:
- name: aws
  user:
    exec:
      apiVersion: client.authentication.k8s.io/v1beta1
      command: aws
      args:
        - "eks"
        - "get-token"
        - "--cluster-name"
        - "${aws_eks_cluster.eks.name}"
EOT
}

