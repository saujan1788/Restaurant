# main.tf in the root directory
provider "aws" {
  region = "eu-west-1"
}

data "aws_availability_zones" "available" {}

module "k8s_infra" {
  source             = "./modules/k8s_infra/"
  instance_count     = var.instance_count
  availability_zones = data.aws_availability_zones.available.names
}

variable "instance_count" {
  type    = number
  default = 3
}

