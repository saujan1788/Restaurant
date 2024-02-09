provider "aws" {
	region = "eu-west-1"

}

data "aws_availability_zones" "available" {}

output "availability_zones"{
	value = data.aws_availability_zones.available.names
}
