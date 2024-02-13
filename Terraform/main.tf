provider "aws" {
	region = "eu-west-1"

}

data "aws_availability_zones" "available" {}

output "availability_zones"{
	value = data.aws_availability_zones.available.names
}

module "network"{
	source = "./modules/network/"
	# Pass the availability zones to the network module
	  availability_zones = data.aws_availability_zones.available.names
}
module "k8s_infra" {
  source = "./modules/k8s_infra/"

  ami_id            = "ami-0766b4b472db7e3b9"
  subnet_id         = "subnet-04ea76be2f2fa9fc2"
  security_group_id = "sg-06e98ed62b224d996"
}

