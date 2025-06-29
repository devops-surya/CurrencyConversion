resource "helm_release" "currency_converter" {
  name       = var.helm_release_name
  chart      = "../helm/currency-converter"
  namespace  = "default"
  create_namespace = true
}

