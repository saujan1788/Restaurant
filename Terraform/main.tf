provider "aws" {
  region = "eu-west-1"
}

data "aws_availability_zones" "available" {}

module "k8s_infra" {
  source = "./modules/k8s_infra/"

  availability_zones = data.aws_availability_zones.available.names
}

